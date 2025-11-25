# 🎓 Winter School 2025: Economic & Social Crises in Palestine and Morocco

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io)

**📖 Read in other languages | اقرأ بلغات أخرى | Lire dans d'autres langues:**

- 🇬🇧 English (this page)
- 🇵🇸 [العربية - Arabic](QUICKSTART_ar.md)
- 🇫🇷 [Français - French](QUICKSTART_fr.md)
- 🌍 [Full Multilingual Version](README_MULTILINGUAL.md)

---

An interactive Streamlit dashboard for exploring economic and social crisis indicators in Palestine and Morocco. Built for educational purposes as part of the Winter School 2025 curriculum.

## 📊 Overview

This unified dashboard provides students with hands-on experience analyzing real-world crisis indicators through interactive visualizations. The project consolidates multiple economic and social datasets into a single, easy-to-use interface.

## 🎯 Learning Objectives

- Understand key economic crisis indicators (GDP, unemployment, inflation)
- Analyze youth unemployment trends and regional variations
- Explore education-labor market mismatches
- Examine agricultural stress and food security issues
- Study mobility restrictions and checkpoint impacts
- Investigate micro-enterprise vulnerability
- Analyze household budget shocks and resilience

## 🚀 Quick Start

### Installation

1. **Clone or download this repository**

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser** to the URL shown in the terminal (typically `http://localhost:8501`)

## 📱 Dashboard Pages

The dashboard includes 8 interactive pages accessible via the sidebar:

### 1. 📊 Macro Indicators
**Focus:** Palestine & Morocco
**Indicators:** GDP growth, unemployment rate, youth unemployment, inflation rate
**Time Period:** 2015-2022
**Features:**
- Country comparison (Palestine vs Morocco)
- Interactive indicator selection
- Time series visualization with trends
- Data table with full metrics

### 2. 👥 Youth Unemployment (Morocco)
**Focus:** Morocco
**Indicators:** National, urban, and rural youth unemployment rates
**Time Period:** 2015-2024
**Features:**
- Bilingual interface (Arabic/English)
- Trend analysis across geographic areas
- Comparative visualizations (urban vs rural)
- Peak unemployment identification
- Educational discussion prompts

### 3. 🎓 Education-Labor Mismatch (Palestine)
**Focus:** Palestine
**Analysis:** Unemployment by field of study
**Features:**
- Historical unemployment rates by academic field
- Interactive scenario builder with sliders
- Graduate supply vs job demand projections
- Future unemployment pressure forecasts
- Policy recommendation prompts

### 4. 🌾 Agricultural Stress (Morocco)
**Focus:** Morocco
**Indicators:** Cereal yield, rainfall index, food price index
**Time Period:** 2018-2023
**Features:**
- Bilingual interface (Arabic/English)
- Agricultural productivity trends
- Climate impact analysis (rainfall correlation)
- Food price tracking
- Climate vulnerability discussion

### 5. 🚧 Checkpoint Monitor (Jerusalem)
**Focus:** East Jerusalem
**Indicators:** Wait times at checkpoints
**Features:**
- Bilingual interface (Arabic/English)
- Wait time patterns by day of week
- Hourly trend analysis
- Heatmap visualization
- Economic impact discussion
- Peak congestion identification

### 6. 🏪 Micro-Enterprises (Jerusalem)
**Focus:** East Jerusalem
**Indicators:** Business vulnerability, income, rent burden, risk scores
**Features:**
- Bilingual interface (Arabic/English)
- Risk score distribution analysis
- Income vs rent burden scatter plots
- Sector-based vulnerability analysis
- Neighborhood comparison
- Digital access scoring

### 7. 💰 Household Budgets (Palestine)
**Focus:** Palestine (West Bank & Jerusalem)
**Analysis:** Budget shock scenarios
**Features:**
- Interactive regional filters
- Shock scenario comparison (fuel price +20%, food price +30%, mixed)
- Expenditure share breakdown (food/energy/transport)
- Regional impact analysis
- Household size vs deficit correlation
- Vulnerable population identification

### 8. 🔍 Data Explorer
**Type:** Generic CSV visualization tool
**Features:**
- Auto-detection of all datasets in the project
- Three analysis tabs: Overview, Plot, Data Table
- Multiple chart types (line, bar, scatter)
- Text filtering across categorical columns
- CSV export functionality
- Preset configurations for known datasets

## 📁 Project Structure

```
winter-school-econ-social-crises/
├── app.py                          # Main entry point
├── requirements.txt                # Python dependencies
├── README.md                       # This file
│
├── pages/                          # Dashboard modules
│   ├── __init__.py
│   ├── macro_indicators.py
│   ├── youth_unemployment.py
│   ├── education_labor_mismatch.py
│   ├── agricultural_stress.py
│   ├── checkpoint_monitor.py
│   ├── micro_enterprises.py
│   ├── household_budgets.py
│   └── data_explorer.py
│
├── data/                           # All datasets
│   ├── macro/
│   │   └── econ_indicators.csv
│   ├── morocco/
│   │   ├── youth_unemployment.csv
│   │   ├── agri_stress.csv
│   │   └── food_price_index_monthly.csv
│   ├── palestine/
│   │   ├── unemployment_by_field.csv
│   │   ├── youth_education_employment.csv
│   │   └── household_budget_shocks.csv
│   └── jerusalem/
│       ├── checkpoint_wait_times.csv
│       ├── micro_enterprises.csv
│       └── neighborhood_vulnerability.csv
│
└── utils/                          # Shared utilities (optional)
    └── __init__.py
```

