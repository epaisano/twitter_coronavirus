#!/usr/bin/env python3
import matplotlib
matplotlib.use('Agg')

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
#parser.add_argument('--key',required=True)
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


# making dataframe
df = pd.DataFrame(counts)
cols = list(df.axes[0])
df= df.T
df = df.reset_index()


df = df.rename(columns={'index': "date"})
df['date'] = df['date'].str.replace('outputs/geoTwitter', '').str.replace('.zip.lang', '').str.replace('20-', '')
df['date'] = df['date'].str[:] + '-2020'
df["date"] = pd.to_datetime(df["date"])

# making line plot
fig, ax = plt.subplots()
plt.plot(df['date'], df['#coronavirus'], label = "#coronavirus")
plt.plot(df['date'], df['#corona'], label = "#corona")
plt.plot(df['date'], df['#covid19'], label = "#covid19")
plt.legend()
plt.xlabel('Date')
plt.ylabel('Frequency')
ax.set_title('Frequency of Tag Usage in 2020')
plt.tight_layout()
altreduce_png = 'altreduce.png'
plt.savefig(altreduce_png, dpi=150)


