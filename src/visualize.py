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
import pandas as pd

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
print("args.percent=", args.percent)
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
for k,v in items:
    print(k,':',v)

# making bar chart
sorteditems = sorted(items, key=lambda x: x[1])
cat = [cat for cat,val in sorteditems][-10:]
val = [val for cat,val in sorteditems][-10:]
val,cat = zip(*sorted(zip(val,cat)))
cat = list(cat)

x = list(range(len(cat)))
widthlis = [0.8 for x in list(range(len(cat)))]

plt.rcdefaults()
fig, ax = plt.subplots()
plt.bar(range(len(cat)),val, align='center')
plt.xlabel('Language')
plt.ylabel('Frequency')
ax.set_title('Frequency of the #coronavirus Usage by Language in 2020')
plt.xticks(range(len(cat)), cat)
plt.tight_layout()
covidfreqlang2020_png = 'covidfreqlang2020.png'
plt.savefig(covidfreqlang2020_png, dpi=150)

