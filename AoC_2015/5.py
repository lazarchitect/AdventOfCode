def vowels(s):
	v = 0
	for i in s:
		if i in "aeiou":
			v+=1
	return v > 2		

def doubles(s):
	for i in range(1, len(s)):
		if s[i] == s[i-1]:
			return True
	return False	
	
def bans(s):
	return ("ab" not in s) and ("cd" not in s) and ("pq"  not in s) and ("xy" not in s)		

def isNice(s):
	return vowels(s) and doubles(s) and bans(s)
	
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""	
def sandwich(s):
	for i in range(2, len(s)):
		if s[i] == s[i-2]:
			return True
	return False		
	
def pairs(s):
	for i in range(1, len(s)):
		for j in range(1, len(s)):
			if s[j-1:j+1]==s[i-1:i+1] and j!=i and j!=i+1 and j!=i-1:
				return True
	return False
	
def isSuperNice(s):
	return sandwich(s) and pairs(s)
part1 = 0
part2 = 0
for each in open("5.txt").readlines():
	if isNice(each):
		part1+=1
	if isSuperNice(each):
		part2+=1
	
print("Part 1: "+ str(part1))	
print("Part 2: "+ str(part2))