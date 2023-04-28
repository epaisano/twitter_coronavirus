#!/bin/sh
for file in '/data/Twitter dataset/'geoTwitter20-07-12.zip; do
    $(./src/map.py --input_path="$file"); done
