# 🌐 Workshop Webpage Deployment Guide
**Deploy to winter.digital-economy.org**

---

## 📦 What You're Deploying

A complete multilingual workshop landing page with:
- ✅ Workshop information and objectives
- ✅ Interactive language switcher (English/Arabic/French)
- ✅ Links to reference dashboards
- ✅ Student access instructions with QR code
- ✅ University logos and branding
- ✅ Responsive design (mobile-friendly)

**Location:** `/web/` folder
**Main file:** `web/index.html`

---

## 🚀 Deployment Options

### Option 1: Deploy to Your Web Server (Recommended)

If you have SSH access to winter.digital-economy.org:

#### Step 1: SSH into Your Server
```bash
ssh user@winter.digital-economy.org
```

#### Step 2: Navigate to Web Root
```bash
# Common web root locations:
cd /var/www/html                    # Apache default
# OR
cd /usr/share/nginx/html            # Nginx default
# OR
cd /var/www/winter.digital-economy.org   # Custom vhost
```

#### Step 3: Clone Repository
```bash
# Clone the repo
git clone https://github.com/hnuseibeh/winter-university.git

# Copy web files to web root
cp -r winter-university/web/* .

# OR create a subdirectory
mkdir -p workshop3
cp -r winter-university/web/* workshop3/
```

#### Step 4: Set Permissions
```bash
# Ensure web server can read files
sudo chown -R www-data:www-data .
sudo chmod -R 755 .
```

#### Step 5: Verify
Open your browser and visit:
- `https://winter.digital-economy.org/`
- OR `https://winter.digital-economy.org/workshop3/`

---

### Option 2: GitHub Pages (Free & Easy)

Deploy directly from your GitHub repository:

#### Step 1: Enable GitHub Pages
1. Go to https://github.com/hnuseibeh/winter-university/settings/pages
2. Under "Source", select:
   - **Branch:** `main`
   - **Folder:** `/web`
3. Click **Save**

#### Step 2: Wait for Deployment
- GitHub will build and deploy your site (1-2 minutes)
- Your site will be available at: `https://hnuseibeh.github.io/winter-university/`

#### Step 3: Configure Custom Domain (Optional)
1. In GitHub Pages settings, add custom domain: `winter.digital-economy.org`
2. Add DNS records (see DNS Configuration section below)

---

### Option 3: Netlify (Fast & Modern)

Deploy with continuous deployment:

#### Step 1: Sign Up
1. Go to https://netlify.com
2. Sign up with your GitHub account

#### Step 2: Deploy
1. Click **"Add new site"** → **"Import an existing project"**
2. Connect to GitHub and select: `hnuseibeh/winter-university`
3. Configure:
   - **Branch:** `main`
   - **Base directory:** `web`
   - **Publish directory:** `web`
4. Click **Deploy**

#### Step 3: Configure Custom Domain
1. Go to **Site settings** → **Domain management**
2. Add custom domain: `winter.digital-economy.org`
3. Follow Netlify's DNS instructions

**Benefits:**
- Automatic deployments on git push
- Free SSL certificate
- CDN for fast global access
- Preview deployments for branches

---

### Option 4: Traditional FTP/SFTP Upload

If you only have FTP access:

#### Using FileZilla or Similar:
1. Connect to your server via FTP/SFTP
2. Navigate to your web root directory
3. Upload the entire `/web/` folder contents:
   ```
   web/
   ├── index.html
   ├── assets/
   │   ├── css/
   │   ├── js/
   │   └── logos/
   ```
4. Ensure all files are uploaded completely
5. Visit your domain to verify

---

## 🔧 DNS Configuration

To point winter.digital-economy.org to your hosting:

### For Web Server (Option 1)
Add an A record:
```
Type: A
Name: winter (or @)
Value: [YOUR_SERVER_IP]
TTL: 3600
```

### For GitHub Pages (Option 2)
Add CNAME record:
```
Type: CNAME
Name: winter (or www)
Value: hnuseibeh.github.io
TTL: 3600
```

### For Netlify (Option 3)
Follow Netlify's custom DNS instructions (they provide specific records)

---

## 🔐 SSL Certificate (HTTPS)

### Using Let's Encrypt (Free)

If you have server access:

```bash
# Install Certbot
sudo apt-get update
sudo apt-get install certbot python3-certbot-nginx

# Get certificate (for Nginx)
sudo certbot --nginx -d winter.digital-economy.org

# OR for Apache
sudo certbot --apache -d winter.digital-economy.org

# Auto-renewal is set up automatically
```

### Using Cloudflare (Free)
1. Sign up at https://cloudflare.com
2. Add your domain
3. Update nameservers at your registrar
4. Enable SSL (Flexible or Full)

---

## 📁 Files Structure on Server

Your deployed website should look like:

