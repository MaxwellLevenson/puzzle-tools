import os

# Searches for word that can be mashed with all words in input set to get all new valid words
# Suffixator name credit to Shai
# Run with python suffixator.py arg1 arg2 ...
# 
# E.g. Input [sum, up, list, mate, point], Output: Check
# checksum, checkup, checklist, checkmate, checkpoint
def suffixator(arr):
	words = set(line.split('/', 1)[0].strip() for line in open('./en_US.dic'))
	outs = []
	found = True
	if len(arr) >= 1:
		for w in words:
			for v in arr:
				if w + v not in words and v + w not in words:
					found = False
					break;
			if found:
				outs.append(w)
			found = True

	print outs


# Converts a single number (or list of numbers) from 1-26
# into capital characters for puzzles answers.
# E.g. Inputs -> Outputs: 13 -> M, [13, 1, 24] -> MAX
def num2let(arr):
	ans = []
	diff_to_A = 64
	tmp = 0
	try: 
		tmp = int(arr)
		if tmp > 26 or tmp < 1:
			print "Input was not in the range of 1-26."
			return
		ans = chr(tmp + diff_to_A)
		print ans
	except TypeError:
		try:
			tmp = [ int(x) for x in arr ]
			for i, item in enumerate(tmp):
				if item > 26 or item < 1:
					print "Input " + str(i+1) + " was not in the range of 1-26."
					return
			ans = [ chr(x + diff_to_A) for x in arr ]
			print "".join(ans)
		except TypeError:
			print "Bad input, please enter a letter or a list of letters deliminated by commas."
			return

# Run semaphore translation script
# See 'semaphore_translator.py'
def semaphore_translator():
	os.system('python ./semaphore_translator.py')