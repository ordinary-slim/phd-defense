# AGENTS.md - PhD Defense Presentation Repository

This repository contains a LaTeX-based PhD defense presentation about computational strategies for time-accurate simulation of part-scale LPBF (Laser Powder Bed Fusion). The project uses LaTeX/Beamer for the presentation, Python scripts for data processing, and shell scripts for automation.

## Project Structure

This is a **LaTeX Beamer presentation** project with:
- **Main document**: `main.tex` (LuaLaTeX document)
- **Content sections**: Individual `.tex` files for each presentation section
- **Build system**: LaTeX with `latexmk` configuration
- **Output directory**: `build/` for compiled artifacts
- **Web publishing**: `website/` for HTML export via `beamer-reveal`
- **Media assets**: `videos/`, `figures/`, `plots/` directories
- **Python scripts**: Data processing utilities in `plots/` subdirectories

## Build & Development Commands

### Primary Build Commands
```bash
# Build the PDF presentation (main command)
latexmk -lualatex -output-directory=build main.tex

# Clean build artifacts
latexmk -C

# Continuous build (watch for changes)
latexmk -lualatex -pvc -output-directory=build main.tex

# Export SVGs to PDF with LaTeX compatibility
./scripts/export_to_latex.sh

# Generate web version of presentation
./publish.sh
```

### Development Commands
```bash
# View build log
less build/main.log

# Check for LaTeX errors
grep -i error build/main.log

# Find LaTeX warnings
grep -i warning build/main.log

# List all TeX files
find . -name "*.tex" -not -path "./build/*"
```

### Python Script Execution
```bash
# Run CSV scaling script
cd plots/meltpool_contours/
python scale_csv.py -i input.csv -o output.csv
```

### Single File Testing
Since this is a presentation project, there are no traditional "tests". However:
```bash
# Test compile a single section
latexmk -lualatex -output-directory=build -interaction=nonstopmode objectives.tex

# Validate LaTeX syntax for a file
chktex lpbf.tex

# Preview specific section (if working on modular approach)
echo "\input{main.tex}\begin{document}\input{lpbf.tex}\end{document}" > temp.tex && latexmk -lualatex temp.tex
```

## Code Style Guidelines

### LaTeX Conventions

#### File Organization
- **Main file**: `main.tex` contains document structure and preamble
- **Section files**: Individual `.tex` files for content (e.g., `lpbf.tex`, `objectives.tex`)
- **Helper files**: `helpers.tex` for custom commands and configurations
- **Style file**: `metropolis.tex` for Beamer theme configuration

#### LaTeX Coding Style
```latex
% Use consistent indentation (2 spaces)
\begin{frame}
  \frametitle{Title}
  \begin{itemize}
    \item First item
    \item Second item
  \end{itemize}
\end{frame}

% Command definitions in helpers.tex
\newcommand{\todo}[1]{
  \ifisdraft {
    \Large
    $\color{black}\star$\color{red}~\textit{#1}\color{black}~$\star$
  } \fi
}

% Use descriptive names for custom commands
\newcommand{\legendpowderbulk}{%
  \begin{tabular}{rlrl}
     ({\color{powderColor} \rule[-1.5 pt]{8 pt}{8 pt}}) & Powder & ({\color{metalColor} \rule[-1.5 pt]{8 pt}{8 pt}})  & Bulk
  \end{tabular}
}
```

#### Naming Conventions
- **Files**: Use kebab-case for multi-word files (`substepping-examples.tex`)
- **Commands**: Use camelCase (`\playthumb`, `\labelbox`)
- **Colors**: Descriptive names (`\definecolor{advectionColor}`)
- **Environments**: Follow LaTeX conventions

#### Mathematical Notation
```latex
% Custom math commands for consistency
\newcommand{\nablaxi}[0]{\nabla_{\boldsymbol{\xi}}}
\newcommand{\deltaxi}[0]{\Delta_{\boldsymbol{\xi}}}
\newcommand{\support}[1]{\text{supp}\left(#1\right)}
\newcommand{\eunorm}[1]{
  \text{\Large$|\hspace{-0.8mm}|$}\; #1 \;\text{\Large$|\hspace{-0.8mm}|_{\scriptscriptstyle{2}}$}
}
```

### Python Conventions

#### Script Structure
```python
import pandas as pd
import argparse

def main(input_csv, output_csv):
    """Main processing function with clear parameters."""
    # Read the CSV file
    df = pd.read_csv(input_csv)
    
    # Apply transformations
    df['x'] *= -1e-3
    df['x'] += +(0.000236*1e3) - (-38.72943637745948*1e-3)
    df.sort_values(by='x', inplace=True)
    
    # Save results
    df.to_csv(output_csv, index=False)

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, default='data.csv', help='Input CSV file path')
    parser.add_argument('-o', '--output', type=str, default='scaled_data.csv', help='Output CSV file path')
    args = parser.parse_args()
    main(args.input, args.output)
```

#### Style Rules
- Use **argparse** for command-line interfaces
- Include **default values** and **help text**
- Use **descriptive function and variable names**
- Follow **PEP 8** conventions for Python code
- Include **docstrings** for functions

### Shell Script Conventions

#### Script Structure
```bash
#!/bin/bash
# Clear comments at the top explaining purpose

# Use descriptive variable names
svg_files=$(find . -name "*.svg")
for svg in $svg_files
do
  pushd $(dirname $svg)
  inkscape --batch-process --export-latex --export-type="pdf" $(basename $svg)
  popd
done
```

## Error Handling

### LaTeX Error Handling
- **Draft mode**: Enable draft mode in `main.tex` for faster compilation during development
- **Error logging**: Check `build/main.log` for compilation errors
- **Missing packages**: Install missing LaTeX packages via TeX Live manager

### Python Error Handling
- **File validation**: Check input file existence before processing
- **Exception handling**: Use try-catch blocks for file operations
- **Argument validation**: Validate command-line arguments

## Development Workflow

1. **Edit content**: Modify individual section `.tex` files
2. **Test build**: Run `latexmk -lualatex -output-directory=build main.tex`
3. **Check output**: Review `build/main.pdf`
4. **Debug errors**: Examine `build/main.log` if compilation fails
5. **Iterative development**: Use continuous build with `-pvc` flag

## Repository Conventions

- **Git workflow**: Standard GitHub flow (main branch: `main`)
- **Remote**: `https://github.com/ordinary-slim/phd-defense.git`
- **Build artifacts**: Excluded from version control (in `build/` directory)
- **Media files**: Large video files committed to repository
- **Documentation**: This AGENTS.md file for development guidance

## Dependencies

- **LaTeX**: LuaLaTeX engine (TeXLive 2025)
- **Packages**: beamer, tikz, pgfplots, siunitx, natbib, multimedia
- **Python**: pandas, argparse
- **External tools**: inkscape (for SVG conversion), beamer-reveal.pl

## Notes for Agents

- This is a **presentation project**, not a software application
- Focus on **content accuracy** and **LaTeX best practices**
- **Build artifacts** are in `build/` directory, do not edit directly
- **Media files** are large and should be handled carefully
- **Python scripts** are utilities for data processing, not core functionality
- **Web export** via beamer-reveal requires specific workflow