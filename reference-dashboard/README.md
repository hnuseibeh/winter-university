# REFERENCE EXAMPLE - Completed Dashboard

## Economic & Social Crises Dashboard

**Palestine & Morocco Crisis Analysis | AI-Driven Data Visualization**

---

## Note to Students

This is a **completed reference example** dashboard provided for your learning and inspiration. You can explore the code, run the application, and see how a finished crisis analysis tool works. This example demonstrates advanced features and comprehensive integration, but **you don't need to build something this complex** for your project. Use it as a reference to understand possibilities, get ideas, and see best practices in action.

**Key Points:**

- This is an example, not a template - your project can be simpler
- Explore the code to understand structure and techniques
- Run it to see what's possible with Streamlit and data visualization
- Focus on your own research question - don't try to replicate this exactly
- Ask questions if you want to understand how specific features work

---

## Overview

This Streamlit dashboard synthesizes academic research on economic and social crises in **Palestine** and **Morocco** into interactive, policy-relevant visualizations. It combines macro-economic indicators, scenario modeling, regional analysis, and research context to help students, policymakers, and researchers understand systemic fragility.

### Key Crises Explored

| Region | Crisis Type | Examples |
|--------|-------------|----------|
| **Palestine** | Structural strangulation | Occupation, residency revocation, checkpoint delays, commercial collapse |
| **Morocco** | Climate vulnerability + inequality | Drought-driven migration, youth unemployment, spatial disparities |

---

## Features

### 📚 Pages

