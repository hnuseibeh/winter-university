# 🎯 DEPLOYMENT TO winter.digital-economy.org - QUICK REFERENCE

**Status:** ✅ READY FOR PRODUCTION  
**Created:** November 25, 2025  
**URL:** https://winter.digital-economy.org

---

## 📋 What You're Deploying

A complete student learning platform featuring:
- 🧙 Interactive wizard for Palestinian & Moroccan crisis data
- 📊 6 real datasets (humanitarian, climate, agricultural, timeline, sentiment, news)
- 🌐 Web landing page
- 📚 Educational resources
- 💾 Export & reporting tools

---

## 🚀 3 Deployment Options

### ⚡ Option 1: Streamlit Cloud (FASTEST - 2 minutes)

```bash
# 1. Push code to GitHub
git add .
git commit -m "Production ready"
git push origin main

# 2. Go to streamlit.io/cloud
# 3. Connect GitHub account
# 4. Create new app
# 5. Select this repo + wizard.py
# 6. Configure custom domain
```

**Best for:** Quick launch, academic projects  
**Cost:** FREE for public repo

---

### 🐳 Option 2: Docker + Nginx (RECOMMENDED - 10 minutes)

```bash
# 1. SSH into server
ssh user@winter.digital-economy.org

# 2. Clone repository
cd /opt
git clone https://github.com/your-org/winter.git
cd winter

# 3. Run deployment
./deploy.sh prod

# 4. Get SSL certificate
sudo certbot certonly --nginx -d winter.digital-economy.org
```

**Best for:** Full control, production deployment, scaling  
**Cost:** Only server/domain costs

---

### 🖥️ Option 3: Manual Server (TRADITIONAL - 15 minutes)

```bash
# 1. SSH to server
ssh user@winter.digital-economy.org

# 2. Setup
cd /opt/winter
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. Run with systemd (see DEPLOYMENT_GUIDE.md)
# 4. Configure nginx reverse proxy
# 5. Get SSL certificate
```

**Best for:** Minimal dependencies, simple setup  
**Cost:** Only server/domain costs

---

## 📦 Files You Need

### ✅ Already Included

```
winter/
├── 🧙 wizard.py                    # Main application
├── 📋 requirements.txt             # Dependencies
├── 🐳 Dockerfile                   # Container image
├── 🎪 docker-compose.yml           # Container orchestration
├── 🌐 nginx.conf                   # Web server config
├── ⚙️  deploy.sh                    # Deployment automation
├── 📚 .streamlit/config.toml       # Streamlit config
├── 📊 reference-dashboard/data/    # 6 CSV datasets
├── 🌍 web/index.html               # Landing page
└── 📖 DEPLOYMENT_GUIDE.md          # Full guide
```

### 🔗 DNS Configuration

Point these records to your server:

```
winter.digital-economy.org    A    [SERVER_IP]
www.winter.digital-economy.org CNAME winter.digital-economy.org
```

### 🔐 SSL Certificate

Use Let's Encrypt (FREE):

```bash
sudo certbot certonly --nginx \
  -d winter.digital-economy.org \
  -d www.winter.digital-economy.org
```

---

## ✅ Pre-Deployment Checklist

