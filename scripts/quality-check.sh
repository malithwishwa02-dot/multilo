#!/bin/bash

# Code quality check script
# Usage: ./scripts/quality-check.sh

set -e

echo "=== Running Code Quality Checks ==="
echo ""

# Check if virtual environment is activated
if [ -z "$VIRTUAL_ENV" ]; then
    echo "⚠️  Virtual environment not activated"
    echo "Run: source venv/bin/activate"
    exit 1
fi

# Flake8 - Style Guide Enforcement
echo "1. Running flake8..."
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics || true
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics || true
echo "✓ Flake8 check complete"
echo ""

# Pylint - Code Analysis
echo "2. Running pylint..."
pylint *.py --disable=C,R,W --max-line-length=127 || true
echo "✓ Pylint check complete"
echo ""

# Black - Code Formatting
echo "3. Checking code formatting with black..."
black --check --line-length 127 . || true
echo "✓ Black check complete"
echo ""

# Isort - Import Sorting
echo "4. Checking import sorting..."
isort --check-only --profile black . || true
echo "✓ Isort check complete"
echo ""

# Bandit - Security Check
echo "5. Running security checks with bandit..."
bandit -r . -f json -o logs/bandit-report.json || true
echo "✓ Bandit check complete (report saved to logs/bandit-report.json)"
echo ""

# MyPy - Type Checking
echo "6. Running type checks with mypy..."
mypy . --ignore-missing-imports --no-strict-optional || true
echo "✓ MyPy check complete"
echo ""

echo "=== Code Quality Checks Complete ==="
echo ""
echo "To auto-fix formatting issues:"
echo "  black --line-length 127 ."
echo "  isort --profile black ."
echo ""
