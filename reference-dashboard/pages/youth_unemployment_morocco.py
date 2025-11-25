"""
Youth Unemployment by Region (Morocco)
Visualizes national vs urban vs rural disparities.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_data


def run():
    """Main page runner function."""
    st.title("👥 Youth Unemployment – Morocco (Regional Analysis)")
    st.markdown("""
    This page reveals **spatial inequality** masked by national averages.
    Compare youth unemployment across national, urban, and rural regions.
    """)

    # Load data
    df = load_data("morocco_youth_unemployment.csv")
    if df.empty:
        st.error("No data available. Please check that morocco_youth_unemployment.csv exists.")
        return

    st.subheader("Data Preview")
    st.dataframe(df.head(10))

    # Main chart: Regional trends
    st.subheader("Youth Unemployment Over Time")
    
    # Check which columns exist
    region_cols = [col for col in df.columns if col not in ['year', 'date', 'Year', 'Date']]
    
    if 'year' in df.columns or 'Year' in df.columns:
        year_col = 'year' if 'year' in df.columns else 'Year'
        
        if len(region_cols) > 0:
            # Plot multiple regions
            fig = px.line(
                df,
                x=year_col,
                y=region_cols,
                markers=True,
                title="Youth Unemployment by Region",
                labels={year_col: "Year", "value": "Unemployment Rate (%)"},
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("No regional columns found in data.")
    else:
        st.warning("No year column found in data.")

    # Regional statistics
    st.subheader("Regional Statistics")
    if region_cols:
        stats_df = df[region_cols].describe().T
        st.dataframe(stats_df[['mean', 'std', 'min', 'max']])

    # Research insights
    st.markdown("---")
    st.info("""
    **Why Regional Breakdown Matters:**
    
    National averages (e.g., "12% youth unemployment") mask profound spatial disparities:
    - **Urban centers** (Casablanca, Rabat) may have 8-10% youth unemployment
    - **Rural areas** (Atlas Mountains, coastal villages) can face 25-35% youth unemployment
    
    This spatial mismatch creates:
    - **Rural-to-urban migration pressure** (seeking jobs)
    - **Urban periphery overcrowding** (low-wage informal sector)
    - **Social volatility** (frustration among stranded rural youth)
    
    AI can disaggregate national data using satellite imagery, mobile phone data, and surveys 
    to target interventions more precisely.
    """)

    st.markdown("---")
    st.subheader("Analytical Questions")
    st.markdown("""
    - What drives urban-rural unemployment divergence?
    - How do education levels vary by region? Does this explain the gap?
    - What local industries could create jobs in high-unemployment rural areas?
    - How does seasonal agriculture affect youth employment patterns?
    - Can skills training reduce regional migration pressure?
    """)
