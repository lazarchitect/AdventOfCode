d = eval(open("12.txt").read())

total = 0

def gnrDict(someDict):
	global total
	
	####Part 2 Code
	if someDict == "red":
		return 0
	for i in someDict:
		if someDict[i] == "red":
			return 0
	
	for i in someDict:		
		if type(someDict[i]) == int:  total+=someDict[i]
		if type(someDict[i]) == list: gnrList(someDict[i])
		if type(someDict[i]) == dict: gnrDict(someDict[i])

def gnrList(someList):
	global total
	for i in someList:	
		if type(i) == int:  total += i
		if type(i) == list: gnrList(i)
		if type(i) == dict: gnrDict(i)
			
gnrDict(d)					
print("Part 2: "+str(total))