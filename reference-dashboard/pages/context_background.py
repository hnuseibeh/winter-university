"""
Context & Background page: Research foundations and analytical frameworks.
"""

import streamlit as st
from pathlib import Path
import sys

# Import context data from parent directory
sys.path.insert(0, str(Path(__file__).parent.parent))
from context_data import RESEARCH_CONTEXT, KEY_INSIGHTS, NARRATIVES


def run():
    """Main page runner function."""
    st.set_page_config(page_title="Context & Background", layout="wide")
    
    st.title("📚 Research Context & Background")
    st.markdown("""
    This project is grounded in rigorous academic research on economic and social crises in 
    **Palestine** and **Morocco**. The following provides a synthesis of key findings, analytical 
    frameworks, and data sources that inform the dashboards.
    """)
    
    st.markdown("---")
    
    # About section
    st.header("About This Project")
    st.markdown(RESEARCH_CONTEXT["about"]["description"])
    
    st.markdown("---")
    
    # Tabs for different contexts
    tab1, tab2, tab3, tab4 = st.tabs(["🇵🇸 Palestine", "🇲🇦 Morocco", "🤖 AI Methods", "📖 Research Stories"])
    
    with tab1:
        st.subheader("Palestine: Economics of Strangulation & Fragmentation")
        st.markdown("""
        Palestine's economy operates under unique structural constraints: it is a **"truncated economy"** 
        where primary macroeconomic levers—currency, borders, trade revenue—are controlled externally.
        """)
        
        for challenge in RESEARCH_CONTEXT["palestine"]["key_challenges"]:
            with st.expander(f"📌 {challenge['name']}", expanded=False):
                st.markdown(f"**{challenge['description']}**")
                st.markdown("**Key Indicators:**")
                for indicator in challenge["indicators"]:
                    st.write(f"• {indicator}")
        
        st.markdown("**Economic Metrics:**")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(
                "GDP Loss (2000-2020)",
                "$45B",
                "Cumulative due to occupation"
            )
        with col2:
            st.metric(
                "Residency Revocations",
                "14,500+",
                "Since 1967"
            )
        with col3:
            st.metric(
                "Population at Risk",
                "100,000+",
                "Home demolition risk"
            )
    
    with tab2:
        st.subheader("Morocco: Vulnerability to Climate & Inequality")
        st.markdown("""
        Morocco faces a **"polycrisis"**: climate-induced volatility, entrenched structural unemployment, 
        and spatial inequality that national averages mask.
        """)
        
        for challenge in RESEARCH_CONTEXT["morocco"]["key_challenges"]:
            with st.expander(f"📌 {challenge['name']}", expanded=False):
                st.markdown(f"**{challenge['description']}**")
                st.markdown("**Key Indicators:**")
                for indicator in challenge["indicators"]:
                    st.write(f"• {indicator}")
        
        st.markdown("**Economic Context:**")
        st.info("""
        - **Open Data Ranking:** 24th globally (high transparency, but masking regional disparities)
        - **Primary Challenge:** Rain-fed GDP volatility → Rural income collapse → Urban migration → Social unrest
        - **Lead Time Opportunity:** Satellite vegetation indices (NDVI) provide 2-4 month warning of agricultural shocks
        """)
    
    with tab3:
        st.subheader("AI & Crisis Prediction Methodologies")
        st.markdown("""
        The dashboards employ four primary AI/data methodologies to transform crisis prediction 
        from reactive damage control to proactive anticipation:
        """)
        
        for method_info in RESEARCH_CONTEXT["ai_applications"]["methods"]:
            col1, col2 = st.columns([2, 3])
            with col1:
                st.subheader(f"🔬 {method_info['method']}")
            with col2:
                st.markdown(f"**Use:** {method_info['use']}")
                st.markdown(f"**Example:** {method_info['example']}")
            st.divider()
        
        st.warning("**Ethical Considerations:**")
        for consideration in RESEARCH_CONTEXT["ai_applications"]["ethical_considerations"]:
            st.write(f"⚠️ {consideration}")
    
    with tab4:
        st.subheader("Research Stories & Narratives")
        st.markdown("""
        Beyond numbers, these crises manifest in lived experiences. The following narratives 
        translate quantitative indicators into human context:
        """)
        
        for key, narrative in NARRATIVES.items():
            with st.expander(f"📖 {narrative['title']}", expanded=False):
                st.markdown(narrative["story"])
    
    st.markdown("---")
    
    # Key insights quick reference
    st.subheader("🔑 Key Research Insights (Quick Reference)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Palestine**")
        for topic, insight in list(KEY_INSIGHTS.items())[:3]:
            st.write(f"• {insight}")
    
    with col2:
        st.markdown("**Morocco**")
        for topic, insight in list(KEY_INSIGHTS.items())[3:]:
            st.write(f"• {insight}")
    
    st.markdown("---")
    
    # Dataset rationale
    st.subheader("📊 Why These Datasets Matter")
    st.markdown("""
    Each page in this dashboard corresponds to specific research findings and analytical questions:
    """)
    
    for page_name, page_info in RESEARCH_CONTEXT["datasets_rationale"].items():
        with st.expander(page_info["title"], expanded=False):
            st.markdown(f"**Rationale:** {page_info['rationale']}")
            if "interactive_elements" in page_info:
                st.markdown("**Interactive Elements:**")
                for element in page_info["interactive_elements"]:
                    st.write(f"- {element}")
            if "feature" in page_info:
                st.markdown(f"**Key Feature:** {page_info['feature']}")
            if "metrics" in page_info:
                st.markdown("**Key Metrics:**")
                for metric in page_info["metrics"]:
                    st.write(f"- {metric}")
    
    st.markdown("---")
    
    st.markdown("""
    **📚 Data Sources:**
    - Palestinian Central Bureau of Statistics (PCBS)
    - World Bank (Morocco economic indicators)
    - FAO (Agricultural data)
    - Research reports on East Jerusalem, Gaza, and regional economic crises
    
    **🔗 Next Steps:**
    - Explore the dashboards using the sidebar menu
    - Adjust filters and scenario parameters to understand policy impacts
    - Consider how technology can serve transparency and justice
    """)
