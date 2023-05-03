#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

import os
import json
from collections import Counter,defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

with open(args.input_path) as f:
    counts = json.load(f)

if args.percent:
    for k in counts[args.key]:
        if k in counts['_all']:
            counts[args.key][k] /= counts['_all'][k]

items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
for k,v in items:
    print(k,':',v)

top_items = items[:10] 
keys = [item[0] for item in top_items]
values = [item[1] for item in top_items]
keys = keys[::-1]
values = values[::-1]

plt.bar(range(len(keys)), values)
plt.xticks(range(len(keys)), keys)
if args.input_path[-1] == 'g':
    plt.title(f'Number of Tweets by Language')
    plt.xlabel('Language')
else:
    plt.title(f'Number of Tweets by Country')
    plt.xlabel('Country')
if args.percent:
    plt.ylabel('Percentage')
else:
    plt.ylabel('Number of Tweets')

if args.input_path[-1] == 'g':
    plt.savefig(args.key[1:] + '_lang.png')
else:
    plt.savefig(args.key[1:] + '_country.png')
