#!/usr/bin/env python3.6

"""reducer.py"""
from operator import itemgetter
import sys
current_word = None
current_count = 0
word = None
seen=set()
result={}
# input comes from STDIN
for line in sys.stdin:
#with open("wc.txt","r",encoding = 'unicode_escape') as myfile:	
	#lines = myfile.read()
	#print(lines)
	#for line in lines:
	#line = line.strip()
	word, count = line.split(',',1)
	try:
		count = int(count)
	except ValueError:
		continue
	if word not in seen:
		seen.add(word)
		current_count=count
		result[word]=current_count
	else:
		current_count=count+result[word]
		result[word]=current_count
	
#for key,value in result.items():
	#print(key,value)

a1_sorted_keys = sorted(result, key=result.get, reverse=True)
for r in a1_sorted_keys:
    print(r, result[r])
		
