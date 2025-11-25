# 🚀 Deployment Guide: winter.digital-economy.org

**Last Updated:** November 25, 2025  
**Status:** Production Ready

---

## Table of Contents

1. [Quick Deployment](#quick-deployment)
2. [Architecture Overview](#architecture-overview)
3. [Server Requirements](#server-requirements)
4. [Deployment Options](#deployment-options)
5. [Configuration](#configuration)
6. [Monitoring & Maintenance](#monitoring--maintenance)
7. [Troubleshooting](#troubleshooting)

---

## Quick Deployment

### Option 1: Streamlit Cloud (Fastest - 5 minutes)

```bash
# 1. Push to GitHub
git add .
git commit -m "Ready for production"
git push origin main

# 2. Go to https://streamlit.io/cloud
# 3. Connect GitHub repository
# 4. Deploy with:
#    - Repository: your-repo
#    - Branch: main
#    - Main file path: wizard.py
#    - URL: winter.digital-economy.org (via DNS)
```

**Pros:** Free, auto-updates, handles SSL  
**Cons:** Limited customization, shared infrastructure

### Option 2: Docker + Nginx (Recommended - 30 minutes)

```bash
# 1. Build Docker image
docker build -t winter-wizard:latest .

# 2. Push to registry (e.g., Docker Hub)
docker tag winter-wizard:latest your-registry/winter-wizard:latest
docker push your-registry/winter-wizard:latest

# 3. Deploy on server
ssh user@winter.digital-economy.org
docker pull your-registry/winter-wizard:latest
docker run -d -p 8501:8501 --name winter-wizard your-registry/winter-wizard:latest

# 4. Configure Nginx reverse proxy (see below)
```

**Pros:** Full control, scalable, can host multiple apps  
**Cons:** Requires server management

### Option 3: Traditional Server (1-2 hours)

```bash
# SSH into server
ssh user@winter.digital-economy.org

# Clone repository
git clone https://github.com/your-org/winter.git
cd winter

# Install dependencies
pip install -r requirements.txt

# Run with process manager
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 'streamlit_app:app'

# Or use systemd (see below)
```

---

## Architecture Overview

```
winter.digital-economy.org
│
├── Web Interface (index.html)
│   └── Landing page with tool links
│
├── Wizard Application (wizard.py)
│   ├── Welcome & onboarding
│   ├── Quick start
│   ├── Data explorer
│   ├── Learning lessons
│   └── Export & reporting
│
├── Reference Dashboard
│   └── 4-page research dashboard
│
├── Reference Examples
│   └── 8-page comprehensive examples
│
└── Data Layer
    └── CSV files (6 datasets)
        ├── humanitarian_indicators.csv
        ├── climate_vulnerability_index.csv
        ├── agricultural_stress.csv
        ├── crisis_timeline.csv
        ├── sentiment_index.csv
        └── news_summary.csv
```

---

## Server Requirements

### Minimum Requirements
- **OS:** Ubuntu 20.04 LTS or later, macOS, Windows Server
- **CPU:** 2 cores
- **RAM:** 2 GB minimum, 4 GB recommended
- **Storage:** 10 GB (for code, data, and logs)
- **Python:** 3.8 or higher

### Recommended Specifications
- **OS:** Ubuntu 22.04 LTS
- **CPU:** 4+ cores
- **RAM:** 8 GB
- **Storage:** 50 GB SSD
- **Python:** 3.10+
- **Web Server:** Nginx (reverse proxy)

### Dependencies
```bash
# System packages
sudo apt-get update
sudo apt-get install -y \
    python3.10 \
    python3-pip \
    python3-venv \
    git \
    nginx \
    certbot \
    python3-certbot-nginx \
    supervisor
```

---

## Deployment Options

### Option 1: Streamlit Cloud (Free Tier)

**Best for:** Academic/non-profit projects, quick launch

**Steps:**

1. Create GitHub repository:
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/your-org/winter.git
git push -u origin main
```

2. Go to https://streamlit.io/cloud
3. Sign in with GitHub
4. Click "New app"
5. Select repository, branch, and main file (wizard.py)
6. Deploy!
7. Custom domain: Update DNS to point to Streamlit URL

**Configuration file:** `.streamlit/config.toml`
```toml
[server]
port = 8501
headless = true
runOnSave = true

[browser]
gatherUsageStats = false

[theme]
primaryColor = "#1f77b4"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
font = "sans serif"
```

---

### Option 2: Docker + Nginx (Production)

**Best for:** Production deployments, custom domains, full control

#### Step 1: Create Dockerfile

Already created at: `Dockerfile`

```dockerfile
FROM python:3.10-slim

WORKDIR /app

# Copy files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose port
EXPOSE 8501

# Health check
HEALTHCHECK CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8501/_stcore/health').read()"

# Run Streamlit
CMD ["streamlit", "run", "wizard.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

#### Step 2: Build and Push

```bash
# Build
docker build -t winter-wizard:v1.0 .

# Tag for registry
docker tag winter-wizard:v1.0 registry.example.com/winter-wizard:v1.0

# Push
docker push registry.example.com/winter-wizard:v1.0
```

#### Step 3: Deploy with Docker Compose

Create `docker-compose.yml`:

```yaml
version: '3.8'

services:
  wizard:
    image: registry.example.com/winter-wizard:v1.0
    container_name: winter-wizard
    ports:
      - "8501:8501"
    volumes:
      - ./reference-dashboard/data:/app/reference-dashboard/data:ro
      - ./logs:/app/logs
    environment:
      - STREAMLIT_SERVER_PORT=8501
      - STREAMLIT_SERVER_ADDRESS=0.0.0.0
      - STREAMLIT_LOGGER_LEVEL=info
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8501/_stcore/health"]
      interval: 30s
      timeout: 10s
      retries: 3
```

Deploy:
```bash
docker-compose up -d
```

#### Step 4: Nginx Reverse Proxy

Create `/etc/nginx/sites-available/winter`:

```nginx
upstream streamlit_app {
    server localhost:8501;
}

# Redirect HTTP to HTTPS
server {
    listen 80;
    server_name winter.digital-economy.org;
    
    location / {
        return 301 https://$server_name$request_uri;
    }
}

# Main HTTPS server
server {
    listen 443 ssl http2;
    server_name winter.digital-economy.org;
    
    # SSL certificates (via Let's Encrypt)
    ssl_certificate /etc/letsencrypt/live/winter.digital-economy.org/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/winter.digital-economy.org/privkey.pem;
    
    # Security headers
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-XSS-Protection "1; mode=block" always;
    
    # Gzip compression
    gzip on;
    gzip_types text/plain text/css application/json application/javascript;
    gzip_min_length 1024;
    
    # Proxy settings
    location / {
        proxy_pass http://streamlit_app;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # Timeouts
        proxy_connect_timeout 60s;
        proxy_send_timeout 60s;
        proxy_read_timeout 60s;
    }
    
    # Static files (if using external storage)
    location /static/ {
        alias /var/www/winter/static/;
        expires 30d;
    }
}
```

Enable and restart:
```bash
sudo ln -s /etc/nginx/sites-available/winter /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

#### Step 5: SSL Certificate (Let's Encrypt)

```bash
sudo certbot certonly --nginx -d winter.digital-economy.org
# Auto-renew
sudo systemctl enable certbot.timer
```

---

### Option 3: Systemd Service (Simple)

Create `/etc/systemd/system/winter-wizard.service`:

```ini
[Unit]
Description=Winter University Wizard
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/opt/winter
ExecStart=/usr/bin/python3 -m streamlit run wizard.py \
    --server.port=8501 \
    --server.address=127.0.0.1 \
    --logger.level=info
Restart=on-failure
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Deploy:
```bash
sudo systemctl daemon-reload
sudo systemctl enable winter-wizard
sudo systemctl start winter-wizard
sudo systemctl status winter-wizard
```

---

## Configuration

### Environment Variables

Create `.env` file in project root:

```bash
# Application
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
STREAMLIT_LOGGER_LEVEL=info

# Data paths
DATA_DIR=/app/reference-dashboard/data

# External services (if needed)
# API_KEY=xxxxx
# SENTRY_DSN=xxxxx
```

### Streamlit Configuration

Create `.streamlit/config.toml`:

```toml
[client]
showErrorDetails = false

[logger]
level = "info"

[server]
port = 8501
headless = true
runOnSave = false
maxUploadSize = 200

[theme]
primaryColor = "#1f77b4"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
font = "sans serif"
```

---

## Monitoring & Maintenance

### Health Checks

```bash
# Check if app is running
curl https://winter.digital-economy.org

# Check specific endpoint
curl https://winter.digital-economy.org/_stcore/health

# Monitor logs
docker logs -f winter-wizard

# Or systemd
journalctl -u winter-wizard -f
```

### Backup Strategy

```bash
# Daily backup script
#!/bin/bash
BACKUP_DIR="/backups/winter"
mkdir -p $BACKUP_DIR
DATE=$(date +%Y%m%d_%H%M%S)

# Backup data
tar -czf $BACKUP_DIR/data_$DATE.tar.gz reference-dashboard/data/
tar -czf $BACKUP_DIR/code_$DATE.tar.gz --exclude=__pycache__ --exclude=.git .

# Keep last 30 days
find $BACKUP_DIR -name "*.tar.gz" -mtime +30 -delete
```

Schedule with cron:
```bash
0 2 * * * /usr/local/bin/backup-winter.sh
```

### Performance Monitoring

```bash
# CPU & Memory
watch -n 1 'ps aux | grep wizard'

# Network connections
netstat -ant | grep 8501

# Disk usage
du -sh /opt/winter

# Docker stats
docker stats winter-wizard
```

### Logging

Configure log rotation:

```bash
# /etc/logrotate.d/winter-wizard
/opt/winter/logs/*.log {
    daily
    rotate 14
    compress
    delaycompress
    notifempty
    create 0640 www-data www-data
    sharedscripts
    postrotate
        systemctl reload winter-wizard > /dev/null 2>&1 || true
    endscript
}
```

---

## Troubleshooting

### Issue: App won't start

```bash
# Check Python version
python3 --version

# Check dependencies
pip list | grep -E 'streamlit|pandas|plotly'

# Test import
python3 -c "import streamlit; print(streamlit.__version__)"

# Run with debug
python3 -m streamlit run wizard.py --logger.level=debug
```

### Issue: Port already in use

```bash
# Find process using port 8501
lsof -i :8501

# Kill it
kill -9 <PID>

# Or use different port
streamlit run wizard.py --server.port=8502
```

### Issue: Data files not found

```bash
# Check if files exist
ls -la reference-dashboard/data/

# Verify permissions
chmod -R 755 reference-dashboard/data/

# Update data path in wizard.py
# Point to correct absolute or relative path
```

### Issue: Nginx 502 Bad Gateway

```bash
# Check Streamlit is running
docker ps | grep winter-wizard
systemctl status winter-wizard

# Check Nginx logs
tail -f /var/log/nginx/error.log

# Verify proxy settings
sudo nginx -T | grep upstream

# Restart both
sudo systemctl restart nginx
docker restart winter-wizard
```

### Issue: High memory usage

```bash
# Monitor memory
docker stats winter-wizard

# Check for memory leaks
ps aux | grep wizard
df -h

# Restart container
docker restart winter-wizard
```

### Issue: SSL certificate issues

```bash
# Check certificate
openssl s_client -connect winter.digital-economy.org:443

# Renew manually
sudo certbot renew --force-renewal -n

# Check expiry
curl -v https://winter.digital-economy.org 2>&1 | grep 'expire'
```

---

## Post-Deployment Checklist

- [ ] Domain points to server (DNS check)
- [ ] SSL certificate installed and valid
- [ ] App accessible at winter.digital-economy.org
- [ ] All pages load correctly
- [ ] Data files accessible
- [ ] Wizard navigation works
- [ ] Export feature functions
- [ ] Logs being written
- [ ] Monitoring configured
- [ ] Backup schedule active
- [ ] Team has access
- [ ] Documentation updated

---

## Support & Resources

### Documentation
- [Streamlit Docs](https://docs.streamlit.io/)
- [Docker Docs](https://docs.docker.com/)
- [Nginx Docs](https://nginx.org/en/docs/)
- [Certbot Docs](https://certbot.eff.org/)

### Contact
- **Administrator:** [Your Name]
- **Email:** [Your Email]
- **Slack Channel:** #winter-deployment

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | Nov 25, 2025 | Initial deployment guide |

