from hashlib import md5
from time import sleep

startstring = "pgflpeqp"

paths = []

def shortestPath():
	shortest = ""
	length = 1000**44
	for i in paths:
		if len(i) < length:
			shortest = i
			length = len(i)
	return shortest

def longestPath():
	longest = ""
	length = 0
	for i in paths:
		if len(i) > length:
			longest = i
			length = len(i)
	return longest				

def countLetter(letter, string):
	count = 0
	for char in string:
		if letter == char:
			count += 1
	return count

def valid(key):
	return key in ['b', 'c', 'd', 'e', 'f']

def topRow(roomstring):
	return countLetter("U", roomstring) == countLetter("D", roomstring)

def bottomRow(roomstring):
	return countLetter("D", roomstring) == countLetter("U", roomstring) + 3

def leftCol(roomstring):
	return countLetter("L", roomstring) == countLetter("R", roomstring)

def rightCol(roomstring):
	return countLetter("R", roomstring) == countLetter("L", roomstring) + 3	

def checkRoom(roomstring): #recursive. needs floor case and delve case
	
	# sleep(1)

	# base case. this is the room!
	if countLetter("D", roomstring) == countLetter("U", roomstring) + 3 and countLetter("R", roomstring) == countLetter("L", roomstring) + 3:
		paths.append(roomstring)
		return

	hashstring = md5(roomstring.encode('utf-8')).hexdigest()
 
	# print(roomstring)	

	# print(hashstring)

	if valid(hashstring[0]) and topRow(roomstring) == False:
		checkRoom(roomstring + "U")

	if valid(hashstring[1]) and bottomRow(roomstring) == False:
		checkRoom(roomstring + "D")

	if valid(hashstring[2]) and leftCol(roomstring) == False:
		checkRoom(roomstring + "L")
		
	if valid(hashstring[3]) and rightCol(roomstring) == False:
		checkRoom(roomstring + "R")		


checkRoom(startstring)

print("Part 1: " + shortestPath()[len(startstring):])
print("Part 2: " + str(len(longestPath()[len(startstring):])))
