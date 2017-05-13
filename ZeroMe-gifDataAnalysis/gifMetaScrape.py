#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 15:01:15 2017

This is a data extractions and cleaning script from the Gif Data of ZeroMe site. 
"""

import csv, re, sys, nltk
from nltk.probability import FreqDist
from nltk.corpus import stopwords

f = open('./result.csv', 'rt', encoding='Latin-1')
count = 0;
wordList = []
srcList = []
dateList = []

try:
    reader = csv.reader(f)
    for row in reader:
        for wrds in re.sub("[^\w]", " ",  row[2]).split():
            wordList.append(wrds.lower())
            
        srcList.append(row[1])
            
        dateList.append(row[3])
            
        count+=1
        
    print('Number of rows :'+str(count-1) + ' & length of word list :' + str(len(wordList)))
    print('\n')

    filtered_words = [word for word in wordList if word not in stopwords.words('english')]

    wordFreqDict = FreqDist(filtered_words)
    srcFreqDict = FreqDist(srcList)
    dateFreqDict = FreqDist(dateList)
    
    sortWF = sorted(wordFreqDict.items(), key=lambda value: value[1], reverse=True)[:100]
    print('Top 100 word frequency after removing stopwords:')
    print(sortWF)
    print('\n')
    
    sortSrc = sorted(srcFreqDict.items(), key=lambda value: value[1], reverse=True)
    print('Gif Source Frequency:')
    print(sortSrc)
    print('\n')
    
    sortDt = sorted(dateFreqDict.items(), key=lambda value: value[1], reverse=True)
    print('Date Frequencies (can be used for building a time series plot):')
    print(sortDt)

        
finally:
    f.close()
    
    
