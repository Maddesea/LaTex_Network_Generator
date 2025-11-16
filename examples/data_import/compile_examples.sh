#!/bin/bash
# compile_examples.sh - Compile all data import examples
# This script compiles all example files in the data_import directory

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Data Import Examples - Compilation${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# Check for required tools
echo -e "${YELLOW}Checking for required tools...${NC}"

if ! command -v pdflatex &> /dev/null; then
    echo -e "${RED}ERROR: pdflatex not found. Please install TeX Live.${NC}"
    exit 1
fi
echo -e "${GREEN}✓ pdflatex found${NC}"

if command -v lualatex &> /dev/null; then
    echo -e "${GREEN}✓ lualatex found (required for Nmap/Nessus/JSON/YAML examples)${NC}"
    HAS_LUALATEX=true
else
    echo -e "${YELLOW}⚠ lualatex not found (some examples will be skipped)${NC}"
    HAS_LUALATEX=false
fi

echo ""

# Function to compile with pdflatex
compile_pdf() {
    local file=$1
    local name=$(basename "$file" .tex)

    echo -e "${BLUE}Compiling: ${name}${NC}"

    if pdflatex -interaction=nonstopmode -halt-on-error "$file" > "${name}.log" 2>&1; then
        echo -e "${GREEN}✓ Success: ${name}.pdf${NC}"
        return 0
    else
        echo -e "${RED}✗ Failed: ${name}${NC}"
        echo -e "${RED}  Check ${name}.log for errors${NC}"
        return 1
    fi
}

# Function to compile with lualatex
compile_lua() {
    local file=$1
    local name=$(basename "$file" .tex)

    echo -e "${BLUE}Compiling: ${name} (LuaLaTeX)${NC}"

    if lualatex -interaction=nonstopmode -halt-on-error "$file" > "${name}.log" 2>&1; then
        echo -e "${GREEN}✓ Success: ${name}.pdf${NC}"
        return 0
    else
        echo -e "${RED}✗ Failed: ${name}${NC}"
        echo -e "${RED}  Check ${name}.log for errors${NC}"
        return 1
    fi
}

# Counters
SUCCESS_COUNT=0
FAIL_COUNT=0
SKIP_COUNT=0

echo -e "${YELLOW}Starting compilation...${NC}"
echo ""

# Compile CSV example (works with pdflatex)
if [ -f "example_csv_import.tex" ]; then
    if compile_pdf "example_csv_import.tex"; then
        ((SUCCESS_COUNT++))
    else
        ((FAIL_COUNT++))
    fi
    echo ""
fi

# Compile auto-positioning example (works with pdflatex)
if [ -f "example_auto_positioning.tex" ]; then
    if compile_pdf "example_auto_positioning.tex"; then
        ((SUCCESS_COUNT++))
    else
        ((FAIL_COUNT++))
    fi
    echo ""
fi

# Compile advanced integration example (works with pdflatex)
if [ -f "example_advanced_integration.tex" ]; then
    if compile_pdf "example_advanced_integration.tex"; then
        ((SUCCESS_COUNT++))
    else
        ((FAIL_COUNT++))
    fi
    echo ""
fi

# LuaLaTeX-only examples
if [ "$HAS_LUALATEX" = true ]; then
    # Compile Nmap example
    if [ -f "example_nmap_import.tex" ]; then
        if compile_lua "example_nmap_import.tex"; then
            ((SUCCESS_COUNT++))
        else
            ((FAIL_COUNT++))
        fi
        echo ""
    fi

    # Compile Nessus example
    if [ -f "example_nessus_import.tex" ]; then
        if compile_lua "example_nessus_import.tex"; then
            ((SUCCESS_COUNT++))
        else
            ((FAIL_COUNT++))
        fi
        echo ""
    fi
else
    echo -e "${YELLOW}Skipping LuaLaTeX examples (lualatex not available)${NC}"
    echo -e "${YELLOW}  - example_nmap_import.tex${NC}"
    echo -e "${YELLOW}  - example_nessus_import.tex${NC}"
    SKIP_COUNT=2
    echo ""
fi

# Clean up auxiliary files
echo -e "${YELLOW}Cleaning up auxiliary files...${NC}"
rm -f *.aux *.log *.out *.toc *.nav *.snm

# Summary
echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Compilation Summary${NC}"
echo -e "${BLUE}========================================${NC}"
echo -e "${GREEN}Successful: ${SUCCESS_COUNT}${NC}"
if [ $FAIL_COUNT -gt 0 ]; then
    echo -e "${RED}Failed: ${FAIL_COUNT}${NC}"
fi
if [ $SKIP_COUNT -gt 0 ]; then
    echo -e "${YELLOW}Skipped: ${SKIP_COUNT}${NC}"
fi
echo ""

if [ $FAIL_COUNT -eq 0 ]; then
    echo -e "${GREEN}✓ All examples compiled successfully!${NC}"
    exit 0
else
    echo -e "${RED}✗ Some examples failed to compile.${NC}"
    echo -e "${YELLOW}Check the log files for details.${NC}"
    exit 1
fi
