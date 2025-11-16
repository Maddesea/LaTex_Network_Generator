# Makefile for LaTeX Network Diagram Generator
# Provides easy compilation and management of network diagrams

# Default target
.PHONY: all
all: main examples

# Compiler settings
LATEX = pdflatex
LATEX_FLAGS = -interaction=nonstopmode -halt-on-error
SVG_CONVERT = pdf2svg
PNG_CONVERT = convert

# Main diagram
MAIN = network_diagram_generator
MAIN_PDF = $(MAIN).pdf

# Example files
EXAMPLES = example_tiered_layout example_datacenter_grid example_hub_spoke example_comprehensive_showcase
EXAMPLE_PDFS = $(addsuffix .pdf,$(EXAMPLES))

# ============================================================================
# Main Targets
# ============================================================================

.PHONY: main
main: $(MAIN_PDF)

.PHONY: examples
examples: $(EXAMPLE_PDFS)

# Compile main diagram
$(MAIN_PDF): $(MAIN).tex network_layout.tex node_definitions.tex connection_renderer.tex threat_indicators.tex styles_config.tex network_data.tex
	@echo "Compiling main diagram..."
	$(LATEX) $(LATEX_FLAGS) $(MAIN).tex
	@echo "✓ Main diagram compiled successfully"

# Compile examples
example_%.pdf: example_%.tex network_layout.tex node_definitions.tex connection_renderer.tex threat_indicators.tex styles_config.tex
	@echo "Compiling $<..."
	$(LATEX) $(LATEX_FLAGS) $<
	@echo "✓ $< compiled successfully"

# ============================================================================
# Format Conversions
# ============================================================================

.PHONY: svg
svg: $(MAIN_PDF)
	@echo "Converting to SVG..."
	@if command -v $(SVG_CONVERT) > /dev/null; then \
		$(SVG_CONVERT) $(MAIN_PDF) $(MAIN).svg; \
		echo "✓ SVG created: $(MAIN).svg"; \
	else \
		echo "✗ pdf2svg not found. Install with: sudo apt-get install pdf2svg"; \
	fi

.PHONY: png
png: $(MAIN_PDF)
	@echo "Converting to PNG (300 DPI)..."
	@if command -v $(PNG_CONVERT) > /dev/null; then \
		$(PNG_CONVERT) -density 300 $(MAIN_PDF) $(MAIN).png; \
		echo "✓ PNG created: $(MAIN).png"; \
	else \
		echo "✗ ImageMagick not found. Install with: sudo apt-get install imagemagick"; \
	fi

.PHONY: all-formats
all-formats: main svg png
	@echo "✓ All formats generated"

# ============================================================================
# Example Conversions
# ============================================================================

.PHONY: examples-svg
examples-svg: examples
	@echo "Converting examples to SVG..."
	@for example in $(EXAMPLES); do \
		if [ -f $$example.pdf ]; then \
			$(SVG_CONVERT) $$example.pdf $$example.svg 2>/dev/null && \
			echo "✓ $$example.svg created" || \
			echo "✗ Failed to create $$example.svg"; \
		fi; \
	done

.PHONY: examples-png
examples-png: examples
	@echo "Converting examples to PNG..."
	@for example in $(EXAMPLES); do \
		if [ -f $$example.pdf ]; then \
			$(PNG_CONVERT) -density 300 $$example.pdf $$example.png 2>/dev/null && \
			echo "✓ $$example.png created" || \
			echo "✗ Failed to create $$example.png"; \
		fi; \
	done

# ============================================================================
# Quality Checks
# ============================================================================

.PHONY: check
check:
	@echo "Running quality checks..."
	@echo "Checking for required .tex files..."
	@for file in network_layout.tex node_definitions.tex connection_renderer.tex threat_indicators.tex styles_config.tex; do \
		if [ -f $$file ]; then \
			echo "  ✓ $$file"; \
		else \
			echo "  ✗ $$file (MISSING)"; \
		fi; \
	done
	@echo "Checking LaTeX installation..."
	@if command -v $(LATEX) > /dev/null; then \
		echo "  ✓ pdflatex found"; \
	else \
		echo "  ✗ pdflatex not found"; \
	fi

.PHONY: validate
validate: check
	@echo "Validating LaTeX syntax..."
	@for file in $(MAIN).tex $(addsuffix .tex,$(EXAMPLES)); do \
		echo "Checking $$file..."; \
		$(LATEX) -draftmode -interaction=batchmode $$file > /dev/null 2>&1 && \
		echo "  ✓ $$file syntax OK" || \
		echo "  ✗ $$file has errors"; \
	done

# ============================================================================
# Cleanup
# ============================================================================

.PHONY: clean
clean:
	@echo "Cleaning auxiliary files..."
	@rm -f *.aux *.log *.out *.toc *.lof *.lot *.fls *.fdb_latexmk *.synctex.gz
	@echo "✓ Auxiliary files removed"

