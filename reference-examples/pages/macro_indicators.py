"""
Macro Indicators Dashboard
===========================

This page displays key macroeconomic indicators for selected countries,
including GDP growth, unemployment rates, youth unemployment, and inflation.

Students can explore how these indicators have changed over time and compare
patterns across different countries.
"""

from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


# Define the path to the data file
DATA_PATH = Path(__file__).parents[1] / "data" / "macro" / "econ_indicators.csv"


def load_data() -> pd.DataFrame:
    """
    Load economic indicators data from CSV file.

    Returns:
        pd.DataFrame: DataFrame containing country, year, and indicator columns
    """
    df = pd.read_csv(DATA_PATH)
    return df


def run():
    """
    Main function to run the Macro Indicators dashboard.

    This function:
    1. Displays the page title and description
    2. Loads the economic data
    3. Provides filters for country and indicator selection
    4. Displays a line chart showing the selected indicator over time
    5. Shows a data table with the underlying values
    """

    # Page title and description
    st.title("📈 Economic & Social Crises – Macro Indicators")
    st.markdown(
        """
        Explore simplified macro-economic indicators for **Palestine** and **Morocco**:

        - **GDP growth**: Annual percentage change in economic output
        - **Unemployment rate**: Percentage of labor force without employment
        - **Youth unemployment**: Unemployment rate among young people (typically 15-24 years)
        - **Inflation rate**: Annual percentage change in consumer prices
        """
    )

    # Load the data
    df = load_data()

    # Create sidebar filters
    st.sidebar.header("Filters")

    # Filter 1: Select country
    country = st.sidebar.selectbox(
        "Country",
        sorted(df["country"].unique().tolist()),
        help="Choose a country to view its economic indicators"
    )

    # Filter 2: Select indicator
    indicator = st.sidebar.selectbox(
        "Indicator",
        ["gdp_growth", "unemployment_rate", "youth_unemployment", "inflation_rate"],
        help="Select which economic indicator you want to explore"
    )

    # Filter data for selected country
    dff = df[df["country"] == country]

    # Map indicator column names to human-readable labels
    indicator_labels = {
        "gdp_growth": "GDP growth (%)",
        "unemployment_rate": "Unemployment rate (%)",
        "youth_unemployment": "Youth unemployment (%)",
        "inflation_rate": "Inflation rate (%)",
    }

    # Display line chart showing indicator over time
    st.subheader(f"{indicator_labels[indicator]} in {country} over time")
    fig = px.line(
        dff,
        x="year",
        y=indicator,
        markers=True,
        title=f"{indicator_labels[indicator]} – {country}",
        labels={"year": "Year", indicator: indicator_labels[indicator]},
    )
    st.plotly_chart(fig, use_container_width=True)

    # Display data table
    st.subheader("Data table")
    st.dataframe(dff[["year", indicator]].set_index("year"))
