#!/bin/bash
#
# Complete Workshop Deployment Script
# Deploys all components: landing page, wizard, dashboard, and examples
#

set -e  # Exit on error

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}"
echo "╔═══════════════════════════════════════════════════╗"
echo "║  Winter University 2025 - Complete Deployment    ║"
echo "║  Workshop 3: Economic & Social Crises             ║"
echo "╚═══════════════════════════════════════════════════╝"
echo -e "${NC}"
echo ""

# Check prerequisites
check_prerequisites() {
    echo "🔍 Checking prerequisites..."

    if [ ! -f "wizard.py" ]; then
        echo -e "${RED}❌ Error: wizard.py not found. Run from repository root.${NC}"
        exit 1
    fi

    if [ ! -d "web" ]; then
        echo -e "${RED}❌ Error: web/ directory not found.${NC}"
        exit 1
    fi

    echo -e "${GREEN}✅ Prerequisites OK${NC}"
    echo ""
}

# Show deployment menu
show_menu() {
    echo "Select deployment type:"
    echo ""
    echo -e "${BLUE}═══ Production Deployments ═══${NC}"
    echo "1) 🐳 Complete Docker Deployment (Recommended)"
    echo "   └─ Deploy ALL components with Docker + Nginx"
    echo ""
    echo "2) 🌐 Static Site Only (Server)"
    echo "   └─ Deploy workshop landing page to web server"
    echo ""
    echo "3) ☁️  Mixed: Static + Streamlit Cloud"
    echo "   └─ Landing page on server, apps on Streamlit Cloud"
    echo ""
    echo -e "${BLUE}═══ Testing & Development ═══${NC}"
    echo "4) 🧪 Test All Components Locally"
    echo "   └─ Run everything on localhost"
    echo ""
    echo "5) 🧪 Test with Docker Locally"
    echo "   └─ Test Docker setup before production"
    echo ""
    echo -e "${BLUE}═══ Information ═══${NC}"
    echo "6) 📖 Show Deployment Guide"
    echo "7) ℹ️  Show Server Requirements"
    echo ""
    read -p "Enter your choice (1-7): " choice
}

# Option 1: Complete Docker Deployment
deploy_docker_complete() {
    echo ""
    echo -e "${YELLOW}🐳 Complete Docker Deployment${NC}"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""

    read -p "Server address (e.g., user@winter.digital-economy.org): " server

    echo ""
    echo "📤 Step 1/5: Syncing files to server..."
    rsync -avz --progress \
        --exclude '.git' \
        --exclude '__pycache__' \
        --exclude '*.pyc' \
        --exclude '.DS_Store' \
        --exclude 'node_modules' \
        . "$server:/opt/winter-university/"

    echo ""
    echo "🐳 Step 2/5: Building Docker images..."
    ssh "$server" "cd /opt/winter-university && sudo docker-compose -f docker-compose-complete.yml build"

    echo ""
    echo "🛑 Step 3/5: Stopping old containers..."
    ssh "$server" "cd /opt/winter-university && sudo docker-compose -f docker-compose-complete.yml down" || true

    echo ""
    echo "🚀 Step 4/5: Starting all services..."
    ssh "$server" "cd /opt/winter-university && sudo docker-compose -f docker-compose-complete.yml up -d"

    echo ""
    echo "⏳ Step 5/5: Waiting for services to be ready..."
    sleep 10

    echo ""
    echo "🔍 Checking service status..."
    ssh "$server" "cd /opt/winter-university && sudo docker-compose -f docker-compose-complete.yml ps"

    echo ""
    echo -e "${GREEN}✅ Deployment complete!${NC}"
    echo ""
    echo "📍 Your workshop is now accessible at:"
    echo ""
    echo -e "   ${BLUE}🏠 Landing Page:${NC}    http://winter.digital-economy.org"
    echo -e "   ${BLUE}🧙 Wizard:${NC}          http://winter.digital-economy.org/wizard"
    echo -e "   ${BLUE}📊 Dashboard:${NC}       http://winter.digital-economy.org/dashboard"
    echo -e "   ${BLUE}📚 Examples:${NC}        http://winter.digital-economy.org/examples"
    echo ""
    echo -e "${YELLOW}⚠️  Next steps:${NC}"
    echo "1. Configure DNS: Point winter.digital-economy.org to your server IP"
    echo "2. Get SSL certificate:"
    echo "   ssh $server"
    echo "   sudo certbot certonly --nginx -d winter.digital-economy.org"
    echo "3. Update nginx-complete.conf with SSL paths and restart nginx"
    echo ""
}

