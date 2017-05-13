import csv
import json
import collections
import watson_developer_cloud
import textblob
import nltk
from watson_developer_cloud import LanguageTranslatorV2 as LanguageTranslator
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from textblob import TextBlob

# read csv and creating a dictionary with user_name and his status
status = dict()
with open(r'C:\Users\iimra\Documents\hackathontampa\data.csv',encoding='utf-8') as f:
	reader = csv.reader(f)
	for line in reader:
		display_name=line[5]
		status[display_name]=line[14]
		
print(status)





#using ibm language_translator to translate user status from japanese to english
language_translator = LanguageTranslator(
   username='cfae4f65-e562-441e-9bca-f90751c59541',
   password='fQqF7xiK1Mij')
for key in status:
	key=language_translator.translate(key,source='ja', target='en')  
for key in status:
	status[key] = language_translator.translate(text=status[key],source='ja', target='en')
	#print(json.dumps(status[key], indent=2, ensure_ascii=False))


#getting sentiments	
sentimentpolarity=dict()
sentimentsub=dict()
for key in status:
	sentimentpolarity[key]= TextBlob(status[key]).sentiment.polarity
	sentimentsub[key]=TextBlob(status[key]).sentiment.subjectivity
print(sentimentpolarity)
print(sentimentsub)


# tokenizing the status of user into words
words = list()
for key in status:
	for i in word_tokenize(status[key]):
		words.append(i)
		
#print(words)


# removing stop words
stop_words = set(stopwords.words("English"))
finalwords = list()
for w in words:
	if w not in stop_words:
		finalwords.append(w)
print(finalwords)


#creating dictionary of term frequencies 
wordfreq = defaultdict(int)
for w in finalwords:
	wordfreq[w] +=1 
print(wordfreq)

#to create various topcis by topic modeling with mallet,creating corpus of textual files each with status
count=0
for key in status:
	count+=1
	outputstatus = open(str(count)+'.txt',encoding='utf-8')
	outputstatus.write(status[key])


#commands to train the mallet lda
# bin\mallet import-dir --input data\mastodondata\ --output data\mastodon.mallet --keep-sequence --remove-stopwords
# bin\mallet train-topics --input data\mastodon.mallet --num-topics 5 --output-doc-topics data\doc-topics-mastodon.txt --output-topic-keys data\topic-keys-mastodon.txt --random-seed 1





	

