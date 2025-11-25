# GitHub Deployment Guide

This guide walks you through pushing your Winter University Crisis Dashboard project to GitHub.

## Prerequisites

1. **GitHub Account** - Create at https://github.com if you don't have one
2. **Git Installed** - Check with: `git --version`
3. **Your Project** - Ready at `/Users/musicinst/Desktop/winter/`

## Step 1: Initialize Local Repository

```bash
cd /Users/musicinst/Desktop/winter

# Initialize git
git init

# Configure git (if first time)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Check status
git status
```

## Step 2: Add All Files to Git

```bash
# Add all files
git add .

# Verify what will be committed
git status

# You should see ~25-30 files to commit (not 100+)
# If you see __pycache__ or .DS_Store, .gitignore isn't working
```

## Step 3: Create First Commit

```bash
git commit -m "Initial commit: Winter University Crisis Dashboard and Student Wizard

- Complete Streamlit-based educational platform
- Student wizard with 6 learning modules
- Two reference dashboards (4 and 8 pages)
- 30+ real datasets on Palestinian and Moroccan crises
- Comprehensive documentation and guides
- Ready for GitHub and student deployment"
```

## Step 4: Create Repository on GitHub

1. Go to https://github.com/new
2. Fill in:
   - **Repository name:** `winter-crisis-dashboard`
   - **Description:** Educational platform for analyzing Palestinian & Moroccan crises using AI
   - **Visibility:** Public (for students) or Private (for team only)
   - **Initialize:** Do NOT check any boxes (we already have files)
3. Click "Create repository"

## Step 5: Connect Local to Remote

```bash
# Replace YOUR_USERNAME with your GitHub username
git remote add origin https://github.com/YOUR_USERNAME/winter-crisis-dashboard.git

# Verify
git remote -v
```

## Step 6: Push to GitHub

```bash
# Rename branch to 'main' (GitHub standard)
git branch -M main

# Push your code
git push -u origin main

# This will prompt for GitHub credentials (use personal access token)
```

## Step 7: Verify on GitHub

1. Visit `https://github.com/YOUR_USERNAME/winter-crisis-dashboard`
2. Check that all files are there:
   - ✅ wizard.py
   - ✅ reference-dashboard/
   - ✅ reference-examples/
   - ✅ README.md
   - ✅ All documentation
3. Verify .gitignore is working (no __pycache__ folders shown)

## For Students: How to Clone

Once on GitHub, students can:

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/winter-crisis-dashboard.git
cd winter-crisis-dashboard

# Install dependencies
pip install -r requirements.txt

# Run the wizard
streamlit run wizard.py

# Or run the dashboards
cd reference-dashboard && streamlit run app.py
```

## Optional: Deploy Wizard Online

### Option 1: Streamlit Cloud (Free)

```bash
# From your project directory
streamlit deploy

# Follow prompts to authenticate with GitHub
# Choose wizard.py as the main file
# Your app will be live at: https://YOUR_USERNAME-winter-crisis-dashboard.streamlit.app
```

### Option 2: GitHub Pages (Static Site)

The `web/` folder can host a static landing page:

1. Go to repository Settings
2. Go to "Pages"
3. Set source to: `main` branch, `/web` folder
4. Your site will be at: `https://YOUR_USERNAME.github.io/winter-crisis-dashboard/`

## Ongoing: Making Updates

After initial push, to update:

```bash
# Make changes to files

# Stage changes
git add .

# Commit with message
git commit -m "Description of changes"

# Push to GitHub
git push
```

## Common Issues & Solutions

### Issue: "Git command not found"
**Solution:** Install Git from https://git-scm.com/

### Issue: "Permission denied (publickey)"
**Solution:** 
- Generate SSH key: `ssh-keygen -t ed25519`
- Add to GitHub: Settings → SSH Keys
- Or use HTTPS with personal access token

### Issue: Large files error
**Solution:** Our .gitignore prevents large files. Check:
```bash
git ls-files | sort -k5 -rn | head -10
```

### Issue: __pycache__ folders appearing in GitHub
**Solution:** 
```bash
git rm -r --cached __pycache__/
git commit -m "Remove __pycache__ from tracking"
git push
```

## Repository Settings to Configure

After creating the repo:

### 1. Add Collaborators (for team)
- Settings → Collaborators
- Add team members with Write access

### 2. Set Default Branch
- Settings → General
- Default branch: `main`

### 3. Enable Issues (for feedback)
- Settings → Features
- Check "Issues"

### 4. Add Topics (for discoverability)
- Add: `education`, `crisis-analysis`, `palestine`, `morocco`, `ai`, `streamlit`

### 5. Branch Protection (optional for main)
- Settings → Branches
- Add rule for `main`
- Require status checks before merge

## Files Not in Repository (Good!)

These should NOT appear on GitHub (handled by .gitignore):

- ❌ __pycache__/ folders
- ❌ *.pyc files
- ❌ .venv/ or venv/ folders
- ❌ .env files
- ❌ .DS_Store
- ❌ .idea/ or .vscode/ folders
- ❌ _archive/ folder (old versions)

## Repository Structure on GitHub

Your GitHub repo will show:

```
📂 winter-crisis-dashboard/
├── 📄 README.md (Main page)
├── 📄 QUICK_START.md
├── 📄 requirements.txt
├── 📄 wizard.py ⭐
├── 📄 DEPLOYMENT_READINESS.md
├── 📄 WIZARD_README.md
├── 📁 reference-dashboard/
├── 📁 reference-examples/
├── 📁 docs/
├── 📁 scrapers/
├── 📁 student-template/
├── 📁 web/
└── 📁 real_data/
```

## Sharing with Students

After deploying to GitHub:

### Share the Link
```
https://github.com/YOUR_USERNAME/winter-crisis-dashboard
```

### For Classroom
1. Have students fork: Click "Fork" button
2. Students clone their fork
3. They work in their own copy
4. Option to submit pull requests with findings

### For Direct Access
Share the Streamlit deployment link if using Streamlit Cloud:
```
https://YOUR_USERNAME-winter-crisis-dashboard.streamlit.app
```

## GitHub Actions (Optional Advanced)

Create `.github/workflows/test.yml` for automated testing:

```yaml
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
      - run: pip install -r requirements.txt
      - run: python -m py_compile wizard.py
      - run: python -m py_compile reference-dashboard/app.py
```

## Next Steps

1. ✅ Initialize git locally
2. ✅ Commit all files
3. ✅ Create GitHub repository
4. ✅ Push to GitHub
5. ✅ Share link with students/team
6. ✅ (Optional) Deploy wizard to Streamlit Cloud
7. ✅ (Optional) Enable GitHub Pages for landing page

## Support

For issues:
- GitHub Help: https://docs.github.com/
- Git Guide: https://git-scm.com/doc
- Streamlit Deploy: https://docs.streamlit.io/deploy/streamlit-community-cloud

---

**Ready to push?** Run the commands above to get your project to GitHub!

