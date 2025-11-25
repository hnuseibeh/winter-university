"""
Macro-Economic Indicators Dashboard (Palestine & Morocco)
Explores: GDP growth, unemployment, youth unemployment, inflation
Source: p03_econ_social_crises canonical version
"""

import pathlib
import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_data


def run():
    """Main page runner function."""
    st.title("📈 Macro-Economic Indicators")
    st.markdown("""
    Explore simplified macro-economic indicators for **Palestine** and **Morocco**:
    GDP growth, unemployment, youth unemployment, and inflation.
    """)

    # Load data
    df = load_data("macro_indicators.csv")
    if df.empty:
        st.error("No data available. Please check that macro_indicators.csv exists in the data/ folder.")
        return

    # Sidebar filters
    st.sidebar.header("Dashboard Filters")
    country = st.sidebar.selectbox(
        "Country",
        sorted(df["country"].unique().tolist()) if "country" in df.columns else ["N/A"]
    )
    
    indicator = st.sidebar.selectbox(
        "Indicator",
        ["gdp_growth", "unemployment_rate", "youth_unemployment", "inflation_rate"],
    )

    # Filter data
    if "country" in df.columns:
        dff = df[df["country"] == country]
    else:
        dff = df

    # Indicator labels
    indicator_labels = {
        "gdp_growth": "GDP growth (%)",
        "unemployment_rate": "Unemployment rate (%)",
        "youth_unemployment": "Youth unemployment (%)",
        "inflation_rate": "Inflation rate (%)",
    }

    # Main chart
    st.subheader(f"{indicator_labels[indicator]} in {country} over time")
    
    if indicator in dff.columns:
        fig = px.line(
            dff,
            x="year" if "year" in dff.columns else dff.index,
            y=indicator,
            markers=True,
            title=f"{indicator_labels[indicator]} – {country}",
            labels={"year": "Year", indicator: indicator_labels[indicator]},
        )
        st.plotly_chart(fig, use_container_width=True)

        # Data table
        st.subheader("Data Table")
        if "year" in dff.columns:
            st.dataframe(dff[["year", indicator]].set_index("year") if "year" in dff.columns else dff[[indicator]])
        else:
            st.dataframe(dff[[indicator]])
    else:
        st.warning(f"Indicator '{indicator}' not found in dataset.")

    # Research context
    st.markdown("---")
    st.info("""
    **Research Context:**
    
    These indicators serve as early-warning signals for systemic economic stress:
    - **GDP growth decline** suggests aggregate demand shock or policy disruption
    - **Rising unemployment** indicates labor market dysfunction and economic stagnation
    - **Youth unemployment spike** reveals education-labor mismatch and social vulnerability
    - **Inflation acceleration** erodes purchasing power, esp. for vulnerable households
    
    In occupied/fragmented contexts like Palestine, these metrics are distorted by external 
    control over macroeconomic levers (currency, borders, tax revenues).
    """)
