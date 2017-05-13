#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 14:05:36 2017

@author: Santhosh
"""

import os, re, fnmatch, nltk
from nltk.probability import FreqDist
from datetime import date, timedelta

rootPath = './Comments'
pattern = 'data.json'

sys.stdout = open('file', 'w', encoding='Latin-1')

postID = []

for root, dirs, files in os.walk(rootPath):
        
    for filename in fnmatch.filter(files, pattern):
            
        fullpath = os.path.join(root, filename)
            
        for line in open(fullpath, encoding='Latin-1'):
            if len(line) == 12 or len(line) == 13:
                postID.append(re.sub("[^\w]", " ",  line).split()[0])
                
    
    

postIDFreqDict = FreqDist(postID)
    
sortPID = sorted(postIDFreqDict.items(), key=lambda value: value[1], reverse=True)[:250]
print('A dictionary of top 250 post IDs and their frequencies based on their number of occurances in the comment section:')
print(sortPID)
print('\n')

print('Top 250 post IDs and their Titles:')
for postIDVal in sortPID:
    for item in re.findall(r'\'+\w+\'', str(postIDVal)):
        f = open('/Users/Santhosh/Downloads/result.csv', 'rt', encoding='Latin-1')
        try:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == item.strip("''"):
                    print('Post ID: '+item.strip("''"))
                    print('Post Title: '+row[2])
        
        finally:
            f.close()