"""
Education-Labor Mismatch Dashboard
===================================

This module explores the mismatch between higher education outputs and labor market needs
in Palestine. Students can use scenario analysis features to understand how changes in graduate
supply and job demand might affect unemployment in different fields of study.

Key concepts:
- Graduate supply index: Measures the number of graduates in a field
- Jobs demand index: Measures the number of available job opportunities
- Unemployment proxy: Estimated based on the gap between supply and demand
"""

import pathlib
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st


# Data path for Palestine unemployment by field of study
DATA_PATH = pathlib.Path(__file__).parent.parent / "data" / "palestine" / "unemployment_by_field.csv"


def load_data() -> pd.DataFrame:
    """
    Load and prepare unemployment data from CSV file.

    The data contains historical unemployment rates and indices for graduate supply
    and job demand across different fields of study in Palestine.

    Returns:
        pd.DataFrame: Processed data with proper data types for analysis
    """
    df = pd.read_csv(DATA_PATH)
    df["year"] = df["year"].astype(int)
    df["unemployment_rate"] = df["unemployment_rate"].astype(float)
    df["graduates_supply_index"] = df["graduates_supply_index"].astype(float)
    df["jobs_demand_index"] = df["jobs_demand_index"].astype(float)
    return df


def scenario_projection(df: pd.DataFrame, field: str, years_ahead: int,
                        supply_growth: float, demand_growth: float) -> pd.DataFrame:
    """
    Project future graduate supply and job demand for a specific field.

    This function creates a scenario by projecting current trends forward using
    user-defined growth rates. Students can experiment with different scenarios
    to understand how policy changes (e.g., reduced program enrollment or job creation)
    might affect unemployment.

    Args:
        df (pd.DataFrame): Historical data for a specific field
        field (str): Field of study to project
        years_ahead (int): Number of years to project into the future
        supply_growth (float): Annual graduate supply growth rate (as decimal, e.g., 0.05 for 5%)
        demand_growth (float): Annual job demand growth rate (as decimal, e.g., 0.02 for 2%)

    Returns:
        pd.DataFrame: Projected data with supply, demand, and unemployment proxy values
    """
    base = df[df["field"] == field].sort_values("year").copy()
    if base.empty:
        raise ValueError(f"No data for field {field!r}")

    # Get the most recent values from historical data
    last_year = int(base["year"].max())
    last_supply = float(base["graduates_supply_index"].iloc[-1])
    last_demand = float(base["jobs_demand_index"].iloc[-1])

    # Generate future year projections
    future_rows = []
    for t in range(1, years_ahead + 1):
        year = last_year + t
        # Apply exponential growth to both supply and demand
        supply = last_supply * ((1 + supply_growth) ** t)
        demand = last_demand * ((1 + demand_growth) ** t)
        future_rows.append(
            {
                "year": year,
                "field": field,
                "graduates_supply_index": supply,
                "jobs_demand_index": demand,
            }
        )

    future_df = pd.DataFrame(future_rows)

    # Calculate unemployment proxy: percentage of graduates without jobs
    # Formula: (supply - demand) / supply * 100
    # This is capped at 0 to represent at least zero unemployment
    future_df["unemployment_proxy"] = np.maximum(
        0,
        (future_df["graduates_supply_index"] - future_df["jobs_demand_index"])
        / np.maximum(future_df["graduates_supply_index"], 1e-6),
    ) * 100.0

    return future_df