## 📊 Datasets

### Economic Indicators (Macro)
- **File:** `data/macro/econ_indicators.csv`
- **Countries:** Palestine, Morocco
- **Years:** 2015-2022
- **Indicators:** GDP growth (%), unemployment rate (%), youth unemployment (%), inflation rate (%)
- **Source:** Synthetic data for educational purposes

### Morocco Datasets
1. **Youth Unemployment** (`data/morocco/youth_unemployment.csv`)
   - National, urban, and rural rates (2015-2024)

2. **Agricultural Stress** (`data/morocco/agri_stress.csv`)
   - Cereal yield, rainfall index, food prices (2018-2023)

3. **Food Price Index** (`data/morocco/food_price_index_monthly.csv`)
   - Monthly food prices by region (3 years, 3 regions)

### Palestine Datasets
1. **Unemployment by Field** (`data/palestine/unemployment_by_field.csv`)
   - Field-specific unemployment, graduate supply, job demand indices

2. **Youth Education-Employment** (`data/palestine/youth_education_employment.csv`)
   - Demographics, education levels, employment status

3. **Household Budget Shocks** (`data/palestine/household_budget_shocks.csv`)
   - Expenditure shares, shock scenarios, simulated deficits

### Jerusalem Datasets
1. **Checkpoint Wait Times** (`data/jerusalem/checkpoint_wait_times.csv`)
   - Wait times by day of week and hour

2. **Micro-Enterprises** (`data/jerusalem/micro_enterprises.csv`)
   - Income, rent, tax burden, digital access, risk scores

3. **Neighborhood Vulnerability** (`data/jerusalem/neighborhood_vulnerability.csv`)
   - Unemployment, income, rent burden, eviction risk by neighborhood

## 🎓 Pedagogical Approach

This dashboard is designed to be:

1. **Interactive:** Students can filter, explore, and manipulate data to discover patterns
2. **Multilingual:** Key interfaces support both Arabic and English
3. **Scenario-Based:** Includes projection tools for exploring "what-if" scenarios
4. **Discussion-Oriented:** Each page includes prompts for critical thinking and policy discussion
5. **Modular:** Each page focuses on a specific crisis dimension, making it easy to teach individual topics
6. **Extensible:** Students can add new datasets using the Data Explorer tool

## 🛠️ Technical Details

**Framework:** Streamlit 1.28+
**Data Processing:** Pandas, NumPy
**Visualization:** Matplotlib, Plotly
**Python Version:** 3.8+

## 📚 How to Use in Teaching

### Individual Page Focus
Use individual pages for focused lessons:
- Week 1: Macro Indicators (economic fundamentals)
- Week 2: Youth Unemployment (labor market dynamics)
- Week 3: Education-Labor Mismatch (human capital)
- Week 4: Agricultural & Household Crises (food security and resilience)

### Comparative Analysis
Use multiple pages together:
- Compare Morocco youth unemployment with Palestine education mismatch
- Link agricultural stress to household budget shocks
- Connect checkpoint impacts to micro-enterprise vulnerability

### Student Exercises
1. **Data Explorer:** Students can upload their own CSV files
2. **Scenario Builder:** Adjust parameters in Education-Labor Mismatch page
3. **Cross-Dashboard Analysis:** Find connections between different indicators
4. **Policy Recommendations:** Use insights to develop evidence-based proposals

## 🔧 Customization

### Adding New Datasets
1. Place CSV file in appropriate `data/` subfolder
2. The Data Explorer will auto-detect it
3. (Optional) Create a dedicated page module in `pages/` for custom analysis

### Adding New Pages
1. Create a new `.py` file in `pages/` folder
2. Define a `run()` function with your Streamlit code
3. Import it in `app.py` and add to the `PAGES` dictionary

## 📝 Notes

- **Data Sources:** All data is synthetic or aggregated for educational purposes
- **Bilingual Support:** Arabic/English support is available on selected pages
- **Privacy:** No real personal or sensitive data is included
- **Updates:** Data can be refreshed by replacing CSV files in `data/` folders

## 🤝 Contributing

This is a teaching resource. Students and instructors are encouraged to:
- Add new datasets relevant to economic and social crises
- Create new visualization pages
- Improve existing analyses
- Translate content to additional languages
- Submit improvements via pull requests

## 📧 Support

For questions about using this dashboard in your curriculum:
- Review the code comments in each page module
- Check the Data Explorer for dataset documentation
- Consult the discussion prompts embedded in each dashboard

## 📄 License

This project is intended for educational use in the Winter School 2025 curriculum.

---

**Winter School 2025** | Economic & Social Crises in Palestine and Morocco
*Interactive data visualization for crisis analysis and policy development*
