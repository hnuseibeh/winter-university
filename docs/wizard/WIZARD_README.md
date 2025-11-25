# 🧙 Crisis Dashboard Wizard - Educational Guide

An interactive web-based wizard to help students learn about and explore data on Palestinian and Moroccan economic and humanitarian crises.

## Overview

The Crisis Dashboard Wizard is a guided educational tool that walks students through:

- **Understanding Crisis Data** — Key indicators and what they mean
- **Exploring Real Datasets** — Interactive browsing of humanitarian, climate, and economic data
- **Learning Historical Context** — Background on Palestinian and Moroccan crises
- **Analyzing Patterns** — Finding insights in the data
- **Creating Reports** — Exporting findings for research projects

## Features

### 🏠 **Home & Onboarding**
- Welcome screen with learning path selection
- Student name tracking (optional)
- Multiple learning modes:
  - **Quick Start** (5 min) — Fast overview
  - **Full Tutorial** (20 min) — Comprehensive guide
  - **Focused Study** — Pick specific topics
  - **Data Explorer** — Open-ended exploration

### 📊 **Interactive Data Explorer**
- Browse all 6 datasets interactively
- Preview data tables with filtering
- Download CSVs for each dataset
- Column information and data summaries
- Quick visualizations with Plotly

### 📖 **Educational Content**
Three detailed sections covering:

1. **🇵🇸 Palestinian Crisis**
   - Humanitarian indicators (deaths, displacement, damage)
   - Economic collapse (GDP, employment, trade)
   - Movement restrictions and checkpoints
   - Demographic impact on youth

2. **🇲🇦 Moroccan Crisis**
   - Climate vulnerability and projections
   - Agricultural stress and regional impacts
   - Youth unemployment patterns
   - Urban-rural development gaps

3. **💡 Data Analysis Tips**
   - Questions to ask about data
   - Data quality considerations
   - Research methodology
   - Recommended sources

### 📤 **Data Export & Analysis**
- Download any dataset as CSV
- Create custom analysis reports
- Template for research questions, findings, sources
- Export reports as Markdown documents

### 🎓 **Completion & Resources**
- Completion certificate screen
- Links to official data sources
- Documentation and guides
- Next steps for continued learning

## Installation & Setup

### Prerequisites
- Python 3.8+
- Streamlit
- Pandas
- Plotly

### Installation

```bash
# Install dependencies
pip install streamlit pandas plotly

# Navigate to project directory
cd /Users/musicinst/Desktop/winter

# Run the wizard
streamlit run wizard.py
```

### Access

The wizard will be available at: `http://localhost:8501`

## File Structure

```
winter/
├── wizard.py                           # Main wizard application
├── reference-dashboard/
│   ├── data/                          # CSV datasets (6 files)
│   │   ├── humanitarian_indicators.csv
│   │   ├── climate_vulnerability_index.csv
│   │   ├── agricultural_stress.csv
│   │   ├── crisis_timeline.csv
│   │   ├── sentiment_index.csv
│   │   └── news_summary.csv
│   ├── app.py                         # Main dashboard (for reference)
│   └── pages/                         # Dashboard pages
└── WIZARD_README.md                   # This file
```

## Usage Guide

### For Students

1. **Start the Wizard**
   ```bash
   streamlit run wizard.py
   ```

2. **Choose a Learning Path**
   - Select based on time available and learning goals
   - Quick Start for overview, Full Tutorial for depth

3. **Explore Data**
   - Use Data Explorer to browse datasets
   - Download data you want to analyze
   - Check column types and summaries

4. **Learn Context**
   - Read about Palestinian crisis (humanitarian, economic)
   - Understand Moroccan challenges (climate, agriculture, youth)
   - Learn analysis tips and best practices

5. **Create Report**
   - Define your research question
   - Select relevant datasets
   - Document findings
   - Export as Markdown for class submission

### For Instructors

**Customization Options:**

1. **Add More Datasets**
   - Place new CSV files in `reference-dashboard/data/`
   - They'll automatically appear in explorer

2. **Modify Educational Content**
   - Edit `page_learning_lessons()` function
   - Update context sections
   - Add more analysis tips

3. **Adjust Learning Paths**
   - Modify step structure in `page_welcome()`
   - Create new custom paths
   - Add assessment questions

4. **Theme & Branding**
   - Customize CSS in style section
   - Change colors, fonts, layout
   - Add institutional branding

## Datasets Included

| Dataset | Rows | Key Metrics | Source |
|---------|------|-------------|--------|
| humanitarian_indicators.csv | 2 | IDPs, poverty, food insecurity | PCBS, UN OCHA |
| climate_vulnerability_index.csv | 2 | Temperature, precipitation, drought | IPCC, UN Climate |
| agricultural_stress.csv | 4 | Drought intensity, crop yields | FAO, HCP |
| crisis_timeline.csv | 4 | Event date, impact, population affected | News, humanitarian orgs |
| sentiment_index.csv | 2 | Crisis score (0-10), stability index | Analysis data |
| news_summary.csv | 4 | Topics, sentiment, mention frequency | News aggregation |

## Key Concepts Covered

### Palestinian Crisis Indicators
- **Humanitarian:** Deaths, injuries, displacement, detained persons
- **Economic:** GDP contraction, unemployment, trade disruption
- **Structural:** 600+ checkpoints, movement restrictions, economic isolation
- **Demographic:** 44% youth population, educational disruption