.PHONY: clean-all
clean-all: clean
	@echo "Cleaning all generated files..."
	@rm -f *.pdf *.svg *.png
	@echo "✓ All generated files removed"

.PHONY: clean-examples
clean-examples:
	@echo "Cleaning example outputs..."
	@rm -f example_*.pdf example_*.svg example_*.png example_*.aux example_*.log
	@echo "✓ Example outputs cleaned"

# ============================================================================
# Development Helpers
# ============================================================================

.PHONY: watch
watch:
	@echo "Watching for changes (requires entr)..."
	@if command -v entr > /dev/null; then \
		ls *.tex | entr -c make main; \
	else \
		echo "✗ entr not found. Install with: sudo apt-get install entr"; \
		echo "Falling back to simple loop..."; \
		while true; do \
			make main; \
			sleep 2; \
		done; \
	fi

.PHONY: quick
quick:
	@echo "Quick compile (no dependency checking)..."
	$(LATEX) $(LATEX_FLAGS) $(MAIN).tex

.PHONY: debug
debug:
	@echo "Compiling with full output..."
	$(LATEX) -interaction=errorstopmode $(MAIN).tex

# ============================================================================
# Documentation
# ============================================================================

.PHONY: help
help:
	@echo "LaTeX Network Diagram Generator - Make targets"
	@echo ""
	@echo "Main targets:"
	@echo "  make              - Compile main diagram and examples"
	@echo "  make main         - Compile only main diagram"
	@echo "  make examples     - Compile all examples"
	@echo ""
	@echo "Format conversions:"
	@echo "  make svg          - Convert main PDF to SVG"
	@echo "  make png          - Convert main PDF to PNG"
	@echo "  make all-formats  - Generate all formats"
	@echo "  make examples-svg - Convert all examples to SVG"
	@echo "  make examples-png - Convert all examples to PNG"
	@echo ""
	@echo "Quality checks:"
	@echo "  make check        - Check for required files and tools"
	@echo "  make validate     - Validate LaTeX syntax"
	@echo ""
	@echo "Cleanup:"
	@echo "  make clean        - Remove auxiliary files (.aux, .log, etc)"
	@echo "  make clean-all    - Remove all generated files (PDFs, SVGs, PNGs)"
	@echo "  make clean-examples - Remove example outputs"
	@echo ""
	@echo "Development:"
	@echo "  make watch        - Auto-compile on file changes"
	@echo "  make quick        - Quick compile without dependency check"
	@echo "  make debug        - Compile with full error output"
	@echo ""
	@echo "Individual examples:"
	@for example in $(EXAMPLES); do \
		echo "  make $$example.pdf"; \
	done

# ============================================================================
# Installation
# ============================================================================

.PHONY: install-deps
install-deps:
	@echo "Checking and installing dependencies..."
	@echo "Note: This requires sudo privileges"
	@echo ""
	@echo "Installing LaTeX packages..."
	@sudo apt-get update
	@sudo apt-get install -y texlive-latex-base texlive-latex-extra texlive-fonts-recommended
	@echo ""
	@echo "Installing conversion tools..."
	@sudo apt-get install -y pdf2svg imagemagick
	@echo ""
	@echo "✓ Dependencies installed"

# ============================================================================
# Testing
# ============================================================================

.PHONY: test
test: clean-all all
	@echo "Running compilation tests..."
	@echo "✓ Main diagram compiled"
	@for example in $(EXAMPLES); do \
		if [ -f $$example.pdf ]; then \
			echo "✓ $$example compiled"; \
		else \
			echo "✗ $$example failed"; \
		fi; \
	done
	@echo ""
	@echo "Test summary:"
	@echo "  Main: $(MAIN_PDF)"
	@echo "  Examples: $(words $(wildcard example_*.pdf)) of $(words $(EXAMPLES)) compiled"

.PHONY: benchmark
benchmark:
	@echo "Running performance benchmark..."
	@echo "Compiling main diagram 3 times..."
	@time -p sh -c 'make clean > /dev/null 2>&1 && make main > /dev/null 2>&1'
	@time -p sh -c 'make clean > /dev/null 2>&1 && make main > /dev/null 2>&1'
	@time -p sh -c 'make clean > /dev/null 2>&1 && make main > /dev/null 2>&1'

# ============================================================================
# Special Targets
# ============================================================================

.PHONY: showcase
showcase: example_comprehensive_showcase.pdf
	@echo "✓ Comprehensive showcase compiled"
	@echo "View with: evince example_comprehensive_showcase.pdf &"

.PHONY: tiered
tiered: example_tiered_layout.pdf
	@echo "✓ Tiered layout example compiled"

.PHONY: datacenter
datacenter: example_datacenter_grid.pdf
	@echo "✓ Data center example compiled"

.PHONY: hub-spoke
hub-spoke: example_hub_spoke.pdf
	@echo "✓ Hub-and-spoke example compiled"

# Prevent deletion of intermediate files
.PRECIOUS: %.pdf %.svg %.png

# Default shell
SHELL := /bin/bash
