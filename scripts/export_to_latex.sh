# On WSL, remember to run xserver before running this script.
svg_files=$(find . -name "*.svg")
for svg in $svg_files
do
  pushd $(dirname $svg)
  inkscape --batch-process --export-latex --export-type="pdf" $(basename $svg)
  popd
done