# Option 2: Static Site Only
deploy_static_only() {
    echo ""
    echo -e "${YELLOW}🌐 Static Site Deployment${NC}"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""

    read -p "Server address: " server
    read -p "Web root path (default: /var/www/html): " webroot
    webroot=${webroot:-/var/www/html}

    echo ""
    echo "📤 Deploying landing page to $server:$webroot"

    rsync -avz --progress web/ "$server:$webroot/"

    echo ""
    echo "🔒 Setting permissions..."
    ssh "$server" "sudo chown -R www-data:www-data $webroot && sudo chmod -R 755 $webroot"

    echo ""
    echo -e "${GREEN}✅ Static site deployed!${NC}"
    echo ""
    echo "📍 Landing page: https://winter.digital-economy.org"
    echo ""
    echo -e "${YELLOW}⚠️  Note:${NC} Streamlit apps need to be deployed separately"
    echo "   - Use Streamlit Cloud (Option 3), or"
    echo "   - Use Complete Docker Deployment (Option 1)"
    echo ""
}

# Option 3: Mixed Deployment
deploy_mixed() {
    echo ""
    echo -e "${YELLOW}☁️  Mixed Deployment${NC}"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""

    echo "This will:"
    echo "1. Deploy static landing page to your server"
    echo "2. Show instructions for deploying apps to Streamlit Cloud"
    echo ""
    read -p "Continue? (y/n): " confirm

    if [ "$confirm" != "y" ]; then
        echo "Cancelled."
        return
    fi

    # Deploy static site
    read -p "Server address: " server
    read -p "Web root (default: /var/www/html): " webroot
    webroot=${webroot:-/var/www/html}

    rsync -avz --progress web/ "$server:$webroot/"
    ssh "$server" "sudo chown -R www-data:www-data $webroot && sudo chmod -R 755 $webroot"

    echo ""
    echo -e "${GREEN}✅ Landing page deployed!${NC}"
    echo ""
    echo -e "${YELLOW}📋 Next: Deploy Streamlit Apps to Streamlit Cloud${NC}"
    echo ""
    echo "1. Go to: https://streamlit.io/cloud"
    echo "2. Sign in with GitHub"
    echo ""
    echo "Deploy Wizard:"
    echo "   - New app → Repository: hnuseibeh/winter-university"
    echo "   - Main file: wizard.py"
    echo "   - App URL: winter-wizard"
    echo ""
    echo "Deploy Reference Dashboard:"
    echo "   - New app → Repository: hnuseibeh/winter-university"
    echo "   - Main file: reference-dashboard/app.py"
    echo "   - App URL: winter-dashboard"
    echo ""
    echo "Deploy Reference Examples:"
    echo "   - New app → Repository: hnuseibeh/winter-university"
    echo "   - Main file: reference-examples/app.py"
    echo "   - App URL: winter-examples"
    echo ""
    echo "Then update links in web/index.html to point to your Streamlit apps"
    echo ""
}

