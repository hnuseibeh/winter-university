#!/bin/bash

# Winter University - Deployment Script
# Usage: ./deploy.sh [dev|prod]

set -e

ENVIRONMENT=${1:-dev}
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "🚀 Starting deployment for environment: $ENVIRONMENT"
echo "📁 Project directory: $PROJECT_DIR"

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}✓${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

print_info() {
    echo -e "${YELLOW}ℹ${NC} $1"
}

# 1. Pre-flight checks
print_info "Running pre-flight checks..."

# Check Python
if ! command -v python3 &> /dev/null; then
    print_error "Python 3 not found"
    exit 1
fi
print_status "Python 3 found: $(python3 --version)"

# Check Docker (if using Docker deployment)
if [ "$ENVIRONMENT" = "prod" ]; then
    if ! command -v docker &> /dev/null; then
        print_error "Docker not found (required for production)"
        exit 1
    fi
    print_status "Docker found: $(docker --version)"
    
    if ! command -v docker-compose &> /dev/null; then
        print_error "Docker Compose not found"
        exit 1
    fi
    print_status "Docker Compose found: $(docker-compose --version)"
fi

# 2. Setup Python environment
print_info "Setting up Python environment..."

# Create virtual environment
if [ ! -d "$PROJECT_DIR/venv" ]; then
    python3 -m venv "$PROJECT_DIR/venv"
    print_status "Virtual environment created"
else
    print_status "Virtual environment already exists"
fi

# Activate venv
source "$PROJECT_DIR/venv/bin/activate"
print_status "Virtual environment activated"

# 3. Install dependencies
print_info "Installing dependencies..."
pip install --upgrade pip setuptools wheel > /dev/null 2>&1
pip install -r "$PROJECT_DIR/requirements.txt" > /dev/null 2>&1
print_status "Dependencies installed"

# 4. Verify application
print_info "Verifying application..."
python3 -m py_compile "$PROJECT_DIR/wizard.py"
print_status "Application syntax OK"

# Check data files
if [ ! -f "$PROJECT_DIR/reference-dashboard/data/humanitarian_indicators.csv" ]; then
    print_error "Data files not found"
    exit 1
fi
print_status "Data files verified"

# 5. Environment-specific deployment
if [ "$ENVIRONMENT" = "dev" ]; then
    print_info "Development deployment"
    
    print_status "Ready to start development server"
    echo ""
    echo "To run the development server:"
    echo "  streamlit run wizard.py"
    echo ""
    
elif [ "$ENVIRONMENT" = "prod" ]; then
    print_info "Production deployment"
    
    # Build Docker image
    print_info "Building Docker image..."
    docker build -t winter-wizard:latest "$PROJECT_DIR"
    print_status "Docker image built"
    
    # Start services
    print_info "Starting Docker services..."
    cd "$PROJECT_DIR"
    docker-compose up -d
    print_status "Docker services started"
    
    # Wait for health check
    print_info "Waiting for app to be healthy..."
    sleep 10
    
    if curl -f http://localhost:8501/_stcore/health > /dev/null 2>&1; then
        print_status "Application is healthy"
    else
        print_error "Application health check failed"
        docker logs winter-wizard
        exit 1
    fi
    
    # Show status
    echo ""
    echo "🎉 Deployment complete!"
    echo "📊 Wizard running at: http://localhost:8501"
    echo "🌐 With Nginx: https://winter.digital-economy.org"
    echo ""
    echo "Useful commands:"
    echo "  docker logs -f winter-wizard          # View logs"
    echo "  docker-compose down                   # Stop services"
    echo "  docker-compose up -d                  # Start services"
    echo ""
fi

print_status "Deployment script completed successfully"
