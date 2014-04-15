#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project: Stats
 Author: Matt Post <post@cs.jhu.edu>

This scripts computes some statistics about the number of HITs, number of rankings,
number per language pair, and so on.

Usage: python count_rankings.py < RESULTS_FILE

where RESULTS_FILE is a file in WMT format.
"""
from itertools import combinations
from collections import defaultdict
from csv import DictReader
import sys
import argparse

if __name__ == "__main__":

    all_rankings = []
    lang_rankings = {}
    sentences = {}
    systems = {}
    for i,row in enumerate(DictReader(sys.stdin)):
        rankings = 0
        for pair in combinations(range(5),2):
            rank1 = row.get('system%drank' % (pair[0] + 1))
            rank2 = row.get('system%drank' % (pair[1] + 1))
            name1 = row.get('system%dId' % (pair[0] + 1))
            name2 = row.get('system%dId' % (pair[1] + 1))
            if rank1 < rank2:
                print "%s < %s" % (name1, name2)
            elif rank1 > rank2:
                print "%s < %s" % (name2, name1)
            else:
                print "%s = %s" % (name1, name2)
