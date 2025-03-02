#!/usr/bin/env python3
import matplotlib
import numpy as np
import json
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import argparse
from collections import Counter, defaultdict
from glob import glob

# command args
parser = argparse.ArgumentParser()
parser.add_argument('--input_dir', required=True)
parser.add_argument('--keys', nargs='+', required=True)
args = parser.parse_args()
input_files = glob(args.input_dir + '/*')
for key in args.keys:
    y_axis = []
    total = defaultdict(lambda: Counter())

    for path in sorted(input_files):
        with open(path) as f:
            tmp = json.load(f)
            sumofnum = 0
            try:
                for k in tmp[key]:
                    sumofnum += tmp[key][k]
            except:
                pass
            y_axis.append(sumofnum)
    plt.plot(np.arange(len(y_axis)), y_axis, label=key)
plt.xlabel("Date in 2020")
plt.ylabel("Number of Tweets")
plt.title("Number of Tweets with a Different Word by Each Day in 2020")
plt.legend()
plt.xticks([0,60,120,180,240,300,360,420,480,540,600,660], ["Jan","Feb", "Mar", "Apr", "May", "Jun", "Jul","Aug", "Sept","Oct", "Nov", "Dec"])
plt.savefig("myplot5.png",bbox_inches="tight")
