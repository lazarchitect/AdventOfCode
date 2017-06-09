rawChars = 0
codeChars = 0
metaChars = 0

def createMeta(s):
	retval = 2
	for i in s:
		retval+=1
		if i == "\"" or i == "\\":
			retval+=1
	return retval		 

for E in open("8.txt").readlines():
	rawChars += len(E[:-1])
	codeChars += len(eval(E))
	metaChars += createMeta(E[:-1])
	
print("Part 1: " + str(rawChars - codeChars))
print("Part 1: " + str(metaChars - rawChars))