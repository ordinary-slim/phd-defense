# On WSL, remember to run xserver before running this script.
#set -eux
svg_files=$(find . -name "*.svg")
for svg in $svg_files
do
  pushd $(dirname $svg)
  fname=$(basename -s .svg $svg)
  inkscape --batch-process --export-latex --export-type="pdf" ${fname}.svg
  test -f ${fname}.pdf || { echo "Missing PDF ${fname}.pdf"; exit 1; }
  test -f ${fname}.pdf_tex || { echo "Missing PDF_TEX ${fname}.pdf_tex"; exit 1; }
  popd
done
