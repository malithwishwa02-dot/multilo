#!/bin/bash

# Development setup script for Quantum Profile Warmup CLI
# Usage: ./scripts/setup.sh

set -e

echo "=== Quantum Profile Warmup CLI - Development Setup ==="
echo ""

# Check Python version
echo "Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "Found Python $python_version"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Install development dependencies
echo "Installing development dependencies..."
pip install pytest pytest-cov pylint flake8 black isort mypy bandit

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating .env file from example..."
    cp env_Version2.example.txt .env
    echo "⚠️  Please edit .env file and add your API keys"
fi

# Create output directories
echo "Creating output directories..."
mkdir -p out batch_profiles logs

# Run basic tests
echo ""
echo "Running basic import tests..."
python3 -c "import requests; import selenium; import numpy; print('✓ All imports successful')"

echo ""
echo "=== Setup Complete ==="
echo ""
echo "Next steps:"
echo "1. Edit .env file and add your API keys"
echo "2. Activate virtual environment: source venv/bin/activate"
echo "3. Run the CLI: python3 main.py --help"
echo ""
