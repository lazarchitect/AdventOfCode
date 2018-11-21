#aoc 2017 #6

"""
basic idea:
for each string: 
	for each char:
		
		put it in the dict at the right spot.
		
		if that dict doesnt already contain that letter,
			set the key to the letter and the value to 1
		else	
			bump the value up by 1

	at the end,
	the key in each dict with the highest value number is the letter we want		
"""

chars = [{}, {}, {}, {}, {}, {}, {}, {}] #will have 8 spots, each spot is a dict

def getMaxValue(d):
	retval = ""
	maxnum = 0
	for i in d.keys():
		if d[i] > maxnum:
			maxnum = d[i]
			retval = i
	return retval	

def getMinValue(d):
	retval = ""
	maxnum = 4000000
	for i in d.keys():
		if d[i] < maxnum:
			maxnum = d[i]
			retval = i
	return retval		


with open("6.txt", "r") as f:

	for line in f.read().split("\n")[:-1]:
		# print(line)
		for x in range(0, 8):
			dictionary = chars[x]
			letter = line[x]
			
			if letter in dictionary:
				dictionary[letter] += 1

			else:
				dictionary[letter] = 1

# print(chars)				

Part1 = ''.join([getMaxValue(i) for i in chars])
Part2 = ''.join([getMinValue(i) for i in chars])

print("Part 1:" + Part1)
print("Part 2:" + Part2)