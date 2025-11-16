#!/bin/bash
# Compile all example files
# Usage: ./compile_all.sh [compiler]
# Default compiler: pdflatex

COMPILER=${1:-pdflatex}
ERROR_COUNT=0
SUCCESS_COUNT=0

echo "====================================="
echo "Network Diagram Examples Compiler"
echo "====================================="
echo "Using compiler: $COMPILER"
echo ""

# Array of example files
EXAMPLES=(
    "01_basic_network_colorschemes.tex"
    "02_enterprise_gradients.tex"
    "03_security_with_badges.tex"
    "04_multicloud_architecture.tex"
    "05_accessibility_patterns.tex"
    "07_complete_demo.tex"
)

# Beamer presentation (needs special handling)
BEAMER_EXAMPLE="06_beamer_presentation.tex"

# Function to compile a file
compile_file() {
    local file=$1
    local basename=$(basename "$file" .tex)

    echo "Compiling: $file"

    # Run compiler twice for references
    $COMPILER -interaction=nonstopmode "$file" > "${basename}_compile.log" 2>&1

    if [ $? -eq 0 ]; then
        # Second pass for references
        $COMPILER -interaction=nonstopmode "$file" >> "${basename}_compile.log" 2>&1

        if [ $? -eq 0 ]; then
            echo "  ✓ SUCCESS: ${basename}.pdf created"
            ((SUCCESS_COUNT++))

            # Clean up auxiliary files
            rm -f "${basename}.aux" "${basename}.log" "${basename}.out" \
                  "${basename}.nav" "${basename}.snm" "${basename}.toc" \
                  "${basename}_compile.log"
        else
            echo "  ✗ FAILED: Second pass failed"
            echo "  See ${basename}_compile.log for details"
            ((ERROR_COUNT++))
        fi
    else
        echo "  ✗ FAILED: Compilation error"
        echo "  See ${basename}_compile.log for details"
        ((ERROR_COUNT++))
    fi

    echo ""
}

# Compile standard examples
for example in "${EXAMPLES[@]}"; do
    if [ -f "$example" ]; then
        compile_file "$example"
    else
        echo "Warning: $example not found, skipping"
        echo ""
    fi
done

# Compile Beamer presentation if it exists
if [ -f "$BEAMER_EXAMPLE" ]; then
    echo "Compiling Beamer presentation: $BEAMER_EXAMPLE"
    compile_file "$BEAMER_EXAMPLE"
fi

# Summary
echo "====================================="
echo "Compilation Summary"
echo "====================================="
echo "Successful: $SUCCESS_COUNT"
echo "Failed: $ERROR_COUNT"
echo ""

if [ $ERROR_COUNT -eq 0 ]; then
    echo "✓ All examples compiled successfully!"
    exit 0
else
    echo "✗ Some examples failed to compile"
    echo "  Check the *_compile.log files for details"
    exit 1
fi
