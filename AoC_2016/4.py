def isRealRoom(letters, checksum):
	return letters == checksum

def getLetters(name):
	lettersDict = {}z
	for character in name:
		if character in lettersDict.keys():
			lettersDict[character] += 1
		else: 
			lettersDict[character] = 1
	for 		

def extractName(roomcode):
	return roomcode[0:firstNumeralIndex(roomcode) - 1].split("-").join("") 
	#slices dont count the last one, so end on the separating dash. 
	#and remove the hyphens.

def firstNumeralIndex(roomcode):
	x = 0
	for i in roomcode:
		if i.isdigit():
			return x
		else:
			x += 1	



for each in open("4.txt").readlines():
	pass