#!/usr/bin/env python3


# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_paths',nargs='+',required=True)
parser.add_argument('--output_path',required=True)
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict


###############################################
################## Reducing ###################
###############################################





# load each of the input paths
total = defaultdict(lambda: Counter())
intermed = defaultdict()
for path in args.input_paths: #for every geotwit file
    with open(path) as f: #opening indiv geotwit file
        tmp = json.load(f) #loading contents in each file (tmp is a file!!!)
        for k in tmp:
            #print("k=", k)
            #print("tmp[k]=", tmp[k])
            #print("tmp[k].keys()=", tmp[k].keys())
            #print("tmp[k].value()=", tmp[k].values())
            intermed[k] = sum(list(tmp[k].values()))
            total[path] += intermed
        #hashtags = list(tmp.keys())
        #usage = list(tmp.values())
        #lis = [list(x.values()) for x in usage]
        #sumlis = [sum(x) for x in lis]
        #for i in list(range(len(hashtags))): #for every key in our file,
            #for j in list(range(len(sumlis))):
                #print("hashtags[i]=", hashtags[i])
                #print("sumlis[j]=", sumlis[j])
                #intermed[hashtags[i]] = sumlis[j] #making dictionary of total hashtag usage in a day


# write the output path
with open(args.output_path,'w') as f:
    f.write(json.dumps(total))

