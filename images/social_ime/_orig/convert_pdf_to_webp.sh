#!/bin/sh

rm -f keijiban-*.{png,webp}

pdftoppm -png "keijiban_ocr_scanned.pdf" keijiban

for f in *.png
do
    magick -quality 90 $f ${f%.png}.webp
done

rm -f keijiban-*.png
