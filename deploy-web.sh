#!/bin/bash
#
# Workshop Webpage Deployment Script
# Deploys the web landing page to winter.digital-economy.org
#

set -e  # Exit on error

echo "🌐 Workshop Webpage Deployment Script"
echo "======================================"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if web directory exists
if [ ! -d "web" ]; then
    echo -e "${RED}❌ Error: web/ directory not found${NC}"
    echo "Please run this script from the repository root"
    exit 1
fi

echo "📁 Found web directory"
echo ""

# Show deployment options
echo "Select deployment method:"
echo ""
echo "1) Deploy to Server via SSH"
echo "2) Deploy to Server via RSYNC"
echo "3) Test Locally (Python HTTP Server)"
echo "4) Test Locally (PHP Server)"
echo "5) Show deployment instructions only"
echo ""
read -p "Enter your choice (1-5): " choice

case $choice in
    1)
        echo ""
        read -p "Enter server address (e.g., user@winter.digital-economy.org): " server
        read -p "Enter web root path (e.g., /var/www/html): " webroot

        echo ""
        echo "🚀 Deploying to ${server}:${webroot}"

        # Create temp directory on server
        ssh "$server" "mkdir -p /tmp/winter-web-deploy"

        # Copy files to server
        scp -r web/* "$server:/tmp/winter-web-deploy/"

        # Move files to web root
        ssh "$server" "sudo cp -r /tmp/winter-web-deploy/* ${webroot}/ && \
                       sudo chown -R www-data:www-data ${webroot} && \
                       sudo chmod -R 755 ${webroot} && \
                       rm -rf /tmp/winter-web-deploy"

        echo ""
        echo -e "${GREEN}✅ Deployment complete!${NC}"
        echo ""
        echo "🌐 Visit: https://winter.digital-economy.org"
        ;;

    2)
        echo ""
        read -p "Enter server address (e.g., user@winter.digital-economy.org): " server
        read -p "Enter web root path (e.g., /var/www/html): " webroot

        echo ""
        echo "🚀 Syncing files to ${server}:${webroot}"

        # Use rsync for efficient transfer
        rsync -avz --delete web/ "$server:${webroot}/"

        # Fix permissions
        ssh "$server" "sudo chown -R www-data:www-data ${webroot} && \
                       sudo chmod -R 755 ${webroot}"

        echo ""
        echo -e "${GREEN}✅ Sync complete!${NC}"
        echo ""
        echo "🌐 Visit: https://winter.digital-economy.org"
        ;;

    3)
        echo ""
        echo "🧪 Starting local test server..."
        echo ""
        echo -e "${YELLOW}📍 Local URL: http://localhost:8000${NC}"
        echo ""
        echo "Press Ctrl+C to stop the server"
        echo ""

        cd web
        python3 -m http.server 8000
        ;;

    4)
        echo ""
        echo "🧪 Starting local PHP server..."
        echo ""
        echo -e "${YELLOW}📍 Local URL: http://localhost:8000${NC}"
        echo ""
        echo "Press Ctrl+C to stop the server"
        echo ""

        cd web
        php -S localhost:8000
        ;;

    5)
        echo ""
        echo "📖 Opening deployment guide..."
        echo ""

        if [ -f "WEB_DEPLOYMENT_GUIDE.md" ]; then
            cat WEB_DEPLOYMENT_GUIDE.md
        else
            echo -e "${RED}❌ WEB_DEPLOYMENT_GUIDE.md not found${NC}"
            echo ""
            echo "Quick deployment options:"
            echo ""
            echo "Option 1: GitHub Pages"
            echo "  - Go to: https://github.com/hnuseibeh/winter-university/settings/pages"
            echo "  - Select branch: main"
            echo "  - Select folder: /web"
            echo "  - Save"
            echo ""
            echo "Option 2: Server Deployment"
            echo "  ssh user@winter.digital-economy.org"
            echo "  cd /var/www/html"
            echo "  git clone https://github.com/hnuseibeh/winter-university.git"
            echo "  cp -r winter-university/web/* ."
            echo "  sudo chown -R www-data:www-data ."
            echo "  sudo chmod -R 755 ."
            echo ""
        fi
        ;;

    *)
        echo -e "${RED}❌ Invalid choice${NC}"
        exit 1
        ;;
esac

echo ""
echo "✨ Done!"