- [ ] Server ready (Ubuntu 20.04+)
- [ ] Python 3.8+ installed
- [ ] Docker installed (if using Docker option)
- [ ] Domain points to server
- [ ] All 6 data CSV files present
- [ ] Code pushed to GitHub
- [ ] Requirements.txt updated
- [ ] Dockerfile builds without errors
- [ ] SSL certificate plan (Let's Encrypt)

---

## 🔍 Quick Verification After Deploy

```bash
# Check app is running
curl https://winter.digital-economy.org

# Check health
curl https://winter.digital-economy.org/_stcore/health

# View logs
docker logs -f winter-wizard

# Check SSL
curl -v https://winter.digital-economy.org 2>&1 | grep SSL

# Verify data
curl https://winter.digital-economy.org/data
```

---

## 📊 Expected URLs After Deployment

| Resource | URL |
|----------|-----|
| **Wizard** | https://winter.digital-economy.org |
| **Health Check** | https://winter.digital-economy.org/_stcore/health |
| **Direct Streamlit** | https://winter.digital-economy.org (if no landing page redirect) |

---

## 🔧 Server Requirements

**Minimum:**
- 2 CPU cores
- 2 GB RAM
- 10 GB storage

**Recommended:**
- 4 CPU cores
- 8 GB RAM
- 50 GB SSD storage

---

## 📞 Support & Help

### Documentation Files
1. **DEPLOYMENT_GUIDE.md** - Complete guide (3 options)
2. **DEPLOYMENT_STATUS.md** - Detailed status report
3. **DEPLOYMENT_READINESS.md** - Implementation guide

### Key Commands

**View logs:**
```bash
docker logs -f winter-wizard  # Docker
journalctl -u winter-wizard -f  # Systemd
```

**Restart app:**
```bash
docker restart winter-wizard  # Docker
systemctl restart winter-wizard  # Systemd
```

**Check status:**
```bash
docker ps  # Docker containers
systemctl status winter-wizard  # Systemd service
```

---

## 🎯 Success Criteria

✅ You've deployed successfully when:

1. ✅ Domain resolves to your server
2. ✅ HTTPS connection works (valid certificate)
3. ✅ Wizard page loads at root URL
4. ✅ All 6 pages in wizard function
5. ✅ Data loads in explorer
6. ✅ Export feature works
7. ✅ Health check passes
8. ✅ No browser console errors
9. ✅ Loads in < 3 seconds
10. ✅ Works on mobile browsers

---

## 🚨 Troubleshooting

| Problem | Solution |
|---------|----------|
| **App won't start** | `docker logs winter-wizard` - check for errors |
| **Port in use** | `lsof -i :8501` - kill existing process |
| **SSL not working** | Check cert paths in nginx.conf, renew if needed |
| **Data not loading** | Verify data files exist: `ls -la reference-dashboard/data/` |
| **Nginx 502 error** | Check if Streamlit running: `docker ps` |

---

## 📈 Next Steps

### Immediately After Deployment

1. **Test all pages:**
   - Welcome page ✓
   - Quick start ✓
   - Data explorer ✓
   - Learning lessons ✓
   - Export ✓
   - Completion ✓

2. **Verify data:**
   - All 6 datasets load
   - Visualizations work
   - Export downloads as CSV

3. **Share with students:**
   - Send URL: https://winter.digital-economy.org
   - Include instructions
   - Setup support channel

### Ongoing Maintenance

```bash
# Daily
- Check application logs
- Monitor server resources (CPU, RAM, disk)

# Weekly
- Review error logs
- Check SSL certificate expiry

# Monthly
- Update dependencies
- Backup data
- Security scan

# Quarterly
- Update documentation
- Performance review
- Disaster recovery test
```

---

## 💡 Pro Tips

1. **Setup monitoring:** Use Datadog, New Relic, or similar
2. **Enable backups:** Script daily CSV backups to external storage
3. **Setup alerts:** Get notified if app goes down
4. **Plan for scale:** Add load balancer if traffic grows
5. **Security:** Keep dependencies updated regularly
6. **Testing:** Test deployment to staging first

---

## 🎓 For Students

After deployment, students access via:

```
https://winter.digital-economy.org
```

Features they'll see:
- 🎯 Welcome with learning path selection
- ⚡ 5-minute quick start
- 📊 Interactive data explorer
- 📖 Educational lessons
- 💾 Export & reporting
- 🎓 Completion screen

---

## 📞 Contact & Support

For deployment issues:

1. **Check Documentation:** DEPLOYMENT_GUIDE.md
2. **Review Logs:** `docker logs winter-wizard`
3. **Test Connectivity:** `curl https://winter.digital-economy.org`
4. **Contact DevOps:** [Your contact info]

---

## ✨ Summary

You have everything ready to deploy a production-grade educational platform to winter.digital-economy.org. Choose your deployment option above and follow the steps. The entire process should take 5-15 minutes depending on your chosen method.

**Estimated Timeline:**
- **Streamlit Cloud:** 5 min setup + waiting for build
- **Docker:** 10 min setup + DNS propagation
- **Manual:** 15 min setup + DNS propagation

**All files are production-ready. Let's go! 🚀**

---

*Last Updated: November 25, 2025*  
*Deployment Status: READY FOR PRODUCTION*
