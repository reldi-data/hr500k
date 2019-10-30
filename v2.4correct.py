# !/usr/bin/python
# -*- coding: utf8 -*-

# usage: e.g.  python v2.4correct.py ../git_SETimes.SR/SETimes.SRPlus/set.sr.plus.conll replacements.txt > temp.txt
# assumes "original" conll file format 
# print might need to be adjusted for running with python3


import re
import codecs
import sys

deptable = []
dep_replace = {}
rel_replace = {}

corrinfile = sys.argv[2]
depinfile = sys.argv[1]

corrections = codecs.open(corrinfile, "r", "utf-8")
depdata = codecs.open(depinfile, "r", "utf-8")

""" UPOS correction function """
def correct_upos(old, new):
	expr = r'.+'+re.escape(old)+ r'(.+)'
	if re.match(expr, deptable[i][8]):
		msd = re.search(expr, deptable[i][8]).group(1)
		deptable[i][8] = "UposTag="+new+msd

""" Import specific corrections from a file """
for line in corrections:						#read the list of replacements from a file 
	items = line.split()
	if items[0] == "rel":                        # e.g. replacements.txt
		rel_replace[(items[1],items[2])] = items[3]
	else:
		dep_replace[(items[1],items[2])] = items[3]

""" MAIN """
for line in depdata:							#read the file to be corrected
	line = re.sub(r'\n', '', line)					# instead of chomp in Perl				
	
#	"""if the input line is empty, process and delete the table"""  #triple quotes don't work within a block
	if len(line) == 0:
		metalines = 0
		for i in range(len(deptable)):		
			if 	deptable[i][0][0] == "#":         # extract metadata
				metalines += 1
				metadata = deptable[i][0].split()	
				if metadata[1] == "sent_id":
					sent_ID = metadata[3]
				print deptable[i][0].encode("utf-8")                  #print metadata
			else:
				line = "" 
				word_ID = str(i - metalines + 1) # for sentID and text that precede the table
				deprel = deptable[i][7].split(":")
				dep = str(deprel[0]) 
				rel = ':'.join(deprel[1:])
#			""" replacements """
				if (sent_ID, word_ID) in dep_replace:   #punct-causes-nonproj, advmod deps
					dep = dep_replace[(sent_ID, word_ID)]
				if (sent_ID, word_ID) in rel_replace:
					rel = rel_replace[(sent_ID, word_ID)]
				deptable[i][7] = dep+":"+rel
				if rel == "mark":                           #'mark' should not be 'PRON'
					if re.match(r'.+PRON.+', deptable[i][8]):  
						deptable[i][7] = deprel[0]+":"+"nsubj"
				if rel == "nummod":                             #'nummod' should be 'NUM'
					correct_upos('ADJ','NUM')
				if rel =="det:numgov":                          #'det' is 'ADV'"
					correct_upos('ADV','DET')
				if rel =="advmod":                          
					correct_upos('SCONJ','ADV')     # 'advmod' is 'SCONJ', ADP, NOUN
					if re.match(r'.+ADP.+', deptable[i][8]):  
						deptable[i][7] = deprel[0]+":"+"case"
					if re.match(r'.+NOUN.+', deptable[i][8]):  
						deptable[i][7] = deprel[0]+":"+"nmod"																
				if rel =="det":                    # 'det' is ADJ, PART, CCONJ, X, NUM
					correct_upos('ADJ','DET')				 	
					correct_upos('PART','DET')
					correct_upos('CCONJ','DET')
					correct_upos('X','DET')		
					correct_upos('NUM','DET')
				if rel == "goeswith":					# in hr500k, e.g. "do sada" 
					if re.match(r'.+ADP.+', deptable[i][8]):
						deptable[i][7] = deprel[0]+":"+"case"	
					else: 
						deptable[i][7] = deprel[0]+":"+"amod"
				if rel == "appos":                 # in hr500k mostly wrong rel appos
					if int(dep) >= i:
						deptable[i][7] = deprel[0]+":"+"amod"
				if rel == "flat:foreign":          # in hr500k mostly indeclinable
					if int(dep) >= i:
						deptable[i][7] = deprel[0]+":"+"nmod"
				if rel == "conj":                  # in hr500k coordinated modifiers 
					if int(dep) >= i:
						if re.match(r'.+NUM.+', deptable[i][8]):
							deptable[i][7] = deprel[0]+":"+"nummod"
						else:
							deptable[i][7] = deprel[0]+":"+"amod"																		
#			""" concatenate and print the result without the last tab """
				for j in range(len(deptable[i])):
					line = line + deptable[i][j]+"\t"
				line = line[:-1]    # remove the last tab				
				print line.encode("utf-8")					
		print												
		deptable = []
	
#	""" for all the other lines, store the input into a table"""	
	else:
		lineitems = line.split("\t")
		deptable.append(lineitems)
		
