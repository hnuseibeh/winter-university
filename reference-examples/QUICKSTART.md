# 🚀 Quick Start Guide

## Installation & Running

1. **Navigate to the project directory:**
   ```bash
   cd winter-school-econ-social-crises
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the dashboard:**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser** to: `http://localhost:8501`

## What's Included

### 8 Interactive Dashboard Pages:

1. **📊 Macro Indicators** - GDP, unemployment, inflation (Palestine & Morocco)
2. **👥 Youth Unemployment** - Morocco trends (2015-2024) [Bilingual]
3. **🎓 Education-Labor Mismatch** - Palestine field-specific analysis with scenarios
4. **🌾 Agricultural Stress** - Morocco cereal yields, rainfall, food prices [Bilingual]
5. **🚧 Checkpoint Monitor** - Jerusalem wait time analysis [Bilingual]
6. **🏪 Micro-Enterprises** - Jerusalem business vulnerability [Bilingual]
7. **💰 Household Budgets** - Palestine shock scenarios (fuel/food price increases)
8. **🔍 Data Explorer** - Generic CSV visualization tool

### 10 Datasets Included:

**Macro:**
- Economic indicators (GDP, unemployment, inflation)

**Morocco:**
- Youth unemployment (national/urban/rural)
- Agricultural stress (yield, rainfall, prices)
- Food price index (monthly by region)

**Palestine:**
- Unemployment by field of study
- Youth education-employment data
- Household budget shock scenarios

**Jerusalem:**
- Checkpoint wait times
- Micro-enterprise vulnerability
- Neighborhood vulnerability

## First Steps

1. Start with **📊 Macro Indicators** to see overall economic trends
2. Explore **👥 Youth Unemployment (Morocco)** for detailed regional analysis
3. Try **🎓 Education-Labor Mismatch** to experiment with scenario projections
4. Use **🔍 Data Explorer** to examine any dataset interactively

## For Students

- Each page includes discussion prompts and policy questions
- Bilingual support available on selected pages (Arabic/English)
- Export data for further analysis using the download buttons
- Experiment with filters and scenarios to discover patterns

## Troubleshooting

**Issue:** Module not found errors
**Solution:** Run `pip install -r requirements.txt` again

**Issue:** Data file not found
**Solution:** Ensure you're running `streamlit run app.py` from the project root directory

**Issue:** Port already in use
**Solution:** Use `streamlit run app.py --server.port 8502` to run on a different port

---

**Ready to explore economic and social crises data!** 🎓📊
