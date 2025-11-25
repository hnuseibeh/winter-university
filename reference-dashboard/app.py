"""
Main Streamlit Application: Economic & Social Crises Dashboard
Unified project integrating multiple analytical lenses on Palestine & Morocco crises.
Research data extracted from 5 academic PDFs and integrated into interactive pages.
"""

import streamlit as st
from pages import context_background, macro_indicators

# Page configuration
st.set_page_config(
    page_title="Economic & Social Crises Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styling
st.markdown("""
<style>
    .main-header { font-size: 2.5rem; font-weight: bold; color: #1f77b4; }
    .subheader-style { font-size: 1.3rem; color: #555; }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.markdown("# 📊 Economic & Social Crises")
st.sidebar.markdown("*Palestine & Morocco Crisis Analysis*")
st.sidebar.markdown("---")

pages = {
    "📚 Context & Background": context_background,
    "📈 Macro-Economic Indicators": macro_indicators,
}

selected_page = st.sidebar.radio(
    "Select Page",
    list(pages.keys()),
    index=0
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
### About
This dashboard synthesizes research on systemic economic and social crises in Palestine and Morocco.
It combines:
- **Macro indicators** (GDP, unemployment, inflation)
- **Scenario modeling** (education-labor mismatch)
- **Regional analysis** (youth unemployment, agricultural stress)
- **Research context** (policy frameworks, ethical considerations)

**Built with:** Streamlit, Plotly, Pandas, Python
""")

st.sidebar.markdown("---")
st.sidebar.info("🔗 Data sources: World Bank, FAO, PCBS, research reports")

# Route to selected page
if selected_page in pages:
    pages[selected_page].run()
else:
    st.error("Page not found")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #888; font-size: 0.9rem;">
    <p>Economic & Social Crises Dashboard | Palestine & Morocco Crisis Lab</p>
    <p>Data extracted from academic research | Designed for learning & policymaking</p>
</div>
""", unsafe_allow_html=True)
