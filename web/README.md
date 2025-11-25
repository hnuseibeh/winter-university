# Workshop 3 Webpage - Deployment Guide

This folder contains the professional webpage for **Workshop 3: Approaches to Economic and Social Crises and the Protection of Cultural Heritage Using AI**, presented by Dr. Hasan Nuseibeh on November 25, 2025.

## 🌐 Production Site

**Live URL:** `https://winter.digital-economy.org`

The DNS for this domain is already configured. Deploy the contents of this `web/` folder to the web server root.

## 📁 Folder Structure

```
web/
├── index.html              # Main workshop webpage
├── README.md              # This file
└── assets/
    ├── css/
    │   └── style.css      # Professional stylesheet
    ├── logos/             # University logos
    └── js/                # JavaScript files (if needed)
```

## 🚀 Deployment

### Production Domain

**Live URL:** `https://winter.digital-economy.org`

The DNS for `winter.digital-economy.org` is already configured. Deploy the contents of the `web/` folder to the web server root for this domain.

### Deployment Steps

1. **Upload Files to Server**
   - Upload all contents of the `web/` folder to the web root directory
   - Ensure the folder structure is maintained:
     ```
     web-root/
     ├── index.html
     ├── assets/
     │   ├── css/
     │   ├── logos/
     │   └── js/
     ```

2. **Verify File Permissions**
   - Ensure files are readable by the web server
   - Typical permissions: 644 for files, 755 for directories

3. **Test the Site**
   - Visit `https://winter.digital-economy.org` in a browser
   - Verify all assets load correctly
   - Check that all links work properly

### Alternative Deployment Options

#### Option 1: GitHub Pages (If needed for backup/mirror)

1. **Push to GitHub Repository**
   ```bash
   git add web/
   git commit -m "Add Workshop 3 webpage"
   git push origin main
   ```

2. **Enable GitHub Pages**
   - Go to your repository on GitHub
   - Navigate to Settings → Pages
   - Under "Source", select "Deploy from a branch"
   - Choose "main" branch and "/web" folder
   - Click Save

3. **Access Your Site**
   - Your site will be available at: `https://[username].github.io/[repository-name]/web/`

#### Option 2: Local Development Server

For testing locally before deployment:

```bash
# Using Python 3
cd web
python -m http.server 8000

# Using Node.js (if you have http-server installed)
npx http-server web -p 8000

# Using PHP
cd web
php -S localhost:8000
```

Then open `http://localhost:8000` in your browser.

## 📋 Pre-Deployment Checklist

- [ ] All logo images are properly displayed (check `assets/logos/` folder)
- [ ] All CSS styles are loading correctly
- [ ] All links to tools (reference-dashboard, reference-examples) work correctly
- [ ] Student repository link placeholder is updated with actual URL (if available)
- [ ] Test the page on different browsers (Chrome, Firefox, Safari, Edge)
- [ ] Test responsive design on mobile devices
- [ ] Verify all text content is accurate
- [ ] Check that all images have proper alt text for accessibility

## 🔗 Important Links to Update

Before deploying, make sure to update:

1. **Student Repository Link** (in `index.html`):
   - The student repository link is currently a placeholder
   - When the repository URL is available, you can update it by:
     - Editing the HTML directly, or
     - Using the JavaScript function: `updateStudentRepoLink('https://github.com/username/repo')` in the browser console

2. **Tool Links** (Path Configuration):
   - **Current paths:** `../reference-dashboard/` and `../reference-examples/`
   - These paths assume the tools are at the same directory level as the `web/` folder
   - **For production at `winter.digital-economy.org`:**
     - If tools are deployed together: paths should work as-is
     - If tools are in a different location: update paths to absolute URLs or correct relative paths
     - Example: If tools are at root level, change `../reference-dashboard/` to `/reference-dashboard/`

3. **Asset Links** (CSS, JS, Images):
   - All asset links use relative paths: `assets/css/`, `assets/js/`, `assets/logos/`
   - These will work correctly as long as the folder structure is maintained
   - Image filenames with spaces are URL-encoded (e.g., `WhatsApp%20Image%20...`)

## 🎨 Customization

### Changing Colors

Edit `assets/css/style.css` and modify the CSS variables at the top:

```css
:root {
    --primary-color: #1a5490;
    --secondary-color: #2c7fb8;
    --accent-color: #4a90a4;
    /* ... */
}
```

### Adding More Logos

1. Add logo images to `assets/logos/` folder
2. Update the HTML in `index.html` within the `.university-logos` section
3. Ensure images are optimized for web (recommended: max 200KB per image)

### Modifying Content

- Edit `index.html` directly to update text content
- All workshop information is in the HTML file
- Maintain semantic HTML structure for accessibility

## 📱 Browser Compatibility

This webpage is designed to work on:
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## ♿ Accessibility Features

- Semantic HTML5 structure
- Proper heading hierarchy
- Alt text for images (add if missing)
- Keyboard navigation support
- Focus indicators for interactive elements
- Responsive design for all screen sizes

## 🔍 SEO Considerations

The webpage includes:
- Meta description tag
- Semantic HTML structure
- Proper heading hierarchy
- Descriptive alt text (add for logos if needed)

For better SEO, consider:
- Adding Open Graph meta tags for social sharing
- Adding Twitter Card meta tags
- Creating a sitemap.xml if multiple pages

## 📝 Notes

- **Production URL:** `https://winter.digital-economy.org`
- The webpage is designed to be standalone and self-contained
- All assets (CSS, images) use relative paths
- The page links to tools in parent directories (`../reference-dashboard/`, `../reference-examples/`)
- If the tools are deployed separately, update these paths accordingly
- DNS is already configured for `winter.digital-economy.org`

## 🆘 Troubleshooting

### Images Not Loading
- Check that all files in `assets/logos/` are present
- Verify file paths in HTML are correct
- Ensure images are in supported formats (JPEG, PNG, WebP)

### CSS Not Applying
- Check that `assets/css/style.css` exists
- Verify the path in HTML: `<link rel="stylesheet" href="assets/css/style.css">`
- Clear browser cache (Ctrl+F5 or Cmd+Shift+R)

### Links Not Working
- Verify relative paths are correct for your deployment structure
- Check that target files/folders exist
- Test links in a browser to see actual paths

## 📞 Support

For questions or issues with deployment:
- Check the main repository README.md
- Review the Workshop 3 documentation
- Contact the workshop organizer

---

**Last Updated:** November 25, 2025  
**Workshop:** Winter University 2025 - Workshop 3  
**Presenter:** Dr. Hasan Nuseibeh

