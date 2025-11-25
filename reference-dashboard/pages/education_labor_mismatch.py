"""
Education-Labor Mismatch Scenario Modeler (Palestine)
Source: p06_education_labor_mismatch canonical version
Allows scenario projection with supply/demand growth assumptions.
"""

import pathlib
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
from utils.data_loader import load_data


DATA_PATH = pathlib.Path(__file__).parent.parent / "data" / "unemployment_by_field.csv"


def load_data_local() -> pd.DataFrame:
    """Load education-labor mismatch data."""
    try:
        df = pd.read_csv(DATA_PATH)
        df["year"] = df["year"].astype(int)
        df["unemployment_rate"] = df["unemployment_rate"].astype(float)
        df["graduates_supply_index"] = df["graduates_supply_index"].astype(float)
        df["jobs_demand_index"] = df["jobs_demand_index"].astype(float)
        return df
    except Exception as e:
        st.error(f"Could not load data: {e}")
        return pd.DataFrame()


def scenario_projection(df: pd.DataFrame, field: str, years_ahead: int,
                        supply_growth: float, demand_growth: float) -> pd.DataFrame:
    """
    Project graduate supply vs job demand under policy scenarios.
    """
    base = df[df["field"] == field].sort_values("year").copy()
    if base.empty:
        raise ValueError(f"No data for field {field!r}")

    last_year = int(base["year"].max())
    last_supply = float(base["graduates_supply_index"].iloc[-1])
    last_demand = float(base["jobs_demand_index"].iloc[-1])

    future_rows = []
    for t in range(1, years_ahead + 1):
        year = last_year + t
        supply = last_supply * ((1 + supply_growth) ** t)
        demand = last_demand * ((1 + demand_growth) ** t)
        future_rows.append({
            "year": year,
            "field": field,
            "graduates_supply_index": supply,
            "jobs_demand_index": demand,
        })

    future_df = pd.DataFrame(future_rows)
    future_df["unemployment_proxy"] = np.maximum(
        0,
        (future_df["graduates_supply_index"] - future_df["jobs_demand_index"])
        / np.maximum(future_df["graduates_supply_index"], 1e-6),
    ) * 100.0

    return future_df


def run():
    """Main page runner function."""
    st.title("🎓 Education–Labor Mismatch in Palestine")
    st.markdown("""
    This dashboard explores the **mismatch between higher education outputs and labor market needs**
    in Palestine. Adjust the policy levers to see how different scenarios affect unemployment pressure.
    """)

    df = load_data_local()
    if df.empty:
        st.error("Could not load data. Please check that unemployment_by_field.csv exists.")
        return

    # Sidebar controls
    st.sidebar.header("Scenario Settings")
    fields = sorted(df["field"].unique())
    selected_field = st.sidebar.selectbox("Select a field of study:", fields, index=0 if fields else None)

    years_ahead = st.sidebar.slider("Projection horizon (years):", 3, 20, 10)

    st.sidebar.markdown("**Annual growth assumptions**")
    supply_growth_pct = st.sidebar.slider(
        "Graduate supply growth (% per year):", -5.0, 15.0, 5.0, step=0.5
    )
    demand_growth_pct = st.sidebar.slider(
        "Job demand growth (% per year):", -5.0, 15.0, 2.0, step=0.5
    )

    supply_growth = supply_growth_pct / 100.0
    demand_growth = demand_growth_pct / 100.0

    if selected_field:
        hist = df[df["field"] == selected_field].sort_values("year")

        # Historical unemployment
        st.subheader(f"Historical unemployment rate – {selected_field}")
        if "unemployment_rate" in hist.columns:
            fig_hist = px.line(
                hist,
                x="year",
                y="unemployment_rate",
                markers=True,
                labels={"year": "Year", "unemployment_rate": "Unemployment rate (%)"},
                title=f"Observed unemployment rate in {selected_field}",
            )
            st.plotly_chart(fig_hist, use_container_width=True)

        # Scenario projection
        try:
            proj = scenario_projection(hist, selected_field, years_ahead, supply_growth, demand_growth)

            st.subheader("Scenario: graduate supply vs job demand")
            combined = proj[["year", "graduates_supply_index", "jobs_demand_index"]].melt(
                id_vars="year",
                var_name="indicator",
                value_name="index_value",
            )
            indicator_labels = {
                "graduates_supply_index": "Graduate supply (index)",
                "jobs_demand_index": "Job demand (index)",
            }
            combined["indicator"] = combined["indicator"].map(indicator_labels)

            fig_proj = px.line(
                combined,
                x="year",
                y="index_value",
                color="indicator",
                markers=True,
                labels={"index_value": "Index (normalized)", "year": "Year"},
                title=f"Projected graduate supply vs job demand – {selected_field}",
            )
            st.plotly_chart(fig_proj, use_container_width=True)

            st.subheader("Projected unemployment pressure (proxy)")
            fig_unemp = px.bar(
                proj,
                x="year",
                y="unemployment_proxy",
                labels={"unemployment_proxy": "Unemployment pressure (%)", "year": "Year"},
                title="Approximate unemployment pressure under this scenario",
            )
            st.plotly_chart(fig_unemp, use_container_width=True)

            # Summary metrics
            last_row = proj.iloc[-1]
            st.markdown("### Summary at end of horizon")
            col1, col2, col3 = st.columns(3)
            col1.metric("Year", int(last_row["year"]))
            col2.metric("Supply index", f"{last_row['graduates_supply_index']:.2f}")
            col3.metric("Job demand index", f"{last_row['jobs_demand_index']:.2f}")

            st.info(f"""
            Under the current assumptions (supply growth = {supply_growth_pct:.1f}% per year,
            job demand growth = {demand_growth_pct:.1f}% per year), the **unemployment pressure**
            in {int(last_row['year'])} is approximately **{last_row['unemployment_proxy']:.1f}%**.

            **Policy Levers:**
            - Reduce graduate intake in saturated fields (↓ supply growth)
            - Stimulate job creation in key sectors (↑ demand growth)
            - Target skills training to high-demand fields
            - Support migration to labor-scarce regions
            """)

        except Exception as e:
            st.error(f"Could not generate projection: {e}")
    
    # Research context
    st.markdown("---")
    st.markdown("""
    **Research Context:**
    
    The education-labor mismatch is a critical driver of youth unemployment in Palestine and Morocco.
    When graduate supply vastly exceeds job demand, unemployment rises even as economies grow. This 
    scenario builder allows policymakers and students to test different assumptions about:
    - Population growth & education intake
    - Job creation & sectoral shifts
    - Policy interventions
    """)
