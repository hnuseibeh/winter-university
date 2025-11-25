# 🚀 Complete Deployment Guide
**Deploy Everything to winter.digital-economy.org**

---

## 📦 What You're Deploying

This guide covers deploying ALL workshop components:

1. **Workshop Landing Page** (Static HTML)
   - Location: `/web/`
   - URL: `https://winter.digital-economy.org`

2. **Interactive Wizard** (Streamlit App)
   - Location: `/wizard.py`
   - URL: `https://winter.digital-economy.org/wizard` or `https://wizard.winter.digital-economy.org`

3. **Reference Dashboard** (Streamlit App)
   - Location: `/reference-dashboard/`
   - URL: `https://winter.digital-economy.org/dashboard`

4. **Reference Examples** (Streamlit App)
   - Location: `/reference-examples/`
   - URL: `https://winter.digital-economy.org/examples`

---

## 🎯 Deployment Architecture

```
winter.digital-economy.org
├── /                       → Workshop landing page (static HTML)
├── /wizard                 → Interactive wizard (Streamlit)
├── /dashboard              → Reference dashboard (Streamlit)
└── /examples               → Reference examples (Streamlit)
```

---

## 🚀 Option 1: All-in-One Docker Deployment (Recommended)

Deploy everything with Docker on your server.

### Prerequisites
- Server with Docker installed
- SSH access to winter.digital-economy.org
- Domain pointing to server IP

### Step 1: SSH into Your Server
```bash
ssh user@winter.digital-economy.org
```

### Step 2: Clone Repository
```bash
cd /opt
sudo git clone https://github.com/hnuseibeh/winter-university.git
cd winter-university
```

### Step 3: Run Docker Deployment
```bash
sudo docker-compose up -d
```

This will start:
- **Nginx** web server (port 80/443) serving the landing page
- **Wizard** (port 8501)
- **Reference Dashboard** (port 8502)
- **Reference Examples** (port 8503)

### Step 4: Configure Nginx Reverse Proxy
The included `nginx.conf` will route:
- `/` → Static HTML landing page
- `/wizard` → Streamlit wizard (port 8501)
- `/dashboard` → Reference dashboard (port 8502)
- `/examples` → Reference examples (port 8503)

### Step 5: Get SSL Certificate
```bash
sudo certbot certonly --nginx \
  -d winter.digital-economy.org \
  -d www.winter.digital-economy.org
```

### Step 6: Verify Deployment
```bash
curl https://winter.digital-economy.org
curl https://winter.digital-economy.org/wizard
curl https://winter.digital-economy.org/dashboard
curl https://winter.digital-economy.org/examples
```

---

## 🚀 Option 2: Mixed Deployment (Static + Streamlit Cloud)

Deploy landing page on your server, Streamlit apps on Streamlit Cloud.

### Part A: Deploy Landing Page to Server

```bash
# SSH to server
ssh user@winter.digital-economy.org

# Navigate to web root
cd /var/www/html

# Clone and deploy
git clone https://github.com/hnuseibeh/winter-university.git
cp -r winter-university/web/* .
sudo chown -R www-data:www-data .
sudo chmod -R 755 .
```

### Part B: Deploy Streamlit Apps to Streamlit Cloud

1. **Deploy Wizard:**
   - Go to https://streamlit.io/cloud
   - New App → Repository: `hnuseibeh/winter-university`
   - Main file: `wizard.py`
   - App URL: `winter-wizard`

2. **Deploy Reference Dashboard:**
   - New App → Repository: `hnuseibeh/winter-university`
   - Main file: `reference-dashboard/app.py`
   - App URL: `winter-dashboard`

3. **Deploy Reference Examples:**
   - New App → Repository: `hnuseibeh/winter-university`
   - Main file: `reference-examples/app.py`
   - App URL: `winter-examples`

### Part C: Update Landing Page Links

Edit `web/index.html` to point to your Streamlit apps:
```html
<!-- Update links to Streamlit Cloud URLs -->
<a href="https://winter-wizard.streamlit.app">Interactive Wizard</a>
<a href="https://winter-dashboard.streamlit.app">Reference Dashboard</a>
<a href="https://winter-examples.streamlit.app">Reference Examples</a>
```

---

## 🚀 Option 3: GitHub Pages + Streamlit Cloud (No Server Needed)

Deploy everything without managing a server.

### Step 1: Deploy Landing Page to GitHub Pages
1. Go to https://github.com/hnuseibeh/winter-university/settings/pages
2. Source: `main` branch, `/web` folder
3. Click Save
4. Site will be at: `https://hnuseibeh.github.io/winter-university/`

