# Winter University 2025 – Workspace Inventory

## Overview
This workspace contains **8 project folders** focused on **Economic & Social Crises in Palestine and Morocco**, with Streamlit dashboards, data analysis tools, and teaching materials. There are multiple iterations and variants of similar projects.

---

## 1. `ai-crisis-workshop/`

### Purpose
**Original AI Crisis Prediction Workshop** – Multi-dataset foundation for crisis prediction and governance.

### Key Focus
Five simulated datasets exploring crisis prediction challenges with focus on AI governance.

### Structure
```
ai-crisis-workshop/
├── data/
│   ├── qalandia_checkpoint_monitor.csv          (Wait times + sarcasm scores)
│   ├── ej_micro_enterprise_vulnerability.csv    (Shop cluster risk assessment)
│   ├── palestine_demographic_projections.csv    (Population & labor forecasts)
│   ├── gaza_humanitarian_ratios.csv             (Food insecurity, malnutrition)
│   └── regional_social_volatility.csv           (NLP sentiment + compliance)
├── src/
│   └── app.py                                   (Main 5-dataset dashboard)
├── generate_data.py                             (Simulated data generator)
└── README.md
```

### Streamlit App
**File:** `src/app.py`  
**Pages:** 5 datasets (checkbox-driven routing)
- Qalandia checkpoint temporal monitoring
- East Jerusalem micro-enterprise vulnerability
- Palestine demographic projections
- Gaza humanitarian crisis ratios
- Regional social volatility & AI governance

### Data Scope
- ✅ **Broad crisis scope** (governance, humanitarian, social volatility)
- ✅ **5 distinct analytical challenges**
- ❌ **Not focused on econ/social only** (includes governance & humanitarian)

### Target Audience
Research/workshop participants; broad multidisciplinary coverage.

---

## 2. `winter-university-2025-ai-crisis-lab-expanded 2/`

### Purpose
**Comprehensive 10-Project Lab** – Expanded mini-project collection for diverse crisis topics.

### Key Focus
10 independent mini-projects, each with own Streamlit app and data.

### Structure
```
winter-university-2025-ai-crisis-lab-expanded 2/
├── streamlit_main.py                      (Central router/dispatcher)
├── common/
│   ├── __init__.py
│   └── data_loader.py                     (Shared data utilities)
├── projects/
│   ├── p01_cybersecurity_ai/
│   │   └── app.py
│   ├── p02_digital_narratives/
│   │   └── app.py
│   ├── p03_econ_social_crises/            ⭐ (Economic indicators: GDP, unemployment, etc.)
│   │   └── app.py
│   ├── p04_cultural_heritage_ai/
│   │   └── app.py
│   ├── p05_psychosocial_stress_monitor/
│   │   └── app.py
│   ├── p06_education_labor_mismatch/      ⭐ (Education–labor scenario modeling)
│   │   └── app.py
│   ├── p07_gaza_infra_collapse_monitor/
│   │   └── app.py
│   ├── p08_morocco_flood_risk_tracker/
│   │   └── app.py
│   ├── p09_morocco_poverty_mapper/
│   │   └── app.py
│   └── p10_data_governance_auditor/
│       └── app.py
├── data/
│   ├── econ/
│   ├── governance/
│   ├── heritage/
│   ├── morocco/
│   ├── palestine/
│   └── remote_sensing/
├── requirements.txt
└── README.md
```

### Streamlit App
**File:** `streamlit_main.py`  
**Type:** Central dispatcher with sidebar project selector  
**Key Econ/Social Projects:**
- `p03_econ_social_crises/app.py`: Macro indicators (GDP, unemployment, youth unemployment, inflation)
- `p06_education_labor_mismatch/app.py`: Supply–demand scenario modeling with projection sliders

### Data Scope
- ✅ **Very broad** (10 different crisis angles)
- ✅ **Includes econ/social modules** (`p03`, `p06`)
- ✅ **Sophisticated scenario modeling** (education–labor mismatch with growth rates)
- ❌ **Mixed with governance, heritage, infrastructure, etc.**

### Target Audience
Teaching lab; researchers exploring multiple crisis dimensions.

### Quality Notes
- **p03** (`econ_social_crises`): Clean, focused macro dashboard using Plotly.
- **p06** (`education_labor_mismatch`): Advanced scenario builder with supply/demand projections.

