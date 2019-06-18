gs \
 -sOutputFile=output.tiff \
 -sDEVICE=tiffgray \
 -r600 \
 -monochrome \
 -sColorConversionStrategy=Gray \
 -dProcessColorModel=/DeviceGray \
 -dCompatibilityLevel=1.4 \
 -dNOPAUSE \
 -dBATCH -i \
$1
