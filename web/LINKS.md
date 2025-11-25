# Link Verification & Configuration Guide

This document describes all links in the Workshop 3 webpage and how to verify/update them.

## 📋 Link Inventory

### Internal Asset Links (Relative Paths)

These links are relative to the `web/` folder and should work correctly:

1. **CSS Stylesheet**
   - Path: `assets/css/style.css`
   - Status: ✅ Working
   - Location: Line 9 in `index.html`

2. **JavaScript Files**
   - `assets/js/language.js` - Language switching functionality
   - `assets/js/link-checker.js` - Link validation
   - Status: ✅ Working
   - Location: Lines 296-297 in `index.html`

3. **Logo Images**
   - `assets/logos/WhatsApp%20Image%202025-11-24%20at%2009.45.07.jpeg`
   - `assets/logos/WhatsApp%20Image%202025-11-24%20at%2009.45.07%20(1).jpeg`
   - `assets/logos/WhatsApp%20Image%202025-11-24%20at%2009.45.08.jpeg`
   - `assets/logos/WhatsApp%20Image%202025-11-24%20at%2009.45.20.jpeg`
   - Status: ✅ Working (URL-encoded for spaces)
   - Location: Lines 29, 32, 35, 38 in `index.html`

### External Tool Links (Relative to Parent Directory)

These links point to tools in the parent directory structure:

1. **Reference Dashboard**
   - Folder: `../reference-dashboard/`
   - README: `../reference-dashboard/README.md`
   - Status: ✅ Working (if tools are at same level as `web/` folder)
   - Location: Lines 128-129 in `index.html`

2. **Reference Examples**
   - Folder: `../reference-examples/`
   - README: `../reference-examples/README.md`
   - Status: ✅ Working (if tools are at same level as `web/` folder)
   - Location: Lines 170-171 in `index.html`

### Placeholder Links

1. **Student Repository Link**
   - Current: Placeholder text (not a link)
   - Status: ⚠️ Needs to be updated when repository URL is available
   - Location: Line 193 in `index.html`
   - Update method: Edit HTML or use `updateStudentRepoLink(url)` JavaScript function

## 🔧 Link Configuration for Production

### Current Structure (Local Development)
```
winter/
├── web/                    (webpage files)
├── reference-dashboard/    (tool 1)
└── reference-examples/     (tool 2)
```

### Production Deployment Options

#### Option 1: Same Structure (Recommended)
If deploying the entire `winter/` folder structure:
- Links will work as-is: `../reference-dashboard/` and `../reference-examples/`
- No changes needed

#### Option 2: Web Root Deployment
If only `web/` contents are deployed to `winter.digital-economy.org` root:
- Update tool links to absolute paths or subdirectories
- Example: Change `../reference-dashboard/` to `/reference-dashboard/` or `reference-dashboard/`

#### Option 3: Separate Tool Deployment
If tools are deployed separately:
- Update links to full URLs: `https://winter.digital-economy.org/reference-dashboard/`
- Or use subdomain: `https://tools.winter.digital-economy.org/`

## ✅ Link Verification Checklist

Before deploying to production:

- [ ] All CSS and JS files load correctly
- [ ] All logo images display properly
- [ ] Tool folder links work (test clicking "View Dashboard Folder")
- [ ] Tool README links work (test clicking "Read Documentation")
- [ ] Student repository link is updated (if available)
- [ ] All links tested in target browser(s)
- [ ] Links work on mobile devices
- [ ] No 404 errors in browser console

## 🛠️ How to Update Links

### Update Student Repository Link

**Method 1: Edit HTML directly**
```html
<!-- Find this line (around line 193) -->
<span class="repo-url" id="student-repo-link">[Student Repository Link - To be provided during workshop]</span>

<!-- Replace with: -->
<a href="https://github.com/username/repo" target="_blank" rel="noopener noreferrer" class="repo-url" id="student-repo-link">https://github.com/username/repo</a>
```

**Method 2: Use JavaScript (in browser console)**
```javascript
updateStudentRepoLink('https://github.com/username/repo');
```

### Update Tool Links for Different Deployment

If tools are in a different location, update paths in `index.html`:

**For absolute paths:**
```html
<!-- Change from: -->
<a href="../reference-dashboard/" ...>

<!-- To: -->
<a href="/reference-dashboard/" ...>
<!-- or -->
<a href="https://winter.digital-economy.org/reference-dashboard/" ...>
```

## 🧪 Testing Links

### Local Testing
1. Start local server: `cd web && python3 -m http.server 8000`
2. Open `http://localhost:8000`
3. Check browser console for 404 errors
4. Click all links to verify they work

### Production Testing
1. Deploy to `winter.digital-economy.org`
2. Open browser developer tools (F12)
3. Check Network tab for failed requests
4. Test all links manually
5. Verify on mobile devices

## 📝 Notes

- All asset paths are relative and will work as long as folder structure is maintained
- Image filenames with spaces are URL-encoded (%20 for spaces)
- Tool links assume tools are accessible at the same domain
- Student repository link is intentionally a placeholder until the repository is created

---

**Last Updated:** November 25, 2025

