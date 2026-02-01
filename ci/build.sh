#!/usr/bin/env bash
set -euo pipefail
set -x

# Helpful debug
echo "PWD: $(pwd)"
echo "TeX:"
latexmk -v || true
lualatex --version || true
echo "Perl:"
perl -v | head -n 2 || true
echo "beamer-reveal.pl:"
command -v beamer-reveal.pl || true

# Build PDF with latexmk (BibTeX included)
latexmk \
  -lualatex \
  -auxdir=build \
  -outdir=build \
  -shell-escape \
  -verbose \
  -file-line-error \
  -interaction=nonstopmode \
  -synctex=1 \
  -bibtex \
  main.tex

# Build website output
mkdir -p website
beamer-reveal.pl main --pdf-directory build --output-directory website

# Sanity check
test -f website/index.html || (echo "Missing website/index.html" && exit 1)
