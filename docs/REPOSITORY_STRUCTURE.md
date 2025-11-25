# Winter University 2025 – Repository Structure

## Visual Directory Tree

```
winter/ (Root Repository)
│
├─ ⭐ STUDENT WORKSPACE (Start Here!)
│  ├── WORKSHOP_BRIEF.md ..................... Full workshop instructions (AR/EN/FR)
│  ├── README.md ............................. Quick start guide for students
│  ├── QUICK_START.md ........................ Fast-track onboarding
│  └── student-template/ ..................... 🎯 YOUR WORKING DIRECTORY
│      ├── README.md
│      ├── project-concept.md ............... Document your idea HERE
│      ├── presentation-guide.md ............ How to present (3-5 min)
│      └── resources/ ........................ Background readings & datasets
│
├─ 🔍 REFERENCE MATERIALS (Learn by Example)
│  ├── reference-dashboard/ ................. Complete Streamlit dashboard example
│  │   ├── app.py
│  │   ├── pages/ .......................... Multi-page dashboard modules
│  │   ├── data/ ........................... Crisis indicator datasets
│  │   ├── utils/ .......................... Reusable functions
│  │   ├── requirements.txt ................ Dependencies
│  │   └── README.md/.../SETUP.md ......... Setup instructions
│  └── winter-school-econ-social-crises/ ... Full working application
│      ├── app.py
│      ├── pages/ .......................... 8 specialized analysis pages
│      ├── data/ ........................... Jerusalem, Morocco, Palestine datasets
│      └── requirements.txt
│
├─ 📚 DOCUMENTATION
│  └── docs/
│      ├── README_START_HERE.txt ........... Initial orientation guide
│      ├── DISTRIBUTION_GUIDE.md .......... How to share & distribute work
│      ├── GITHUB_PUSH_CHECKLIST.md ...... Git workflow checklist
│      ├── WORKSPACE_INVENTORY.md ........ Detailed file inventory
│      └── FINAL_SUMMARY.md .............. Project completion summary
│
├─ 🗄️ ARCHIVE (Historical/Reference Only)
│  └── _archive/ ............................ Previous workshop iterations
│  └── archive/ ............................. Research PDFs & reference documents
│
└─ 🔧 Configuration
   ├── .claude/ ............................. Claude settings
   ├── .gitignore ........................... Git ignore rules
   └── LICENSE .............................. Repository license
```

## Quick Reference

| Directory | Purpose | Use Case | Status |
|-----------|---------|----------|--------|
| **student-template/** | Your team's workspace | Edit your project concept & presentation | 🟢 ACTIVE |
| **reference-dashboard/** | Working example | Learn by studying complete code | 📖 Reference |
| **docs/** | Workshop documentation | Find setup & process guides | 📖 Reference |
| **archive/** | Research papers | Background reading on crises | 📖 Reference |
| **_archive/** | Old workshop versions | Historical reference only | 🗂️ Archive |

## What Students Should Do

✅ **DO:**
1. Start with `WORKSHOP_BRIEF.md` (read in your language)
2. Edit `student-template/project-concept.md` with your team's idea
3. Run `reference-dashboard/` to see a working example
4. Use `student-template/resources/` for background context
5. Prepare presentation using `presentation-guide.md`

❌ **DON'T:**
- Modify files outside `student-template/` (unless learning)
- Edit `reference-dashboard/` (it's read-only reference)
- Commit work to wrong folders
- Skip reading the context materials

## Key Files by Use Case

| Need | File |
|------|------|
| Workshop overview | `WORKSHOP_BRIEF.md` |
| Start coding | `student-template/README.md` |
| See working example | `reference-dashboard/README.md` |
| Present your idea | `student-template/presentation-guide.md` |
| Background context | `student-template/resources/*.md` |
| Setup Streamlit | `reference-dashboard/SETUP.md` |

---

**Ready to start?** → `WORKSHOP_BRIEF.md` • **Working space?** → `student-template/` • **Need help?** → `docs/README_START_HERE.txt`
