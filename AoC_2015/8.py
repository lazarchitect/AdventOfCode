codeChars = 0
stringChars = 0

print()

def a(s):
	retval = 2
	for i in s:
		retval += 1
		if i=="\\" or i=="\"":
			retval+=1
		try:
			e = ord(i)
			print(i, e)
			retval += 3
		except ValueError:
			pass
	return retval
	
for each in open("8.txt").readlines():
	codeChars += a(each)
	stringChars += len(each)
	
print("Part 1: " + str(codeChars-stringChars))