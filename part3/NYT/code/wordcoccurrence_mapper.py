#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import sys
sys.path.append("/")
import re
import io
import nltk
#from nltk.corpus import stopwords

#Top 10 words found in CommonCrawl
top_words = ['year', 'state', 'trump', 'people', 'time', 'police', 'woman', 'report', 'case', 'charge']	

from nltk.corpus import wordnet
lmtzr = nltk.WordNetLemmatizer().lemmatize
def get_wordnet_pos(treebank_tag):
	if treebank_tag.startswith('J'):
		return wordnet.ADJ
	elif treebank_tag.startswith('V'):
		return wordnet.VERB
	elif treebank_tag.startswith('N'):
		return wordnet.NOUN
	elif treebank_tag.startswith('R'):
		return wordnet.ADV
	else:
		return wordnet.NOUN

def normalize_text(text):
	word_pos = nltk.pos_tag(nltk.word_tokenize(text))
	lemm_words = [lmtzr(sw[0], get_wordnet_pos(sw[1])) for sw in word_pos]
	return [x.lower() for x in lemm_words]

#The context for the co ocurrance in nytimes data is article. Each article is present in separate file and each file has single line.
for text in sys.stdin:
	#Clean data
	text = re.sub(r'http\S+', '',text)
	text = text.replace("'s","")
	text = text.replace('"', '').replace("'", "")
	text = text.replace("\\.(?=\\s|$)", " ")
	text = re.sub('[^a-zA-Z0-9\n]', ' ', text)
	text = ''.join([i for i in text if not i.isdigit()])
	text = re.sub(' +', ' ', text)
	text=' '.join( [w for w in text.split() if len(w)>1] )
	text=text.lower()
	text = re.sub(" mr | said | new | still | one | would | also | two | u | like "," ", text)	
	if text == '':
		continue
	words = text.split()

	#Remove stop words
	list_of_words = list()
	stop_words = open("stopwords_clean.txt","r")
	stop_words1 = stop_words.read().split()
	pattern = re.compile(r'\b(' + r'|'.join(words for words in stop_words1) + r')\b\s*')
	#pattern = re.compile(r'\b(' + r'|'.join(words for words in stop_words1) + r')\b\s*')
	text2 = pattern.sub('', text)
	list_of_words=normalize_text(text2)
	for index, word1 in enumerate(list_of_words):
		for word2 in list_of_words[(index+1):]:
			if(word2 == word1): continue
			pair = word1+"-"+word2
			if(word1 in top_words or word2 in top_words):
				print('%s,%s' % (pair, 1))