---

## 3. `workshop3-dashboard/`

### Purpose
**Simple 4-Module Teaching Dashboard** – Introductory Streamlit template for Palestine/Morocco crises.

### Key Focus
Ready-made multi-module dashboard for student workshop (basic level).

### Structure
```
workshop3-dashboard/
├── app/
│   ├── streamlit_main.py                  (Module dispatcher)
│   └── modules/
│       ├── module_1_checkpoint_time.py    (Jerusalem checkpoint wait times)
│       ├── module_2_micro_enterprise.py   (Jerusalem micro-enterprise risk)
│       ├── module_3_youth_unemployment_ma.py  (Morocco youth unemployment)
│       └── module_4_agri_stress_ma.py     (Morocco agricultural stress/NDVI)
├── data/
│   ├── jerusalem_checkpoint_wait_times.csv
│   ├── jerusalem_micro_enterprises.csv
│   ├── morocco_youth_unemployment.csv
│   └── morocco_agri_stress.csv
├── notebooks/
│   └── notebook_template.ipynb
├── video_prompt.txt
├── requirements.txt
└── README.md
```

### Streamlit App
**File:** `app/streamlit_main.py`  
**Pages:** 4 modules (radio selector)
- Checkpoint wait times (line chart, anomaly detection)
- Micro-enterprise risk distribution (histogram)
- Youth unemployment trends (line chart, regional comparison)
- Agricultural stress (NDVI by region)

### Data Scope
- ✅ **Focused on Jerusalem & Morocco**
- ✅ **Economic & social focus** (micro-business, unemployment, agriculture)
- ❌ **Very simple/introductory** (basic matplotlib charts)

### Target Audience
Beginner students; hands-on workshop introduction.

### Quality Notes
- Uses matplotlib (simple, but not interactive).
- Module-based architecture is clean (each has `app()` function).

---

## 4. `workshop3-jerusalem-morocco-dashboard/`

### Purpose
**Real Data Variant** – First iteration with emphasis on real-world data sources.

### Key Focus
Same 4-module structure as `workshop3-dashboard/` but with real data for Morocco indicators.

### Structure
```
workshop3-jerusalem-morocco-dashboard/
├── app/
│   ├── streamlit_main.py
│   └── modules/
│       ├── module_1_checkpoint_time.py
│       ├── module_2_micro_enterprise.py
│       ├── module_3_youth_unemployment_ma.py  (Real: World Bank / FRED)
│       └── module_4_agri_stress_ma.py         (Real: FAO-based)
├── data/
│   ├── jerusalem_checkpoint_wait_times.csv
│   ├── jerusalem_micro_enterprises.csv
│   ├── morocco_youth_unemployment.csv
│   └── morocco_agri_stress.csv
├── notebooks/
│   └── notebook_template.ipynb
├── CHALLENGES.md
├── requirements.txt
└── README.md
```

### Distinction
- **Real data for Morocco** (youth unemployment, cereal yield).
- **Educational placeholders for Jerusalem** (can be updated later).

### Data Scope
- ✅ **Mix of real + educational data**
- ✅ **Economic & social focus**

### Target Audience
Workshop students; moderate complexity.

---

## 5. `workshop3-jerusalem-morocco-dashboard 2/`

### Purpose
**All-in-One Teaching Kit** – Comprehensive version with plug-and-play CSV explorer.

### Key Focus
Main dashboard + generic CSV explorer + expanded datasets + challenges document.

### Structure
```
workshop3-jerusalem-morocco-dashboard 2/
├── app/
│   ├── streamlit_main.py                  (Main 4-module dashboard)
│   ├── plug_and_play_dashboard.py         (Generic CSV explorer/visualizer)
│   └── modules/
│       ├── module_1_checkpoint_time.py
│       ├── module_2_micro_enterprise.py
│       ├── module_3_youth_unemployment_ma.py  (Real: national/urban/rural breakdown)
│       └── module_4_agri_stress_ma.py
├── data/
│   ├── jerusalem_checkpoint_wait_times.csv
│   ├── jerusalem_micro_enterprises.csv
│   ├── morocco_youth_unemployment.csv
│   ├── morocco_agri_stress.csv
│   └── [additional extended datasets]
├── notebooks/
│   └── notebook_template.ipynb
├── CHALLENGES.md                          (Group work tasks)
├── DATASETS.md                            (Data dictionary & uses)
├── video_prompt.txt
├── requirements.txt
└── README.md
```

