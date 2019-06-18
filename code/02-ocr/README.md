# Notes on OCR

The goal is to produce noise-free black and white pages, displaying glyphs (letters) that have
sharp, well-defined edges. This pipeline will vary greatly depending on the quality of the
initial scan.

1. Use `pdf-to-tiff.sh` to convert to pdf to tiff for tesseract.
2. `localthresh -m 1 -r 15 -b 8 -n yes <infile> <outfile>` to binaraize the above into a black
   and white image.
3. Use `textcleaner` to remove noise, or sharpen or soften edges.
4. Run `tesseract <input.tiff> <name of output textfile>` for OCR.
5. Run `wc -w <file>` to count the number of words extracted and compare against `hunspell -l
   <file> | wc -l`, which counts the number of words misspelled.

Some useful resources include:

- https://emop.tamu.edu/software-pre-processing
- http://www.fmwconcepts.com/imagemagick/index.php
- https://guides.library.illinois.edu/OCR/intro