# Option 4: Test Locally
test_locally() {
    echo ""
    echo -e "${YELLOW}🧪 Testing All Components Locally${NC}"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""

    echo "Starting all services in background..."
    echo ""
    echo "Services will be available at:"
    echo -e "   ${BLUE}Landing Page:${NC}  http://localhost:8000"
    echo -e "   ${BLUE}Wizard:${NC}        http://localhost:8501"
    echo -e "   ${BLUE}Dashboard:${NC}     http://localhost:8502"
    echo -e "   ${BLUE}Examples:${NC}      http://localhost:8503"
    echo ""
    echo -e "${YELLOW}Press Ctrl+C to stop all servers${NC}"
    echo ""

    # Start services
    cd web && python3 -m http.server 8000 > /dev/null 2>&1 &
    PID1=$!

    cd .. && streamlit run wizard.py --server.port 8501 > /dev/null 2>&1 &
    PID2=$!

    cd reference-dashboard && streamlit run app.py --server.port 8502 > /dev/null 2>&1 &
    PID3=$!

    cd ../reference-examples && streamlit run app.py --server.port 8503 > /dev/null 2>&1 &
    PID4=$!

    cd ..

    # Wait for services to start
    sleep 5

    echo -e "${GREEN}✅ All services started!${NC}"
    echo ""
    echo "Opening in browser..."

    # Try to open in browser
    if command -v open > /dev/null; then
        open http://localhost:8000
    elif command -v xdg-open > /dev/null; then
        xdg-open http://localhost:8000
    fi

    # Cleanup function
    cleanup() {
        echo ""
        echo "Stopping all services..."
        kill $PID1 $PID2 $PID3 $PID4 2>/dev/null || true
        echo -e "${GREEN}✅ All services stopped${NC}"
        exit 0
    }

    trap cleanup EXIT INT TERM

    # Wait
    wait
}

# Option 5: Test with Docker
test_docker() {
    echo ""
    echo -e "${YELLOW}🐳 Testing Docker Setup Locally${NC}"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""

    if ! command -v docker > /dev/null; then
        echo -e "${RED}❌ Docker not found. Please install Docker first.${NC}"
        return
    fi

    echo "Building and starting Docker containers..."
    docker-compose -f docker-compose-complete.yml build
    docker-compose -f docker-compose-complete.yml up -d

    echo ""
    echo "⏳ Waiting for services to start..."
    sleep 10

    echo ""
    docker-compose -f docker-compose-complete.yml ps

    echo ""
    echo -e "${GREEN}✅ Docker services started!${NC}"
    echo ""
    echo "Access at:"
    echo "   http://localhost         (Landing page)"
    echo "   http://localhost/wizard  (Wizard)"
    echo "   http://localhost/dashboard (Dashboard)"
    echo "   http://localhost/examples  (Examples)"
    echo ""
    echo "View logs: docker-compose -f docker-compose-complete.yml logs -f"
    echo "Stop: docker-compose -f docker-compose-complete.yml down"
    echo ""
}

# Option 6: Show guide
show_guide() {
    echo ""
    if [ -f "COMPLETE_DEPLOYMENT_GUIDE.md" ]; then
        less COMPLETE_DEPLOYMENT_GUIDE.md
    else
        echo -e "${RED}❌ COMPLETE_DEPLOYMENT_GUIDE.md not found${NC}"
    fi
}

# Option 7: Show requirements
show_requirements() {
    echo ""
    echo -e "${BLUE}═══ Server Requirements ═══${NC}"
    echo ""
    echo "Minimum:"
    echo "  • 2 CPU cores"
    echo "  • 2 GB RAM"
    echo "  • 10 GB storage"
    echo "  • Ubuntu 20.04+ or similar"
    echo ""
    echo "Recommended:"
    echo "  • 4 CPU cores"
    echo "  • 8 GB RAM"
    echo "  • 50 GB SSD storage"
    echo ""
    echo "Required Software:"
    echo "  • Docker & Docker Compose (for Option 1, 5)"
    echo "  • Nginx (for Option 2, 3)"
    echo "  • Python 3.8+ (for Option 4)"
    echo "  • Git"
    echo ""
    echo "Network:"
    echo "  • Ports 80, 443 open"
    echo "  • Domain pointing to server"
    echo ""
}

# Main script
main() {
    check_prerequisites
    show_menu

    case $choice in
        1) deploy_docker_complete ;;
        2) deploy_static_only ;;
        3) deploy_mixed ;;
        4) test_locally ;;
        5) test_docker ;;
        6) show_guide ;;
        7) show_requirements ;;
        *)
            echo -e "${RED}❌ Invalid choice${NC}"
            exit 1
            ;;
    esac

    echo ""
    echo -e "${GREEN}✨ Done!${NC}"
}

# Run main
main