### Step 2: Configure Custom Domain
1. In GitHub Pages settings, add: `winter.digital-economy.org`
2. Add DNS CNAME record:
   ```
   Type: CNAME
   Name: winter
   Value: hnuseibeh.github.io
   TTL: 3600
   ```

### Step 3: Deploy Streamlit Apps (see Option 2, Part B above)

### Step 4: Update Landing Page Links (see Option 2, Part C above)

---

## 🐳 Enhanced Docker Compose Configuration

Create enhanced `docker-compose.yml` for complete deployment:

```yaml
version: '3.8'

services:
  # Nginx Web Server & Reverse Proxy
  nginx:
    image: nginx:alpine
    container_name: winter-nginx
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./web:/usr/share/nginx/html
      - ./nginx.conf:/etc/nginx/nginx.conf
      - /etc/letsencrypt:/etc/letsencrypt
    depends_on:
      - wizard
      - dashboard
      - examples
    restart: unless-stopped

  # Interactive Wizard
  wizard:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: winter-wizard
    command: streamlit run wizard.py --server.port=8501 --server.address=0.0.0.0
    expose:
      - "8501"
    volumes:
      - ./:/app
    restart: unless-stopped

  # Reference Dashboard
  dashboard:
    build:
      context: ./reference-dashboard
      dockerfile: ../Dockerfile
    container_name: winter-dashboard
    command: streamlit run app.py --server.port=8502 --server.address=0.0.0.0
    working_dir: /app/reference-dashboard
    expose:
      - "8502"
    volumes:
      - ./reference-dashboard:/app/reference-dashboard
    restart: unless-stopped

  # Reference Examples
  examples:
    build:
      context: ./reference-examples
      dockerfile: ../Dockerfile
    container_name: winter-examples
    command: streamlit run app.py --server.port=8503 --server.address=0.0.0.0
    working_dir: /app/reference-examples
    expose:
      - "8503"
    volumes:
      - ./reference-examples:/app/reference-examples
    restart: unless-stopped
```

---

## 🔧 Enhanced Nginx Configuration

Create comprehensive `nginx-complete.conf`:

```nginx
events {
    worker_connections 1024;
}

http {
    include mime.types;
    default_type application/octet-stream;

    # Rate limiting
    limit_req_zone $binary_remote_addr zone=mylimit:10m rate=10r/s;

    # Upstream servers (Streamlit apps)
    upstream wizard {
        server wizard:8501;
    }

    upstream dashboard {
        server dashboard:8502;
    }

    upstream examples {
        server examples:8503;
    }

    # Main server block
    server {
        listen 80;
        server_name winter.digital-economy.org www.winter.digital-economy.org;

        # Redirect HTTP to HTTPS
        return 301 https://$server_name$request_uri;
    }

    server {
        listen 443 ssl http2;
        server_name winter.digital-economy.org www.winter.digital-economy.org;

        # SSL configuration
        ssl_certificate /etc/letsencrypt/live/winter.digital-economy.org/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/winter.digital-economy.org/privkey.pem;

        # Security headers
        add_header X-Frame-Options "SAMEORIGIN" always;
        add_header X-Content-Type-Options "nosniff" always;
        add_header X-XSS-Protection "1; mode=block" always;

        # Static landing page (root)
        location / {
            root /usr/share/nginx/html;
            index index.html;
            try_files $uri $uri/ /index.html;
        }

        # Interactive Wizard
        location /wizard {
            limit_req zone=mylimit burst=20 nodelay;

            proxy_pass http://wizard;
            proxy_http_version 1.1;

            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;

            proxy_read_timeout 86400;
            proxy_buffering off;
        }

        # Reference Dashboard
        location /dashboard {
            limit_req zone=mylimit burst=20 nodelay;

            proxy_pass http://dashboard;
            proxy_http_version 1.1;

            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;

            proxy_read_timeout 86400;
            proxy_buffering off;
        }

        # Reference Examples
        location /examples {
            limit_req zone=mylimit burst=20 nodelay;

            proxy_pass http://examples;
            proxy_http_version 1.1;

            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;

            proxy_read_timeout 86400;
            proxy_buffering off;
        }

        # Static assets
        location /assets {
            root /usr/share/nginx/html;
            expires 1y;
            add_header Cache-Control "public, immutable";
        }
    }
}
```

---

## 📋 Complete Deployment Script

Create `deploy-complete.sh`:

```bash
#!/bin/bash
# Complete deployment script for winter.digital-economy.org

set -e

echo "🚀 Complete Workshop Deployment"
echo "================================"
echo ""

# Check if we're in the right directory
if [ ! -f "wizard.py" ]; then
    echo "❌ Error: Please run from repository root"
    exit 1
fi

echo "Select deployment type:"
echo "1) Deploy to server (Docker)"
echo "2) Deploy to server (Manual)"
echo "3) Deploy landing page only"
echo "4) Test locally"
echo ""
read -p "Enter choice (1-4): " choice

case $choice in
    1)
        read -p "Server address: " server

        echo "📤 Deploying via Docker..."

        # Copy files to server
        rsync -avz --exclude '.git' --exclude '__pycache__' . "$server:/opt/winter-university/"

        # Deploy with Docker
        ssh "$server" "cd /opt/winter-university && \
                       sudo docker-compose down && \
                       sudo docker-compose build && \
                       sudo docker-compose up -d"

        echo "✅ Docker deployment complete!"
        echo ""
        echo "🌐 Landing page: https://winter.digital-economy.org"
        echo "🧙 Wizard: https://winter.digital-economy.org/wizard"
        echo "📊 Dashboard: https://winter.digital-economy.org/dashboard"
        echo "📚 Examples: https://winter.digital-economy.org/examples"
        ;;

    2)
        read -p "Server address: " server

        echo "📤 Manual deployment..."

        # Deploy static site
        ssh "$server" "mkdir -p /var/www/winter.digital-economy.org"
        rsync -avz web/ "$server:/var/www/winter.digital-economy.org/"

        echo "✅ Static site deployed!"
        echo "⚠️  Please deploy Streamlit apps separately or use Option 1"
        ;;

    3)
        read -p "Server address: " server

        echo "📤 Deploying landing page only..."
        rsync -avz web/ "$server:/var/www/html/"
        ssh "$server" "sudo chown -R www-data:www-data /var/www/html && \
                       sudo chmod -R 755 /var/www/html"

        echo "✅ Landing page deployed!"
        ;;

    4)
        echo "🧪 Starting local test servers..."
        echo ""
        echo "Starting services on:"
        echo "  - Landing page: http://localhost:8000"
        echo "  - Wizard: http://localhost:8501"
        echo "  - Dashboard: http://localhost:8502"
        echo "  - Examples: http://localhost:8503"
        echo ""
        echo "Press Ctrl+C to stop all servers"

        # Start in background
        cd web && python3 -m http.server 8000 &
        PID1=$!

        cd .. && streamlit run wizard.py --server.port 8501 &
        PID2=$!

        cd reference-dashboard && streamlit run app.py --server.port 8502 &
        PID3=$!

        cd ../reference-examples && streamlit run app.py --server.port 8503 &
        PID4=$!

        # Wait for Ctrl+C
        trap "kill $PID1 $PID2 $PID3 $PID4" EXIT
        wait
        ;;

    *)
        echo "❌ Invalid choice"
        exit 1
        ;;
esac

echo ""
echo "✨ Deployment complete!"
```

---

## ✅ Post-Deployment Checklist

- [ ] Landing page loads at `https://winter.digital-economy.org`
- [ ] Wizard works at `/wizard` or subdomain
- [ ] Dashboard works at `/dashboard` or subdomain
- [ ] Examples work at `/examples` or subdomain
- [ ] All images and assets load correctly
- [ ] Language switcher works
- [ ] GitHub links work
- [ ] Mobile responsive design works
- [ ] SSL certificate is valid
- [ ] All Streamlit apps function properly

---

## 🔄 Updating After Deployment

### Update via Git (Docker deployment)
```bash
ssh user@winter.digital-economy.org
cd /opt/winter-university
sudo git pull origin main
sudo docker-compose restart
```

### Update Static Site Only
```bash
rsync -avz web/ user@winter.digital-economy.org:/var/www/html/
```

---

## 🆘 Troubleshooting

### Streamlit Apps Not Loading
```bash
# Check containers are running
docker ps

# View logs
docker logs winter-wizard
docker logs winter-dashboard
docker logs winter-examples

# Restart specific service
docker-compose restart wizard
```

### Nginx Errors
```bash
# Test configuration
sudo nginx -t

# View error logs
sudo tail -f /var/log/nginx/error.log

# Restart nginx
sudo systemctl restart nginx
```

### Permission Issues
```bash
sudo chown -R www-data:www-data /var/www/html
sudo chmod -R 755 /var/www/html
```

---

## 📊 Complete URL Structure

After deployment, your workshop will be accessible at:

| Component | URL |
|-----------|-----|
| **Landing Page** | https://winter.digital-economy.org |
| **Interactive Wizard** | https://winter.digital-economy.org/wizard |
| **Reference Dashboard** | https://winter.digital-economy.org/dashboard |
| **Reference Examples** | https://winter.digital-economy.org/examples |
| **GitHub Repository** | https://github.com/hnuseibeh/winter-university |

---

*Last Updated: November 25, 2025*
*Status: READY FOR COMPLETE DEPLOYMENT*
