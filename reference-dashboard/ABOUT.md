# About This Reference Dashboard

## What Is This?

This is a **completed example dashboard** that demonstrates what a finished crisis analysis tool can look like. It was created as a reference for students in the Winter University 2025 AI & Crisis Lab workshop.

## Purpose

**For Inspiration, Not Replication**

This dashboard is meant to:

- Show you what's possible with Streamlit and Python data visualization
- Demonstrate how to structure a multi-page dashboard application
- Illustrate integration of research data with interactive visualizations
- Provide working code examples you can learn from

**Important:** You don't need to build something this complex! Your project can be much simpler and still be excellent. Focus on your research question and start small.

## What It Demonstrates

This dashboard showcases:

1. **Multi-page Streamlit application** - Navigation between different analysis pages
2. **Interactive visualizations** - Using Plotly for dynamic, explorable charts
3. **Scenario modeling** - Interactive sliders to project future trends
4. **Research integration** - Connecting academic research to data visualization
5. **Data management** - Loading, caching, and processing CSV datasets
6. **Regional analysis** - Breaking down national statistics to reveal spatial inequalities

## Quick Start - Try It Out

Want to see it in action? Here's how to run it:

### 1. Open Terminal and Navigate to This Directory

```bash
cd /Users/musicinst/Desktop/winter/reference-dashboard
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Dashboard

```bash
streamlit run app.py
```

### 5. Explore in Your Browser

Open http://localhost:8501 and explore the different pages:

- Context & Background - See how research is presented
- Macro-Economic Indicators - Interactive time-series charts
- Education-Labor Mismatch - Scenario modeling with sliders
- Youth Unemployment Morocco - Regional breakdown analysis

## What To Learn From This

### For Your Own Project

**Don't try to copy this.** Instead, explore it to understand:

- How pages are organized in the `pages/` folder
- How data is loaded in `utils/data_loader.py`
- How charts are created with Plotly
- How the sidebar navigation works in `app.py`
- How research context is structured in `context_data.py`

### Start Simple

For your workshop project, consider starting with:

1. **One page** - Just a single analysis or visualization
2. **One dataset** - A simple CSV file with your data
3. **One chart** - A basic line chart, bar chart, or scatter plot
4. **One insight** - What story does your data tell?

You can always add more features later.

## Questions?

If you see something in this dashboard and wonder "how does that work?", ask your instructor or explore the code. Every feature here started as a simple idea that was built step by step.

## File Structure Overview

```
reference-dashboard/
├── app.py                    # Main entry point - starts here
├── context_data.py           # Research data structure
├── requirements.txt          # Python packages needed
├── pages/                    # Each analysis page
│   ├── context_background.py
│   ├── macro_indicators.py
│   ├── education_labor_mismatch.py
│   └── youth_unemployment_morocco.py
├── utils/                    # Helper functions
│   └── data_loader.py
└── data/                     # CSV datasets
    ├── macro_indicators.csv
    ├── unemployment_by_field.csv
    └── morocco_youth_unemployment.csv
```

## Remember

This dashboard represents one approach to crisis data visualization. Your project might look completely different - and that's great! Use this as inspiration, not as a template to copy. Focus on telling your story with your data in your way.

---

**Good luck with your project!**
