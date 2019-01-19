def firstNumeralIndex(roomcode):
	"""finds the first numerical character in a string.  
	*Parameters: the string in question  
	*Returns: the index of the character
	"""
	x = 0
	for i in roomcode:
		if i.isdigit():
			return x
		else:
			x += 1	

def getLetters(name):
	"""Gets a dict of letters and their frequencies of an alphabetic (not alphabetically sorted) string. 
	Then, finds the 5 letters with the highest frequencies (ties solved by alphabetical order), and returns all 5 together in an ordered string.
	*Parameters: the string  
	*Returns: the dict
	"""
	lettersDict = {}
	for character in name:
		if character in lettersDict.keys():
			lettersDict[character] += 1
		else: 
			lettersDict[character] = 1

			
	

def isRealRoom(letters, checksum):
	return letters == checksum

def tokenize(roomcode):
	fni = firstNumeralIndex(roomcode)
	name = "".join(roomcode[0: fni - 1].split("-"))
	#slices dont count the last one, so end on the separating dash. 
	#and remove the hyphens.
	sectorID = roomcode[fni: fni + 3]
	checksum = roomcode[fni+4: fni + 9]
	return (name, sectorID, checksum)



for roomcode in open("4.txt").readlines():
	name, sectorID, checksum = tokenize(roomcode)

	getLetters(name)