def run():
    """
    Main dashboard application for education-labor mismatch analysis.

    This function creates the Streamlit interface where students can:
    1. Select a field of study
    2. Adjust projection horizon and growth assumptions
    3. Visualize historical unemployment trends
    4. Explore scenario projections
    5. Analyze the unemployment pressure under different policies
    """
    st.title("Education–Labor Mismatch in Palestine")
    st.markdown(
        """
        This dashboard explores the **mismatch between higher education outputs and labor market needs**
        in Palestine using sample data on unemployment by field of study and scenario simulations.

        **How to use this dashboard:**
        - Use the sidebar to select a field of study and adjust growth assumptions
        - Observe how different policy scenarios affect unemployment projections
        - Consider: What policies could reduce education-labor mismatch?
        """
    )

    # Load the data
    df = load_data()

    # SIDEBAR CONTROLS FOR SCENARIO ANALYSIS
    st.sidebar.header("Scenario Settings")

    # Let students choose which field of study to analyze
    fields = sorted(df["field"].unique())
    selected_field = st.sidebar.selectbox(
        "Select a field of study:",
        fields,
        index=0,
        help="Choose a field to analyze its unemployment and supply-demand dynamics"
    )

    # Students can adjust how far into the future to project
    years_ahead = st.sidebar.slider(
        "Projection horizon (years):",
        3, 20, 10,
        help="How many years ahead should we project? Longer horizons show more dramatic changes."
    )

    # Growth rate assumptions - students experiment with different policy scenarios
    st.sidebar.markdown("**Annual growth assumptions** (adjust to explore scenarios)")
    supply_growth_pct = st.sidebar.slider(
        "Graduate supply growth (% per year):",
        -5.0, 15.0, 5.0,
        step=0.5,
        help="Negative values = fewer graduates; positive = more graduates. What happens if we reduce intake?"
    )
    demand_growth_pct = st.sidebar.slider(
        "Job demand growth (% per year):",
        -5.0, 15.0, 2.0,
        step=0.5,
        help="Negative = fewer jobs; positive = job creation. What if government stimulates job creation?"
    )

    # Convert percentages to decimal form for calculations
    supply_growth = supply_growth_pct / 100.0
    demand_growth = demand_growth_pct / 100.0

    # Filter data for selected field
    hist = df[df["field"] == selected_field].sort_values("year")

    # VISUALIZATION 1: HISTORICAL UNEMPLOYMENT RATE
    st.subheader(f"Historical unemployment rate – {selected_field}")
    st.markdown(
        """
        *This chart shows actual unemployment rates in the field over time.
        What trend do you observe? Is unemployment rising or falling?*
        """
    )
    fig_hist = px.line(
        hist,
        x="year",
        y="unemployment_rate",
        markers=True,
        labels={"year": "Year", "unemployment_rate": "Unemployment rate (%)"},
        title=f"Observed unemployment rate in {selected_field}",
    )
    st.plotly_chart(fig_hist, use_container_width=True)

    # SCENARIO PROJECTION
    proj = scenario_projection(hist, selected_field, years_ahead, supply_growth, demand_growth)

    # VISUALIZATION 2: SUPPLY VS DEMAND
    st.subheader("Scenario: graduate supply vs job demand")
    st.markdown(
        """
        *This chart projects future graduate supply (blue) and job demand (orange)
        under your chosen growth assumptions. When does supply exceed demand?*
        """
    )
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

    # VISUALIZATION 3: UNEMPLOYMENT PRESSURE
    st.subheader("Projected unemployment pressure (proxy)")
    st.markdown(
        """
        *This chart estimates unemployment based on the gap between supply and demand.
        If supply grows faster than demand, unemployment pressure increases.*
        """
    )
    fig_unemp = px.bar(
        proj,
        x="year",
        y="unemployment_proxy",
        labels={"unemployment_proxy": "Unemployment pressure (%)", "year": "Year"},
        title="Approximate unemployment pressure under this scenario",
    )
    st.plotly_chart(fig_unemp, use_container_width=True)

    # SUMMARY METRICS
    last_row = proj.iloc[-1]
    st.markdown("### Summary at end of projection horizon")
    col1, col2, col3 = st.columns(3)
    col1.metric("Final year", int(last_row["year"]))
    col2.metric("Supply index", f"{last_row['graduates_supply_index']:.2f}")
    col3.metric("Job demand index", f"{last_row['jobs_demand_index']:.2f}")

    # INSIGHTS AND DISCUSSION
    st.info(
        f"""
        **Key Finding:** Under the current assumptions (supply growth = {supply_growth_pct:.1f}% per year,
        job demand growth = {demand_growth_pct:.1f}% per year), the **unemployment pressure**
        in {int(last_row['year'])} is approximately **{last_row['unemployment_proxy']:.1f}%**.

        **For discussion:**
        - What happens if you reduce graduate supply (negative supply growth)?
        - What happens if you increase job demand growth (stimulus)?
        - Which fields show the worst education-labor mismatch?
        - What policies could help reduce this mismatch?

        **Note:** This unemployment proxy is a simplified estimate based on relative supply and demand.
        Real unemployment depends on many other factors!
        """
    )


# Entry point for the page
if __name__ == "__main__":
    run()