### Streamlit Apps
**Files:**
- `app/streamlit_main.py`: Main 4-module dashboard (same as v1/v3)
- `app/plug_and_play_dashboard.py`: Generic CSV loader + auto-visualizer

### Key Addition
- **`plug_and_play_dashboard.py`**: Allows students to load any CSV from `data/` and auto-generate summary stats + charts.
- **CHALLENGES.md**: Detailed group work instructions.
- **Expanded data**: More Palestine/Morocco datasets included.

### Data Scope
- ✅ **Most comprehensive data set of workshop3 variants**
- ✅ **Includes pedagogical generic tools**

### Target Audience
Full teaching package; workshop facilitators & students.

---

## 6. `workshop3-jerusalem-morocco-dashboard 3/`

### Purpose
**Real Data Variant (Repeat)** – Nearly identical to v1 (variant iteration).

### Key Focus
Same structure and purpose as `workshop3-jerusalem-morocco-dashboard/` (original real data version).

### Structure
```
workshop3-jerusalem-morocco-dashboard 3/
├── app/
│   ├── streamlit_main.py
│   └── modules/
│       ├── module_1_checkpoint_time.py
│       ├── module_2_micro_enterprise.py
│       ├── module_3_youth_unemployment_ma.py
│       └── module_4_agri_stress_ma.py
├── data/
│   ├── jerusalem_checkpoint_wait_times.csv
│   ├── jerusalem_micro_enterprises.csv
│   ├── morocco_youth_unemployment.csv
│   └── morocco_agri_stress.csv
├── notebooks/
│   └── notebook_template.ipynb
├── CHALLENGES.md
├── requirements.txt
└── README.md
```

### Distinction
- **Functionally identical to v1** (appears to be backup or variant iteration).
- No additional features vs. v1.

---

## 7. `workshop3-jerusalem-morocco-dashboard 4/`

### Purpose
**Expanded Teaching Package (Final Version)** – Most complete with extended datasets & documentation.

### Key Focus
Full teaching kit with expanded data, challenges, and comprehensive documentation.

### Structure
```
workshop3-jerusalem-morocco-dashboard 4/
├── app/
│   ├── streamlit_main.py                  (Main 4-module dashboard)
│   └── modules/
│       ├── module_1_checkpoint_time.py
│       ├── module_2_micro_enterprise.py
│       ├── module_3_youth_unemployment_ma.py
│       └── module_4_agri_stress_ma.py
├── data/
│   ├── jerusalem_checkpoint_wait_times.csv
│   ├── jerusalem_micro_enterprises.csv
│   ├── morocco_youth_unemployment.csv
│   ├── morocco_agri_stress.csv
│   └── [additional datasets for expanded use]
├── notebooks/
│   └── notebook_template.ipynb
├── CHALLENGES.md                          (Bilingual: Arabic + English group tasks)
├── DATASETS.md                            (Comprehensive data dictionary)
├── video_prompt.txt                       (Documentary generation prompt)
├── requirements.txt
└── README.md
```

### Key Features
- **Real data for Morocco** (youth unemployment, cereal yield).
- **Educational data for Jerusalem/Palestine** (can be extended).
- **Expanded dataset list** (more Palestine & Morocco indicators).
- **Bilingual documentation** (Arabic + English).
- **Video prompt** for NotebookLM documentary creation.

### Data Scope
- ✅ **Most comprehensive of workshop3 variants**
- ✅ **Real + educational data mix**
- ✅ **Extensive documentation**

### Target Audience
Full teaching package; multilingual student groups.

---

## 8. `workshop3-mini-project/`

### Purpose
**Lightweight Mini-Project Scaffold** – 1–2 hour focused project for students.

### Key Focus
Minimal scaffolding for students to build one indicator + one chart + one narrative.

### Structure
```
workshop3-mini-project/
├── app/
│   ├── plug_and_play_dashboard.py         (Generic CSV visualizer)
│   └── [empty or starter module]
├── data/
│   ├── jerusalem_checkpoint_wait_times.csv
│   ├── jerusalem_micro_enterprises.csv
│   ├── morocco_agri_stress.csv
│   └── morocco_youth_unemployment.csv
├── notebooks/
│   └── notebook_template.ipynb
├── MINI_PROJECT.md                        (Project instructions in Arabic/English)
├── DATASETS.md
├── README.md
└── requirements.txt
```

