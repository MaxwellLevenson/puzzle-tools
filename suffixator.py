# Searches for word that can be mashed with all words in input set to get all new valid words
# Suffixator name credit to Shai
# Run with python suffixator.py arg1 arg2 ...
# 
# E.g. Input [sum, up, list, mate, point], Output: Check
# checksum, checkup, checklist, checkmate, checkpoint
import sys

words = set(line.split('/', 1)[0].strip() for line in open('./en_US.dic'))
outs = []
found = True
if len(sys.argv) > 1:
	for w in words:
		for v in sys.argv[1:len(sys.argv)]:
			if w + v not in words and v + w not in words:
				found = False
				break;
		if found:
			outs.append(w)
		found = True

print outs
