"""
Winter School 2025 - Economic & Social Crises Dashboard
Main entry point for the unified Streamlit application
"""
import streamlit as st
from pages import (
    macro_indicators,
    youth_unemployment,
    education_labor_mismatch,
    agricultural_stress,
    checkpoint_monitor,
    micro_enterprises,
    household_budgets,
    data_explorer
)

# Page configuration
st.set_page_config(
    page_title="Economic & Social Crises",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define all available pages
PAGES = {
    "📊 Macro Indicators": macro_indicators,
    "👥 Youth Unemployment (Morocco)": youth_unemployment,
    "🎓 Education-Labor Mismatch (Palestine)": education_labor_mismatch,
    "🌾 Agricultural Stress (Morocco)": agricultural_stress,
    "🚧 Checkpoint Monitor (Jerusalem)": checkpoint_monitor,
    "🏪 Micro-Enterprises (Jerusalem)": micro_enterprises,
    "💰 Household Budgets (Palestine)": household_budgets,
    "🔍 Data Explorer": data_explorer
}

# Sidebar navigation
st.sidebar.title("🎓 Winter School 2025")
st.sidebar.markdown("### Economic & Social Crises")
st.sidebar.markdown("Palestine & Morocco")
st.sidebar.markdown("---")

# Page selection
selected_page = st.sidebar.radio(
    "Select Dashboard:",
    list(PAGES.keys()),
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.markdown("**About this project:**")
st.sidebar.markdown(
    "Interactive dashboards exploring economic and social crisis indicators "
    "in Palestine and Morocco. Built for educational purposes."
)

# Run the selected page
PAGES[selected_page].run()