### Streamlit App
**File:** `app/plug_and_play_dashboard.py`  
**Type:** Generic CSV loader + auto-visualizer (students pick 1 dataset, compute 1 metric, create 1 chart, write 1 story)

### Data Scope
- ✅ **Minimal, focused**
- ✅ **Beginner-friendly**

### Target Audience
Students working in small groups; 1–2 hour time box.

### Quality Notes
- Uses generic plug-and-play approach (students explore data + build one insight).
- Emphasis on "human story" alongside data visualization.

---

## Summary: Duplicates & Variants

### Module Duplicates
| Aspect | Variants |
|--------|----------|
| **4-module dashboard structure** | `workshop3-dashboard/`, `workshop3-jerusalem-morocco-dashboard/`, `workshop3-jerusalem-morocco-dashboard 2/3/4/` (5 versions) |
| **Youth unemployment Morocco** | Multiple versions: simple regional lines vs. national/urban/rural breakdown (v2+ use national/urban/rural) |
| **Micro-enterprise Jerusalem** | Same structure across all (risk score histogram + income by risk category) |
| **Checkpoint wait times** | Same across all versions |
| **Agricultural stress (NDVI)** | Same across all versions |
| **Generic plug-and-play CSV explorer** | `workshop3-jerusalem-morocco-dashboard 2/`, `workshop3-mini-project/` |

### Canonical Versions (Best Quality/Features)
- **Macro indicators:** `winter-university-2025-ai-crisis-lab-expanded 2/projects/p03_econ_social_crises/app.py` (Plotly, clean sidebar filtering)
- **Education–labor mismatch:** `winter-university-2025-ai-crisis-lab-expanded 2/projects/p06_education_labor_mismatch/app.py` (Advanced scenario modeling)
- **4-module dashboard:** `workshop3-jerusalem-morocco-dashboard 4/app/streamlit_main.py` (Most complete + expanded data)
- **Youth unemployment breakdown:** `workshop3-jerusalem-morocco-dashboard 2/` or `workshop3-jerusalem-morocco-dashboard 4/` (national/urban/rural comparison)

---

## Recommended Next Step: Unified Project

To consolidate for students, consider creating a **single `econ_social_crises_dashboard/` project** with:

1. **Main app** (`app.py`) with sidebar navigation
2. **Pages module** (`pages/`):
   - `macro_indicators.py` (from `p03`)
   - `education_labor_mismatch.py` (from `p06`)
   - `youth_unemployment.py` (from workshop3 v2/v4)
   - `micro_enterprises.py` (from workshop3)
3. **Shared data** (`data/`) – consolidated CSVs
4. **Unified `requirements.txt`** & `README.md`

This would eliminate redundancy and provide students with **one clear, focused project**.

---

## File Inventory Summary

| Folder | Type | Scope | Status |
|--------|------|-------|--------|
| `ai-crisis-workshop/` | Foundation | Broad (5 datasets, mixed crisis types) | Foundational |
| `winter-university-2025-ai-crisis-lab-expanded 2/` | Lab | Very broad (10 projects) | Most advanced |
| `workshop3-dashboard/` | Teaching | Focused (4 modules, basic) | Introductory |
| `workshop3-jerusalem-morocco-dashboard/` | Teaching | Focused (4 modules, real data) | Intermediate |
| `workshop3-jerusalem-morocco-dashboard 2/` | Teaching | Focused (4 modules + plug-and-play) | Advanced |
| `workshop3-jerusalem-morocco-dashboard 3/` | Teaching | Focused (duplicate of v1) | Redundant |
| `workshop3-jerusalem-morocco-dashboard 4/` | Teaching | Focused (4 modules, expanded, multilingual) | Most complete |
| `workshop3-mini-project/` | Teaching | Minimal (scaffold only) | Lightweight |

---

**Last Updated:** November 24, 2025  
**Total Projects:** 8 folders (7 unique + 1 redundant duplicate)  
**Primary Focus:** Economic & Social Crises (Palestine & Morocco)  
**Technology:** Streamlit, Python, Pandas, Plotly
