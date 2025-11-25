# 📦 Winter School 2025 - Distribution Guide

## For Instructors: How to Share This Project

You now have a clean, student-ready repository for the Winter School 2025 Economic & Social Crises module.

---

## 📂 What's in Your Workspace

```
/Users/musicinst/Desktop/winter/
│
├── winter-school-econ-social-crises/          # ✅ MAIN PROJECT (Student-ready)
│   ├── app.py                                  # Main Streamlit application
│   ├── requirements.txt                        # Python dependencies
│   ├── README.md                               # Complete documentation (10KB)
│   ├── QUICKSTART.md                          # Quick start guide
│   ├── LICENSE                                # MIT License for educational use
│   ├── .gitignore                             # Git ignore file
│   ├── pages/                                 # 8 dashboard modules
│   ├── data/                                  # 10 datasets organized by region
│   └── utils/                                 # Shared utilities (empty for now)
│
├── winter-school-econ-social-crises.zip       # ✅ COMPRESSED (48KB for easy sharing)
│
├── _ARCHIVE_old_versions/                     # 📁 Old experimental versions (archived)
│   ├── README.md                              # Archive documentation
│   ├── workshop3-dashboard/
│   ├── workshop3-jerusalem-morocco-dashboard/
│   ├── workshop3-jerusalem-morocco-dashboard 2/
│   ├── workshop3-jerusalem-morocco-dashboard 3/
│   ├── workshop3-jerusalem-morocco-dashboard 4/
│   ├── workshop3-mini-project/
│   ├── winter-university-2025-ai-crisis-lab-expanded 2/
│   └── ai-crisis-workshop/
│
└── [PDF research papers...]                   # Reference materials
```

---

## 🎓 Distribution Options

### Option 1: Direct ZIP Download (Recommended for Email)
**File:** `winter-school-econ-social-crises.zip` (48KB)

**How to share:**
1. Email the ZIP file to students
2. Upload to your course management system (Moodle, Canvas, etc.)
3. Share via cloud storage (Dropbox, Google Drive, etc.)

**Student instructions:**
```
1. Download winter-school-econ-social-crises.zip
2. Extract/unzip the file
3. Open terminal in the extracted folder
4. Run: pip install -r requirements.txt
5. Run: streamlit run app.py
```

### Option 2: Git Repository (Recommended for GitHub/GitLab)
**Folder:** `winter-school-econ-social-crises/`

**How to share:**
1. Initialize git repo:
   ```bash
   cd winter-school-econ-social-crises
   git init
   git add .
   git commit -m "Initial commit: Winter School 2025 Dashboard"
   ```

2. Push to GitHub/GitLab:
   ```bash
   git remote add origin YOUR_REPO_URL
   git push -u origin main
   ```

3. Share the repository URL with students

**Student instructions:**
```
1. git clone YOUR_REPO_URL
2. cd winter-school-econ-social-crises
3. pip install -r requirements.txt
4. streamlit run app.py
```

### Option 3: Cloud Deployment (Advanced)
Deploy to Streamlit Cloud, Heroku, or similar platforms for web access without local installation.

---

## ✅ What Students Get

### Complete Package:
- ✅ **8 interactive dashboard pages** focusing on economic & social crises
- ✅ **10 datasets** (macro, Morocco, Palestine, Jerusalem)
- ✅ **Bilingual support** (Arabic/English on 4 pages)
- ✅ **Complete documentation** (README + QUICKSTART)
- ✅ **Clean code** with educational comments
- ✅ **No dependencies** on external APIs or services

### Technical Requirements:
- Python 3.8+
- ~20MB disk space
- Internet connection for pip install only

---

## 📋 Pre-Distribution Checklist

Before sharing with students:

- ✅ Verified all 8 pages work correctly
- ✅ Verified all 10 datasets are present
- ✅ Removed all __pycache__ and .pyc files
- ✅ Created .gitignore for clean repo
- ✅ Added MIT LICENSE for educational use
- ✅ Created comprehensive README.md
- ✅ Created QUICKSTART.md for quick setup
- ✅ Created compressed ZIP (48KB)
- ✅ Archived old/duplicate versions

---

## 🎯 Recommended Teaching Flow

### Week 1: Introduction & Macro Indicators
- Have students set up the dashboard
- Explore Macro Indicators page
- Compare Palestine vs Morocco trends

### Week 2: Labor Markets
- Youth Unemployment (Morocco)
- Education-Labor Mismatch (Palestine)
- Discussion: structural vs cyclical unemployment

### Week 3: Regional Crises
- Agricultural Stress (Morocco)
- Checkpoint Monitor (Jerusalem)
- Micro-Enterprises (Jerusalem)

### Week 4: Household Impacts & Policy
- Household Budgets (Palestine)
- Data Explorer (custom analysis)
- Final project presentations

---

## 🛠️ Customization Options

### Adding New Datasets:
Students can add CSV files to the `data/` folder and use the Data Explorer to visualize them.

### Adding New Pages:
Instructors can create new dashboard pages in `pages/` folder following the existing pattern.

### Multilingual Support:
Extend bilingual support to additional pages or add new languages.

---

## 📧 Student Support

Include these in your course materials:

**Installation Issues:**
- Refer students to QUICKSTART.md
- Common issue: Python version (need 3.8+)
- Common issue: pip not in PATH

**Data Questions:**
- All data sources documented in README.md
- Datasets are synthetic/educational only
- Encourage students to discuss patterns, not treat as real policy data

**Technical Questions:**
- Code is heavily commented for self-study
- Each page is modular and can be studied independently
- Encourage peer collaboration

---

## 🗑️ Cleaning Up Old Versions

The `_ARCHIVE_old_versions/` folder contains all experimental versions. You can:

**Keep it if:**
- You want reference to original experiments
- You need to verify consolidation decisions
- You want alternative implementations

**Delete it if:**
- You're confident everything needed is in the main project
- You want to save ~50MB disk space
- You want a completely clean workspace

To delete:
```bash
cd /Users/musicinst/Desktop/winter
rm -rf _ARCHIVE_old_versions
```

---

## 📊 Project Statistics

**Main Project Size:**
- Uncompressed: ~100KB
- Compressed ZIP: 48KB
- Number of files: 30
- Lines of Python code: ~3,500
- Number of datasets: 10

**Feature Count:**
- Dashboard pages: 8
- Visualizations: 25+
- Interactive filters: 15+
- Bilingual pages: 4

---

## 🎉 Ready to Distribute!

Your Winter School 2025 dashboard is now:
- ✅ Clean and organized
- ✅ Fully documented
- ✅ Student-ready
- ✅ Easy to distribute
- ✅ Open source (MIT License)

**Next Steps:**
1. Choose your distribution method (ZIP, Git, or Cloud)
2. Share with students
3. Monitor the first setup session to help with any issues
4. Enjoy teaching with interactive data visualization!

---

**Questions?** Review the README.md and QUICKSTART.md in the main project folder.

**Good luck with your Winter School 2025!** 🎓📊
