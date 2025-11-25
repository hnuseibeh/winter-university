"""
Educational Wizard for Economic & Social Crises Dashboard
Interactive guide to help students explore and understand data.
"""

import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px

st.set_page_config(
    page_title="Crisis Dashboard Wizard",
    page_icon="🧙",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# SESSION STATE
# ============================================================================

if 'wizard_step' not in st.session_state:
    st.session_state.wizard_step = 'welcome'

if 'student_name' not in st.session_state:
    st.session_state.student_name = ""

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def load_data(filename):
    """Load CSV data from dashboard."""
    data_path = Path(__file__).parent / "reference-dashboard" / "data" / filename
    if data_path.exists():
        return pd.read_csv(data_path)
    return None

def go_to_step(step_name):
    """Navigate to a wizard step."""
    st.session_state.wizard_step = step_name

# ============================================================================
# WIZARD PAGES
# ============================================================================

def page_welcome():
    """Welcome page."""
    st.title("🧙 Crisis Dashboard Wizard")
    st.write("Learn how to explore real-world data on Palestinian & Moroccan crises")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📚 What You'll Learn")
        st.markdown("""
        - Understanding crisis data
        - Exploring real datasets
        - Data visualization basics
        - Critical analysis skills
        - Exporting your findings
        """)
    
    with col2:
        st.subheader("🌍 Case Studies")
        st.markdown("""
        **Palestine:**
        - Humanitarian crisis tracking
        - Economic collapse indicators
        
        **Morocco:**
        - Climate vulnerability
        - Youth unemployment patterns
        """)
    
    st.divider()
    
    # Learning path selection
    st.subheader("Choose Your Path")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("⚡ Quick Start (5 min)", use_container_width=True, key="btn_quick"):
            go_to_step("quick_start")
            st.rerun()
        
        if st.button("📊 Data Explorer", use_container_width=True, key="btn_explorer"):
            go_to_step("data_explorer")
            st.rerun()
    
    with col2:
        if st.button("📖 Full Tutorial (20 min)", use_container_width=True, key="btn_full"):
            go_to_step("learning_lessons")
            st.rerun()
        
        if st.button("📤 Export Analysis", use_container_width=True, key="btn_export"):
            go_to_step("export_analysis")
            st.rerun()
    
    st.divider()
    
    # Name input
    student_name = st.text_input("What's your name? (optional)")
    if student_name:
        st.session_state.student_name = student_name


def page_quick_start():
    """Quick introduction."""
    st.title("⚡ Quick Start")
    st.write("5-minute overview of key datasets")
    
    st.subheader("📊 Key Datasets")
    
    datasets_info = [
        ("humanitarian_indicators.csv", "🚨 Humanitarian Crisis", "Displacement, deaths, infrastructure damage"),
        ("climate_vulnerability_index.csv", "🌍 Climate Vulnerability", "Temperature projections, water stress"),
        ("crisis_timeline.csv", "📅 Crisis Events", "Timestamped events with impact"),
        ("agricultural_stress.csv", "🌾 Agricultural Stress", "Regional drought data (Morocco)"),
        ("sentiment_index.csv", "📈 Sentiment Index", "Crisis scores (0-10 scale)"),
        ("news_summary.csv", "📰 News Summary", "Recent topics and frequency"),
    ]
    
    for filename, title, description in datasets_info:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown(f"**{title}**")
            st.caption(description)
        
        df = load_data(filename)
        if df is not None:
            with col2:
                st.metric("Rows", len(df))
            st.dataframe(df, use_container_width=True, hide_index=True)
        
        st.divider()
    
    # Navigation
    col1, col2 = st.columns(2)
    with col1:
        if st.button("← Back", use_container_width=True, key="back_quick"):
            go_to_step("welcome")
            st.rerun()
    with col2:
        if st.button("Next →", use_container_width=True, key="next_quick"):
            go_to_step("learning_lessons")
            st.rerun()


def page_data_explorer():
    """Interactive data exploration."""
    st.title("📊 Data Explorer")
    st.write("Browse and visualize datasets")
    
    available_datasets = {
        "humanitarian_indicators.csv": "🚨 Humanitarian Indicators",
        "climate_vulnerability_index.csv": "🌍 Climate Vulnerability",
        "agricultural_stress.csv": "🌾 Agricultural Stress",
        "crisis_timeline.csv": "📅 Crisis Timeline",
        "sentiment_index.csv": "📈 Sentiment Index",
        "news_summary.csv": "📰 News Summary"
    }
    
    selected_dataset = st.selectbox(
        "Choose a dataset:",
        options=list(available_datasets.keys()),
        format_func=lambda x: available_datasets[x]
    )
    
    df = load_data(selected_dataset)
    
    if df is not None:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown(f"**{available_datasets[selected_dataset]}**")
            st.write(f"{len(df)} rows × {len(df.columns)} columns")
        
        with col2:
            st.download_button(
                label="⬇️ Download CSV",
                data=df.to_csv(index=False),
                file_name=selected_dataset,
                mime="text/csv"
            )
        
        # Display data
        st.markdown("### Data Table")
        st.dataframe(df, use_container_width=True, height=300)
        
        # Column info
        st.markdown("### Column Information")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Columns:**")
            for col_name in df.columns:
                dtype = str(df[col_name].dtype)
                st.caption(f"`{col_name}` → {dtype}")
        
        with col2:
            st.markdown("**Summary Statistics:**")
            st.dataframe(df.describe())
        
        # Visualization
        st.markdown("### Quick Visualization")
        numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
        
        if numeric_cols:
            viz_col = st.selectbox("Column to visualize:", numeric_cols)
            
            if len(df) > 0:
                fig = px.bar(
                    df,
                    x=df.columns[0],
                    y=viz_col,
                    title=f"{viz_col} Analysis"
                )
                st.plotly_chart(fig, use_container_width=True)
    
    # Navigation
    col1, col2 = st.columns(2)
    with col1:
        if st.button("← Back", use_container_width=True, key="back_explorer"):
            go_to_step("welcome")
            st.rerun()
    with col2:
        if st.button("Next →", use_container_width=True, key="next_explorer"):
            go_to_step("learning_lessons")
            st.rerun()


def page_learning_lessons():
    """Educational content."""
    st.title("📖 Understanding the Data")
    st.write("Context and analysis for Palestinian & Moroccan crises")
    
    tab1, tab2, tab3 = st.tabs(["🇵🇸 Palestine", "🇲🇦 Morocco", "💡 Tips"])
    
    with tab1:
        st.markdown("""
        ## Palestinian Crisis
        
        ### Humanitarian Indicators
        - **Deaths & Injured:** 70,000+ deaths, 180,000+ injured
        - **Displaced:** ~2 million internally displaced persons
        - **Infrastructure:** 190,000+ buildings damaged
        - **Detained:** 18,000+ people
        
        ### Economic Impact
        - **GDP:** Severe contraction
        - **Unemployment:** 40%+ in some areas
        - **Poverty:** 35%+ rate
        
        ### Movement Restrictions
        - 600+ checkpoints limiting movement
        - Trade disruption
        - Healthcare access challenges
        """)
        
        df = load_data("humanitarian_indicators.csv")
        if df is not None:
            st.markdown("#### Current Data")
            st.dataframe(df[df['Country'] == 'Palestine'], use_container_width=True)
    
    with tab2:
        st.markdown("""
        ## Moroccan Crisis
        
        ### Climate Challenges
        - **Temperature:** +1.5°C by 2050
        - **Precipitation:** -12% decrease
        - **Drought Risk:** High in southern regions
        
        ### Agricultural Impact
        - Regional drought in Draa-Tafilalet, Guelmim-Oued Noun
        - Crop yields declining 8-12% annually
        - Farmer income below poverty line
        
        ### Youth & Employment
        - Unemployment: 12-15% nationally
        - Rural areas hit harder
        - Skills-demand mismatch
        """)
        
        df = load_data("climate_vulnerability_index.csv")
        if df is not None:
            st.markdown("#### Climate Data")
            st.dataframe(df, use_container_width=True)
    
    with tab3:
        st.markdown("""
        ## Analysis Tips
        
        ### Questions to Ask
        1. **Trends:** Is situation improving or worsening?
        2. **Comparison:** How do Palestine & Morocco differ?
        3. **Causes:** What factors created these crises?
        4. **Solutions:** What interventions could help?
        
        ### Data Quality Notes
        - Some data limited by crisis conditions
        - Real-time data may have reporting delays
        - Consider source bias and validation
        """)
    
    # Navigation
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("← Back", use_container_width=True, key="back_lessons"):
            go_to_step("data_explorer")
            st.rerun()
    with col2:
        if st.button("🏠 Home", use_container_width=True, key="home_lessons"):
            go_to_step("welcome")
            st.rerun()
    with col3:
        if st.button("Next →", use_container_width=True, key="next_lessons"):
            go_to_step("export_analysis")
            st.rerun()


def page_export_analysis():
    """Data export and reporting."""
    st.title("📤 Export & Report")
    st.write("Download data and create analysis reports")
    
    st.subheader("📥 Download Datasets")
    
    available_datasets = {
        "humanitarian_indicators.csv": "🚨 Humanitarian Indicators",
        "climate_vulnerability_index.csv": "🌍 Climate Vulnerability",
        "agricultural_stress.csv": "🌾 Agricultural Stress",
        "crisis_timeline.csv": "📅 Crisis Timeline",
        "sentiment_index.csv": "📈 Sentiment Index",
        "news_summary.csv": "📰 News Summary"
    }
    
    cols = st.columns(2)
    for idx, (filename, label) in enumerate(available_datasets.items()):
        df = load_data(filename)
        if df is not None:
            with cols[idx % 2]:
                st.download_button(
                    label=f"⬇️ {label}",
                    data=df.to_csv(index=False),
                    file_name=filename,
                    mime="text/csv",
                    use_container_width=True
                )
    
    st.divider()
    
    st.subheader("📋 Create Analysis Report")
    
    with st.form("analysis_form"):
        report_title = st.text_input("Report Title:", value="My Crisis Analysis")
        research_question = st.text_area(
            "Research Question:",
            placeholder="What are you investigating?"
        )
        findings = st.text_area(
            "Key Findings:",
            placeholder="What did you discover?"
        )
        
        submitted = st.form_submit_button("Generate Report", use_container_width=True)
        
        if submitted and report_title and research_question:
            st.success("Report generated!")
            
            author_name = st.session_state.student_name or "Student"
            
            report = f"""# {report_title}

**Author:** {author_name}  
**Date:** {pd.Timestamp.now().strftime('%Y-%m-%d')}

## Research Question
{research_question}

## Findings
{findings}

## Data Sources
- Palestinian Central Bureau of Statistics
- Morocco High Commission of Planning  
- UN OCHA & FAO
- World Bank Open Data
"""
            
            st.download_button(
                label="📄 Download Report",
                data=report,
                file_name=f"{report_title.lower().replace(' ', '_')}_report.md",
                mime="text/markdown",
                use_container_width=True
            )
    
    st.divider()
    
    # Navigation
    col1, col2 = st.columns(2)
    with col1:
        if st.button("← Back", use_container_width=True, key="back_export"):
            go_to_step("learning_lessons")
            st.rerun()
    with col2:
        if st.button("Finish 🎓", use_container_width=True, key="finish_export"):
            go_to_step("completion")
            st.rerun()


def page_completion():
    """Completion page."""
    st.title("🎓 Congratulations!")
    st.write("You've completed the Crisis Dashboard Wizard")
    
    if st.session_state.student_name:
        st.success(f"Great work, {st.session_state.student_name}! 👋")
    
    st.markdown("""
    ### What You Learned:
    ✅ Understanding crisis data indicators  
    ✅ Exploring datasets from official sources  
    ✅ Visualizing humanitarian and climate data  
    ✅ Analyzing Palestinian & Moroccan crises  
    ✅ Creating analysis reports  
    
    ### Next Steps:
    1. **Create your own analysis** using the data
    2. **Share findings** with your class
    3. **Explore the full dashboard** for deeper analysis
    4. **Download datasets** for your research projects
    """)
    
    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Start Over", use_container_width=True, key="restart"):
            st.session_state.wizard_step = "welcome"
            st.rerun()
    with col2:
        st.info("Check sidebar for more resources")


# ============================================================================
# MAIN APP
# ============================================================================

def main():
    """Main application router."""
    
    # Sidebar
    with st.sidebar:
        st.title("🧙 Navigation")
        
        nav_pages = [
            ("🏠 Home", "welcome"),
            ("⚡ Quick Start", "quick_start"),
            ("📊 Data Explorer", "data_explorer"),
            ("📖 Lessons", "learning_lessons"),
            ("📤 Export", "export_analysis"),
            ("🎓 Completion", "completion"),
        ]
        
        for label, page_key in nav_pages:
            if st.button(label, use_container_width=True):
                go_to_step(page_key)
                st.rerun()
        
        st.divider()
        
        if st.session_state.student_name:
            st.info(f"👤 {st.session_state.student_name}")
        
        st.markdown("""
        ### 💡 Tips
        - Download data anytime
        - Share your findings
        - Ask questions!
        """)
    
    # Route pages
    pages = {
        "welcome": page_welcome,
        "quick_start": page_quick_start,
        "data_explorer": page_data_explorer,
        "learning_lessons": page_learning_lessons,
        "export_analysis": page_export_analysis,
        "completion": page_completion,
    }
    
    current_page = pages.get(st.session_state.wizard_step, page_welcome)
    current_page()


if __name__ == "__main__":
    main()
