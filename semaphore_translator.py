# Semaphore translator

# Reference image: https://flagexpressions.files.wordpress.com/2010/03/semaphore-flag-codes3.jpg

# 8 positions for a semaphore arm, up/down/left/right/and any combination of adjoining directions for a diagonal
# positions referred to as follows:
 #     0
 #   7   1
 # 6       2
 #   5   3
 #     4

outputs = {(4, 5): 'A', (4, 6): 'B', (4, 7): 'C', (0, 4): 'D', (1, 4): 'E', (2, 4): 'F', (3, 4): 'G',
	(5, 6): 'H', (5, 7): 'I', (0 ,2): 'J', (0, 5): 'K', (1, 5): 'L', (2, 5): 'M', (3, 5): 'N', (6, 7): 'O',
	(0, 6): 'P', (1, 6): 'Q', (2, 6): 'R', (3, 6): 'S', (0, 7): 'T', (1, 7): 'U', (0, 3): 'V', (1, 2): 'W',
	(1, 3): 'X', (2, 7): 'Y', (2, 3): 'Z'}

# sanitize input
def check(pos):
	for i in pos:
		try:
			i = int(i)
			if i > 7 or i < 0:
				print("Not in position range of values (from 0 to 7)")
				return 1 
		except ValueError:
	   		print("That's not an int!")
	   		return 1
	return 0

# given two arm position inputs, ouputs semaphore character
def translate_tuple((one, two)):
	if check([one, two]) == 1:
		return
	one = int(one)
	two = int(two)
	less = one if one < two else two
	more = one if less == two else two
	pair = (less, more)
	try:
		return(outputs[pair])
	except KeyError: 
		print("Not a valid semaphore!")

def translate_time((hr, mn)):
	one = 0
	two = 0
	one = int((mn + 4.5) / 7.5)
	one = one if mn < 57 else 0

	tot_min = (hr % 12) * 60 + mn

	if tot_min < 45 or tot_min >= 11 * 60 + 15:
		two = 0
	elif tot_min < 2 * 60 + 15:
		two = 1
	elif tot_min < 3 * 60 + 45:
		two = 2
	elif tot_min <  5 * 60 + 15:
		two = 3
	elif tot_min < 6 * 60 + 45:
		two = 4
	elif tot_min < 8 * 60 + 15:
		two = 5
	elif tot_min < 9 * 60 + 45:
		two = 6
	else:
		two = 7

	return translate_tuple((one, two))

print(chr(27) + "[2J")
print("Arm position diagram:\n" + "    0    \n" + "  7   1\n" + "6       2\n" + "  5   3\n" + "    4")
ans = input("Positions (1) or time (2)? (Use q to quit at any time): ")
while 1:
	if ans == 1:
		inp = input("Please enter a tuple of positions in the form (x, y):\n")
		print translate_tuple(inp)
	elif ans == 2:
		hrs = input("Hours?: ")
		mins = input("Minutes?: ")
		print(translate_time((hrs, mins)))