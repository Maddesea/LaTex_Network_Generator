#!/bin/bash
# compile.sh - Compilation script for network diagram generator
# Usage: ./compile.sh [output_format]
# Formats: pdf (default), svg, png, all

set -e  # Exit on error

OUTPUT_FORMAT="${1:-pdf}"
MAIN_FILE="network_diagram_generator"

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "LaTeX Network Diagram Generator - Build Script"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Check if required files exist
check_files() {
    local required_files=(
        "${MAIN_FILE}.tex"
        "styles_config.tex"
        "node_definitions.tex"
        "network_layout.tex"
        "connection_renderer.tex"
        "threat_indicators.tex"
        "network_data.tex"
    )
    
    for file in "${required_files[@]}"; do
        if [ ! -f "$file" ]; then
            echo "❌ ERROR: Required file '$file' not found!"
            exit 1
        fi
    done
    echo "✅ All required files present"
}

# Check if pdflatex is installed
check_latex() {
    if ! command -v pdflatex &> /dev/null; then
        echo "❌ ERROR: pdflatex not found. Please install TeXLive."
        echo "   Ubuntu/Debian: sudo apt-get install texlive-full"
        echo "   Fedora/RHEL: sudo dnf install texlive-scheme-full"
        exit 1
    fi
    echo "✅ pdflatex found: $(pdflatex --version | head -n1)"
}

# Compile to PDF
compile_pdf() {
    echo ""
    echo "📄 Compiling to PDF..."
    pdflatex -interaction=nonstopmode "${MAIN_FILE}.tex" > /dev/null 2>&1
    
    if [ $? -eq 0 ]; then
        echo "✅ PDF compiled successfully: ${MAIN_FILE}.pdf"
    else
        echo "❌ PDF compilation failed. Check the log file:"
        pdflatex -interaction=nonstopmode "${MAIN_FILE}.tex"
        exit 1
    fi
}

# Convert to SVG
compile_svg() {
    if ! command -v pdf2svg &> /dev/null; then
        echo "⚠️  WARNING: pdf2svg not found. Install with:"
        echo "   Ubuntu/Debian: sudo apt-get install pdf2svg"
        echo "   Fedora/RHEL: sudo dnf install pdf2svg"
        echo "   Skipping SVG conversion."
        return
    fi
    
    echo ""
    echo "🎨 Converting to SVG..."
    pdf2svg "${MAIN_FILE}.pdf" "${MAIN_FILE}.svg"
    echo "✅ SVG created: ${MAIN_FILE}.svg"
}

# Convert to PNG
compile_png() {
    if ! command -v convert &> /dev/null; then
        echo "⚠️  WARNING: ImageMagick not found. Install with:"
        echo "   Ubuntu/Debian: sudo apt-get install imagemagick"
        echo "   Fedora/RHEL: sudo dnf install ImageMagick"
        echo "   Skipping PNG conversion."
        return
    fi
    
    echo ""
    echo "🖼️  Converting to PNG (300 DPI)..."
    convert -density 300 "${MAIN_FILE}.pdf" -quality 100 "${MAIN_FILE}.png"
    echo "✅ PNG created: ${MAIN_FILE}.png"
}

# Clean auxiliary files
clean_aux() {
    echo ""
    echo "🧹 Cleaning auxiliary files..."
    rm -f *.aux *.log *.out *.toc *.nav *.snm *.vrb
    echo "✅ Cleanup complete"
}

# Main execution
main() {
    check_files
    check_latex
    
    case "$OUTPUT_FORMAT" in
        pdf)
            compile_pdf
            ;;
        svg)
            compile_pdf
            compile_svg
            ;;
        png)
            compile_pdf
            compile_png
            ;;
        all)
            compile_pdf
            compile_svg
            compile_png
            ;;
        clean)
            clean_aux
            rm -f "${MAIN_FILE}.pdf" "${MAIN_FILE}.svg" "${MAIN_FILE}.png"
            echo "✅ All output files removed"
            exit 0
            ;;
        *)
            echo "❌ Unknown format: $OUTPUT_FORMAT"
            echo "Usage: $0 [pdf|svg|png|all|clean]"
            exit 1
            ;;
    esac
    
    clean_aux
    
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "✅ Build complete!"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
}

main