### Moroccan Crisis Indicators
- **Climate:** +1.5°C temp increase, -12% precipitation by 2050
- **Agricultural:** Regional drought (Draa-Tafilalet, Guelmim-Oued Noun)
- **Employment:** 12-15% youth unemployment, skills mismatch
- **Regional:** Urban-rural disparity, southward climate impact

## Data Analysis Framework

Students learn to ask:

1. **Temporal Questions**
   - Is the situation improving or worsening?
   - Are there seasonal patterns?
   - What changed year-over-year?

2. **Spatial Questions**
   - How do regions compare?
   - Which areas are most affected?
   - Urban vs rural differences?

3. **Causal Questions**
   - What caused this crisis?
   - How are indicators connected?
   - What are feedback loops?

4. **Predictive Questions**
   - What if trends continue?
   - What interventions could help?
   - How would we measure success?

## Examples & Use Cases

### Class Session: "Understanding Humanitarian Data"
1. Have students work through Quick Start (5 min)
2. Discuss key humanitarian indicators in class
3. Students create custom analyses
4. Share findings and debate interpretations

### Research Project: "Climate Change & Agriculture"
1. Guide students to Morocco section
2. Show climate + agricultural stress datasets
3. Have students analyze connections
4. Export findings for papers

### Comparative Analysis: "Palestinian vs Moroccan Crises"
1. Quick start for overview
2. Learn both country sections
3. Use data explorer to compare
4. Create comparative report

## Troubleshooting

### Datasets not loading?
- Check `reference-dashboard/data/` directory exists
- Verify CSV files are present
- Check file permissions

### Visualizations not rendering?
- Ensure Plotly is installed: `pip install plotly`
- Check internet connection (Plotly loads some libraries online)
- Refresh page in browser

### Slow performance?
- Clear Streamlit cache: `streamlit cache clear`
- Run on faster internet connection
- Use Quick Start instead of Full Tutorial

## Customization Examples

### Add a New Learning Path

```python
def page_custom_topic():
    """Custom topic for specific learning objective."""
    st.header("My Custom Topic")
    st.write("Content here...")
    
    # Add to page_welcome() selector
    if st.button("🎯 My Topic"):
        st.session_state.learning_path = "custom"
        go_to_step("custom_topic")
        st.rerun()
```

### Add Analysis Questions

Edit `page_learning_lessons()` to add more questions:

```python
st.markdown("""
### New Analysis Question
- Why might agricultural stress and youth unemployment be connected?
- What historical events shaped these indicators?
""")
```

### Connect to Main Dashboard

Add button in `page_completion()`:

```python
if st.button("📊 Open Full Dashboard"):
    # Opens reference-dashboard/app.py
    st.write("[Click here to view full dashboard](./app.py)")
```

## Learning Outcomes

By completing this wizard, students will be able to:

✅ **Understand** what crisis indicators mean and how they're measured  
✅ **Analyze** real datasets to identify patterns and trends  
✅ **Evaluate** data quality and consider bias/limitations  
✅ **Compare** different regions and time periods  
✅ **Create** research reports using data evidence  
✅ **Communicate** findings to diverse audiences  
✅ **Synthesize** connections between different types of data  

## Assessment Ideas

### For Instructors

1. **Guided Report**
   - Assign specific research question
   - Students use wizard to explore data
   - Submit findings via wizard export

2. **Comparative Analysis**
   - Compare Palestine vs Morocco crises
   - Identify similar/different indicators
   - Propose policy solutions based on data

3. **Trend Analysis**
   - How have indicators changed 2023-2025?
   - What explains the changes?
   - What do projections suggest?

4. **Data Quality Audit**
   - Evaluate data source credibility
   - Identify gaps or limitations
   - Propose additional metrics needed

## Future Enhancements

Potential improvements for v2.0:

- [ ] Time-series analysis with trend lines
- [ ] Regional heatmaps for geographic analysis
- [ ] Correlation analysis between datasets
- [ ] Scenario modeling (what-if analysis)
- [ ] Assessment quiz at end of wizard
- [ ] Student portfolio / saved analyses
- [ ] Real-time data integration
- [ ] Multi-language support
- [ ] Mobile-optimized interface
- [ ] Collaborative project features

## Resources

### Data Sources
- **PCBS:** https://pcbs.gov.ps/
- **HCP Morocco:** https://www.hcp.ma/
- **World Bank:** https://data.worldbank.org/
- **UN OCHA:** https://www.unocha.org/
- **FAO:** http://www.fao.org/

### Educational Resources
- [World Bank Education Materials](https://data.worldbank.org/products/data-books)
- [UN Sustainable Development Goals](https://sdgs.un.org/)
- [Climate TRACE Project](https://climatetrace.org/)

### Technical Docs
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Plotly Python Docs](https://plotly.com/python/)
- [Pandas Documentation](https://pandas.pydata.org/)

## Support

For questions or issues:

1. Check this README first
2. Review inline code comments in `wizard.py`
3. Consult Streamlit/Plotly documentation
4. Contact instructor or teaching assistant

## License

Educational use. Proper attribution to data sources required.

---

**Status:** ✅ Production Ready  
**Last Updated:** November 2025  
**Version:** 1.0

