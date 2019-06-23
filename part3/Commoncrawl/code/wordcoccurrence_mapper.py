#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import sys
sys.path.append("/")
import re
import io
import nltk
import sh
# nltk.download('stopwords')
# from nltk.corpus import stopwords 
#nltk.download('averaged_perceptron_tagger')
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
top_words = ['state', 'time', 'trump', 'people', 'report', 'police', 'year', 'woman', 'case', 'charge']
##hdfsdir = '/test'
##allFiles = [ line.rsplit(None,1)[-1] for line in sh.hdfs('dfs','-ls',hdfsdir).split('\n') if len(line.rsplit(None,1))][1:]
##for fname in allFiles:
##	with open(fname,encoding='unicode_escape') as outfile:
hdf=sys.stdin
for text in hdf:
        for text in outfile:
            text = re.sub(r'http\S+', '',text)
            text = text.replace("'s","")
            text = text.replace('"', '').replace("'", "")
            text = text.replace("\\.(?=\\s|$)", " ")
            text = re.sub('[^a-zA-Z0-9\n]', ' ', text)
            text = re.sub("<.*>|<|!|\.|@|#|\$|\*|:|%|\+|…|\\\\|\/|«|»|···|\||\•|\?|\(|\)|=|-|&|;|\_|—|~|¯|\{|\}|\[|\]|£|€|¥|¿|–", " ", text)
            text = ''.join([i for i in text if not i.isdigit()])
            text = re.sub(' +', ' ', text)
            text=' '.join( [w for w in text.split() if len(w)>1] )
            text=text.lower()
            stop_words = open("stopwords_clean.txt","r")
            stop_words1 = stop_words.read().split()
            pattern = re.compile(r'\b(' + r'|'.join(words for words in stop_words1) + r')\b\s*')
            text2 = pattern.sub('', text)
            t=normalize_text(text2)
            for word in t:
                if word in top_words:
                    for word2 in t:
                        if word2==word:
                            continue
                        print(word+"-"+word2+",1")