```
/var/www/html/  (or your web root)
├── index.html              # Main landing page
├── assets/
│   ├── css/
│   │   └── style.css       # Styling
│   ├── js/
│   │   ├── language.js     # Language switcher
│   │   └── link-checker.js # GitHub link validation
│   └── logos/
│       ├── WhatsApp Image 2025-11-24 at 09.45.07.jpeg
│       ├── WhatsApp Image 2025-11-24 at 09.45.07 (1).jpeg
│       ├── WhatsApp Image 2025-11-24 at 09.45.08.jpeg
│       └── WhatsApp Image 2025-11-24 at 09.45.20.jpeg
```

---

## ✅ Post-Deployment Checklist

After deployment, verify:

- [ ] Page loads at https://winter.digital-economy.org
- [ ] All CSS styles are applied correctly
- [ ] University logos display properly
- [ ] Language switcher works (English/Arabic/French)
- [ ] GitHub repository link works
- [ ] QR code displays and scans correctly
- [ ] All internal links work
- [ ] Page is mobile-responsive
- [ ] HTTPS/SSL certificate is valid
- [ ] No console errors in browser developer tools

---

## 🔄 Updating the Website

### Method 1: Via Git (Recommended)
```bash
# SSH into server
ssh user@winter.digital-economy.org
cd /var/www/html

# Pull latest changes
git pull origin main
```

### Method 2: Via FTP
1. Make changes locally in `/web/` folder
2. Upload modified files via FTP
3. Overwrite existing files

### Method 3: Automated (GitHub Actions)
- GitHub Pages auto-deploys on push
- Netlify auto-deploys on push

---

## 🌍 Multi-Deployment Strategy (Recommended)

Deploy to multiple platforms for redundancy:

1. **Primary:** Your server at winter.digital-economy.org
   - Full control, fast access for local users

2. **Backup:** GitHub Pages at hnuseibeh.github.io/winter-university
   - Free, reliable, automatic updates

3. **CDN:** Netlify with custom domain
   - Global CDN, fast worldwide access

---

## 🆘 Troubleshooting

### Problem: CSS/JS Not Loading
**Solution:** Check file paths in index.html. Ensure they're relative:
```html
<!-- Correct -->
<link rel="stylesheet" href="assets/css/style.css">

<!-- Wrong (absolute path) -->
<link rel="stylesheet" href="/assets/css/style.css">
```

### Problem: Images Not Displaying
**Solution:**
- Verify all image files are uploaded
- Check file names match exactly (case-sensitive on Linux)
- URL encode spaces: `WhatsApp%20Image...`

### Problem: 403 Forbidden Error
**Solution:** Fix file permissions:
```bash
sudo chmod -R 755 /var/www/html
sudo chown -R www-data:www-data /var/www/html
```

### Problem: Domain Not Resolving
**Solution:**
- Check DNS propagation: https://dnschecker.org
- DNS changes can take 24-48 hours
- Clear your browser cache

### Problem: GitHub Links Not Working
**Solution:**
- Ensure repository is public
- Check link-checker.js is loaded
- Verify GitHub URL is correct in index.html

---

## 🎯 Quick Deploy Commands

### Deploy to Server
```bash
# One-line deploy
ssh user@winter.digital-economy.org "cd /var/www/html && git clone https://github.com/hnuseibeh/winter-university.git && cp -r winter-university/web/* . && sudo chown -R www-data:www-data . && sudo chmod -R 755 ."
```

### Update Existing Deployment
```bash
ssh user@winter.digital-economy.org "cd /var/www/html && git pull origin main && cp -r web/* ../"
```

---

## 📊 Expected URLs After Deployment

| Resource | URL |
|----------|-----|
| **Workshop Landing Page** | https://winter.digital-economy.org |
| **GitHub Repository** | https://github.com/hnuseibeh/winter-university |
| **Wizard App (Streamlit)** | https://winter-digital-economy.streamlit.app |
| **GitHub Pages (Backup)** | https://hnuseibeh.github.io/winter-university |

---

## 📞 Need Help?

### Server Access Issues
- Contact your hosting provider
- Check SSH key permissions
- Verify server credentials

### DNS Issues
- Use https://dnschecker.org to check propagation
- Contact your domain registrar
- Check nameserver configuration

### Technical Issues
- Check browser console for errors (F12)
- Verify all files uploaded correctly
- Test on different browsers/devices

---

## ✨ Summary

You have a production-ready workshop landing page at `/web/`. Choose one of the deployment options above based on your server access and technical requirements.

**Fastest:** GitHub Pages (5 minutes, no server needed)
**Most Control:** Your own server (10 minutes with SSH access)
**Most Modern:** Netlify (5 minutes, includes CDN + auto-deploy)

---

*Last Updated: November 25, 2025*
*Deployment Status: READY FOR PRODUCTION*
