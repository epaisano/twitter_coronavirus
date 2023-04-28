#!/usr/bin/env python3
import matplotlib
matplotlib.use('Agg')

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
from operator import add
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
for k,v in items:
    print(k,':',v)

# making bar chart
cat = [cat for cat,val in items]
val = [val for cat,val in items]
x = list(range(len(cat)))
width = 0.25
widthlis = [0.25 for x in list(range(len(cat)))]

plt.rcdefaults()
fig, ax = plt.subplots()
ax.barh(cat,val, align='center')
ax.set_xlabel('Frequency of #coronavirus Usage')
ax.set_title('Frequency of #coronavirus Usage by Language')
ax.set_xticks(list(map(add, x, widthlis)), cat)
out_png = 'out_file.png'
plt.savefig(out_png, dpi=150)
