# Quick Setup Guide

## One-Time Setup (5 minutes)

### 1. Open Terminal in This Folder

```bash
cd econ_social_crises_dashboard
```

### 2. Create Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

(On Windows: `.venv\Scripts\activate`)

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
streamlit run app.py
```

A browser window should open at `http://localhost:8501`

---

## Using the Dashboard

### First Time?

1. Click **"📚 Context & Background"** to understand the research foundations
2. Read the tabs: Palestine, Morocco, AI Methods, Research Stories
3. Then explore the other pages (Macro Indicators, Education–Labor Mismatch, etc.)

### Exploring Scenarios

**Education–Labor Mismatch page:**
- Select a field of study (Engineering, Medicine, Law)
- Adjust the sliders on the left:
  - Graduate supply growth (%)
  - Job demand growth (%)
  - Projection horizon (years)
- Observe how the projections change
- **Question:** What policy changes would reduce unemployment?

### Modifying Data

Add or edit CSV files in `data/` folder:

```
data/
├── macro_indicators.csv
├── unemployment_by_field.csv
├── morocco_youth_unemployment.csv
└── [add new files here]
```

Changes take effect on next page refresh.

---

## Troubleshooting

**"Module not found" error?**
- Make sure you ran `pip install -r requirements.txt`
- Check that you're in the `.venv` (you should see `(.venv)` in your terminal)

**"Data file not found"?**
- Ensure CSV files are in `data/` folder
- Check spelling matches exactly (case-sensitive on Mac/Linux)

**App too slow?**
- First load builds cache; subsequent loads are faster
- Close other browser tabs to free memory

**Want to reset?**
```bash
deactivate
rm -rf .venv
# Then repeat steps 2-4 above
```

---

## Next Steps

1. **Explore all pages** – get familiar with the dashboards
2. **Modify one dataset** – edit a CSV value and see visualization update
3. **Add your own data** – create a new CSV and add a page to visualize it
4. **Ask research questions** – what patterns do you see? What would you test?

---

## For Instructors

### Customization Options

**Easy (5 min):**
- Update CSV data files
- Customize page titles/descriptions (edit `pages/*.py`)

**Medium (15 min):**
- Add a new page (copy template from `macro_indicators.py`)
- Add new sidebar menu item (edit `app.py`)

**Advanced (30+ min):**
- Integrate external data API (World Bank, FAO, etc.)
- Add data validation & cleaning
- Create custom AI models (forecasting, clustering)

---

**Need Help?**
- Check the main `README.md` for detailed documentation
- See `archive/WORKSPACE_INVENTORY.md` for research context
- Review research PDFs in `archive/` folder for detailed analysis

---

**Happy exploring! 🚀**