1. **Context & Background**
   - Research synthesis from 5 academic reports
   - Theoretical frameworks (Porter's Diamond, "friction economies," "administrative attrition")
   - Ethical considerations for AI in conflict zones
   - Key narratives (Qalandia checkpoint, Old City souvenir collapse, climate migration)

2. **Macro-Economic Indicators**
   - GDP growth, unemployment, youth unemployment, inflation
   - Multi-country comparison (Palestine, Morocco)
   - Interactive filtering and time-series visualization

3. **Education–Labor Mismatch (Palestine)**
   - Scenario modeling: adjust graduate supply/job demand growth rates
   - Interactive projection to 2035 or beyond
   - Policy lever testing (intake caps, job creation targets)

4. **Youth Unemployment by Region (Morocco)**
   - Break down national averages to urban/rural/regional levels
   - Reveal spatial inequality drivers
   - Contextual analysis of rural-to-urban migration pressure

### 🤖 Methodology

- **Plotly interactive charts** for exploration and drill-down
- **Streamlit sidebar controls** for filtering, scenarios, and settings
- **Data caching** for fast performance
- **Research-grounded narratives** connecting data to lived experience

---

## Quick Start

### 1. Clone or Download

```bash
cd econ_social_crises_dashboard
```

### 2. Install Dependencies

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Prepare Data

Add CSV files to `data/` folder:
- `macro_indicators.csv` – GDP, unemployment, inflation (countries as rows, years as columns or rows)
- `unemployment_by_field.csv` – Education field, year, unemployment_rate, supply_index, demand_index
- `morocco_youth_unemployment.csv` – Year, national/urban/rural unemployment rates
- (Optional) Other regional or sector-specific datasets

**CSV Format Example:**

```
macro_indicators.csv:
country,year,gdp_growth,unemployment_rate,youth_unemployment,inflation_rate
Palestine,2020,2.5,25.3,43.2,1.2
Morocco,2020,−5.7,10.1,27.4,0.6
...

unemployment_by_field.csv:
year,field,unemployment_rate,graduates_supply_index,jobs_demand_index
2015,Engineering,15.2,100.0,105.0
2015,Medicine,8.5,100.0,110.0
...
```

### 4. Run the App

```bash
streamlit run app.py
```

Then open http://localhost:8501 in your browser.

---

## File Structure

```
econ_social_crises_dashboard/
├── app.py                           # Main entry point (sidebar dispatcher)
├── context_data.py                  # Research data extracted from 5 PDFs
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
├── SETUP.md                         # Quick start guide
├── .gitignore                       # GitHub ignore rules
│
├── pages/
│   ├── context_background.py       # Research synthesis & narrative (uses context_data.py)
│   ├── macro_indicators.py         # GDP, unemployment, inflation
│   ├── education_labor_mismatch.py # Scenario modeling
│   └── youth_unemployment_morocco.py # Regional analysis
│
├── utils/
│   └── data_loader.py              # Shared data loading & caching
│
└── data/
    ├── macro_indicators.csv
    ├── unemployment_by_field.csv
    ├── morocco_youth_unemployment.csv
    └── [additional datasets]
```

### Research Integration

The **`context_data.py`** file contains structured research extracted from 5 academic PDF reports:

- **Palestine Context:** Demographic engineering, checkpoint toll, commercial collapse
- **Morocco Context:** Climate vulnerability, spatial inequality, youth unemployment
- **AI Methodologies:** Satellite remote sensing, NLP, mobility data, scenario modeling
- **Ethical Frameworks:** Data sovereignty, privacy preservation, participatory design
- **Research Narratives:** Qalandia checkpoint, Old City souvenir collapse, climate-driven migration

This data is automatically imported by the **Context & Background page** to populate all research sections and narratives. See `pages/context_background.py` for integration.

---

## Data Sources

- **Palestinian Central Bureau of Statistics (PCBS)** – Labor, demographics, GDP
- **World Bank** – Morocco economic indicators, development metrics
- **FAO (Food & Agriculture Org)** – Agricultural yields, climate-vulnerability indices
- **Research Reports** – Academic synthesis on East Jerusalem, Gaza, regional crises
- **Extracted from:** 5 peer-reviewed research documents (see `archive/` for PDFs)

---

## Scenario Modeling: How to Use

### Education–Labor Mismatch

1. **Select a field of study** (Engineering, Medicine, Law, etc.)
2. **Adjust sliders:**
   - Graduate supply growth (% per year): How many new graduates enter the field?
   - Job demand growth (% per year): How many new jobs are created?
   - Projection horizon: How many years ahead to forecast?
3. **Observe results:**
   - Historical unemployment trend
   - Projected supply vs. demand gap
   - Unemployment pressure proxy (%)
4. **Ask policy questions:**
   - Should we cap intake in oversaturated fields?
   - Where can we create high-wage jobs?
   - Which regions need targeted skills training?

---

## Ethical Framework for AI in Crisis Zones

⚠️ **Key Considerations:**

- **Data Sovereignty:** Communities control their own data; algorithms transparent to stakeholders
- **Surveillance vs. Monitoring:** Distinguish between surveillance (control) and monitoring (awareness)
- **Dual-Use Risk:** Same algorithms can predict humanitarian crises OR enable military targeting
- **Participatory Design:** Communities should help define what "crisis" means and what interventions matter
- **Accountability:** Who benefits from predictions? Who bears costs?

See **Context & Background** page for full framework.

---

## How This Project Reflects Research Findings

| Research Finding | How It's Shown |
|------------------|----------------|
| Palestinian economy controlled externally → macro indicators show distortions | **Macro-Economic Indicators** page |
| Education-labor mismatch drives youth unemployment | **Education–Labor Mismatch** page with scenarios |
| Morocco's rain-fed GDP creates rural volatility | **Youth Unemployment Morocco** page (rural-urban gap) |
| Spatial inequality masked by national averages | Regional breakdown in **Youth Unemployment** |
| Qalandia checkpoint imposes psychological toll | Context page narrative + sarcasm scoring |
| East Jerusalem commercial collapse via "admin attrition" | Context page narrative + data on tax enforcement |

---

## Extending the Dashboard

### Add a New Page

1. Create `pages/new_page.py`:
   ```python
   import streamlit as st
   from utils.data_loader import load_data
   
   def run():
       st.title("Your Page Title")
       df = load_data("your_data.csv")
       # Your visualization code here
   ```

2. Import in `app.py`:
   ```python
   from pages import context_background, macro_indicators, new_page
   pages = {
       ...
       "📊 Your Page": new_page,
   }
   ```

3. Add data file to `data/` folder

4. Restart `streamlit run app.py`

### Add a New Dataset

- Drop CSV into `data/` folder
- Call `load_data("filename.csv")` in any page
- Data is automatically cached for performance

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "Data file not found" error | Check CSV is in `data/` folder with correct filename |
| Charts not showing | Check CSV has required columns (year, country, indicator names) |
| Slow startup | Streamlit is caching data; second load will be faster |
| Import errors | Run `pip install -r requirements.txt` in activated venv |

---

## For Instructors

### Teaching Use Cases

1. **Econ Fundamentals:** Use macro indicators to discuss GDP, unemployment, inflation dynamics
2. **Policy Analysis:** Use education–labor mismatch scenario builder to debate education policy
3. **Crisis Research:** Use context page to understand occupation, inequality, and systemic fragility
4. **Data Literacy:** Have students modify visualizations, add datasets, pose questions

### Suggested Assignments

- **Dashboard Explorer:** Students choose 1 indicator, explain 3 patterns they see
- **Scenario Tester:** Use education mismatch builder to design a policy intervention; predict outcomes
- **Research Synthesis:** Students read one PDF research report, summarize in 2–3 bullets
- **Data Storytelling:** Pick 1 dataset, create a "human story" that explains the numbers

---

## Limitations & Caveats

- **Simulated/Estimated Data:** Some datasets are simplified or synthetic for teaching purposes
- **Temporal Lag:** Official statistics often lag by 12–24 months
- **Gaza Crisis (2024+):** Most data pre-dates major recent escalations; baseline assumptions may be outdated
- **Occupied Territory:** Standard economic models may not apply; political factors dominate
- **Confidentiality:** No individual-level data; all aggregated for privacy

---

## Contributing

This is an open-source teaching project. Contributions welcome:

- Bug fixes & improvements to code
- Additional datasets (with proper attribution)
- Improved visualizations
- Translations (Arabic, French, English currently supported via documentation)

---

## License

[Specify license—e.g., MIT, CC-BY-4.0, GPL-3.0]

---

## Contact & Support

- **Questions?** Contact the Winter University 2025 – AI & Crisis Lab team
- **Data Issues?** File an issue with dataset filename and error message
- **Feature Requests?** Describe the new analysis or data you'd like to see

---

## References

**Key Research Documents (See `archive/` folder for full PDFs):**

1. *A City Under Pressure: Socio-Economic Conditions in East Jerusalem, 2010–2025*
2. *Algorithmic Foresight: AI-Driven Crisis Prediction in Fragile Contexts*
3. *An Integrated Analysis of Socio-Political Crises through Simulated Proxy Datasets*
4. *East Jerusalem Economic Analysis and Strategies*
5. *The Anatomy of Dispossession: Economic and Social Crises in East Jerusalem*

---

**Last Updated:** November 24, 2025  
**Version:** 1.0 (Beta)  
**Project Status:** Active development for teaching & research
