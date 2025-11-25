# 🚀 Getting Started - Winter University 2025

**Welcome Students!** This guide will help you get the workshop materials running on your computer in just 5 minutes.

---

## 📥 Step 1: Download the Repository

### Option A: Using Git (Recommended)
```bash
git clone https://github.com/hnuseibeh/winter-university.git
cd winter-university
```

### Option B: Download ZIP
1. Go to https://github.com/hnuseibeh/winter-university
2. Click the green **"Code"** button
3. Select **"Download ZIP"**
4. Extract the ZIP file
5. Open terminal/command prompt and navigate to the folder

---

## 🐍 Step 2: Install Python Requirements

### Check if Python is installed:
```bash
python --version
```
You need Python 3.8 or higher. If you don't have it, download from [python.org](https://www.python.org/downloads/).

### Install required packages:
```bash
pip install -r requirements.txt
```

**What gets installed:**
- Streamlit (web app framework)
- Pandas (data analysis)
- Plotly (interactive visualizations)

---

## 🧙 Step 3: Run the Interactive Wizard

The wizard will guide you through the data and help you understand the crisis datasets:

```bash
streamlit run wizard.py
```

Your browser should automatically open to `http://localhost:8501`

**If it doesn't open automatically:**
- Open your browser manually
- Go to: http://localhost:8501

---

## 📊 Explore the Reference Dashboards (Optional)

### Reference Dashboard (Simpler - 4 pages)
```bash
cd reference-dashboard
pip install -r requirements.txt
streamlit run app.py
```

### Reference Examples (Comprehensive - 8 pages)
```bash
cd reference-examples
pip install -r requirements.txt
streamlit run app.py
```

**To stop the app:** Press `Ctrl+C` in the terminal

---

## 📝 Step 4: Start Your Team Project

1. Open the `student-template/` folder
2. Read `student-template/README.md`
3. Start filling out `project-concept.md` with your team's idea
4. Use `presentation-guide.md` to prepare your presentation

---

## 🆘 Troubleshooting

### Problem: "Python not found"
**Solution:** Install Python from https://www.python.org/downloads/

### Problem: "pip not found"
**Solution:**
```bash
python -m pip install -r requirements.txt
```

### Problem: "Permission denied"
**Solution:** Add `--user` flag:
```bash
pip install --user -r requirements.txt
```

### Problem: Port 8501 already in use
**Solution:**
```bash
streamlit run wizard.py --server.port 8502
```

### Problem: Module not found errors
**Solution:** Make sure you're in the correct directory and reinstall:
```bash
pip install --force-reinstall -r requirements.txt
```

### Problem: Browser doesn't open automatically
**Solution:** Manually open http://localhost:8501 in your browser

---

## 📚 What's in This Repository?

```
winter-university/
├── 📖 WORKSHOP_BRIEF.md        ← Workshop instructions
├── 🧙 wizard.py                ← Interactive learning wizard (START HERE!)
├── 📊 requirements.txt         ← Python packages needed
│
├── 📁 student-template/        ← YOUR WORKSPACE
│   ├── README.md                  Instructions
│   ├── project-concept.md         Document your idea here
│   └── presentation-guide.md      Presentation tips
│
├── 📁 reference-dashboard/     ← Example app (simpler)
├── 📁 reference-examples/      ← Example app (comprehensive)
├── 📁 real_data/               ← Crisis datasets (6 CSV files)
└── 📁 docs/                    ← Additional documentation
```

---

## 🎯 Quick Commands Reference

| Task | Command |
|------|---------|
| **Run wizard** | `streamlit run wizard.py` |
| **Stop app** | `Ctrl+C` in terminal |
| **Install packages** | `pip install -r requirements.txt` |
| **Update from GitHub** | `git pull` |
| **Check Python version** | `python --version` |

---

## 🌐 Access the Online Version

If you don't want to install anything locally, you can access the wizard online at:

**https://winter.digital-economy.org**

(Available after deployment is complete)

---

## 📖 Next Steps

1. ✅ Run the wizard: `streamlit run wizard.py`
2. ✅ Explore the 6 datasets (humanitarian, climate, agriculture, timeline, sentiment, news)
3. ✅ Review reference dashboards for inspiration
4. ✅ Read `WORKSHOP_BRIEF.md` for full workshop instructions
5. ✅ Start working in `student-template/`

---

## 🤝 Need Help?

- **Technical issues:** Ask workshop facilitators
- **Understanding the data:** Use the wizard's learning lessons
- **Project ideas:** Check `student-template/resources/`
- **GitHub issues:** Open an issue at https://github.com/hnuseibeh/winter-university/issues

---

## 🌟 Languages / اللغات

This repository supports:
- 🇬🇧 English
- 🇦🇪 العربية (Arabic)
- 🇫🇷 Français (French)

---

**Ready to start?**

```bash
streamlit run wizard.py
```

**Good luck! / بالتوفيق! / Bonne chance!** 🎓✨

---

*Winter University 2025 - Bayt Mal Al-Quds Asharif Agency*
