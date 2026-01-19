#!/bin/sh

for f in *.png
do
    magick -quality 90 $f ${f%.png}.webp
done
