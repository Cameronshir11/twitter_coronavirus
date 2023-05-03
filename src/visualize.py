#!/usr/bin/env python3

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
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
top_10_items = items[:10]
k = [item[0] for item in top_10_items]
v = [item[1] for item in top_10_items]
index = range(len(k))[::-1]
plt.bar(k, v)

if args.input_path == "reduced.lang":
    plt.title(f'Twitter Usage of {args.key} by Language in 2020')
    plt.xlabel('Language')
    plt.ylabel('Number of tweets')
    plt.show()
    plt.savefig(f'lang {args.key} barchart.png')
else:
    plt.title(f'Twitter Usage of {args.key} by Country in 2020')
    plt.xlabel('Country')
    plt.ylabel('Number of tweets')
    plt.show()
    plt.savefig(f'lang {args.key} barchart.png')
'''    
plt.title('#coronavirus in Korean')
if args.input_path[-1] == 'g':
    plt.savefig(args.key[1:] + '_lang.png')
else:
    plt.savefig(args.key[1:] + '_country.png')
'''
