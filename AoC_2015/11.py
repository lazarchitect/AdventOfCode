password = "hepxcrrq"

alph = "abcdefghijklmnopqrstuvwxyz"

def increment(s):
	alphIndex = alph.find(s[len(s)-1]) #alphIndex is a number
	if alphIndex==25:
		return increment(s[:len(s)-1]) + "a"
	else:
		return s[:len(s)-1] + alph[alphIndex+1]
	
def contains_straight(s):
	for i in range(len(s)-2):
		if((alph.find(s[i]) == alph.find(s[i+1])-1) and (alph.find(s[i]) == alph.find(s[i+2])-2)):
			return True
	return False
	
def contains_iol(s):
	return(("i" in s) or ("o" in s) or ("l" in s))
	
def contains_twopairs(s):
	pairs = 0
	index = -1
	for i in range(len(s)-1):
		if(s[i] == s[i+1] and i!=index):
			pairs+=1
			index = i+1
			continue
	return pairs==2		
	
def update(s):
	while True:
		s = increment(s)
		if contains_straight(s):
			if contains_iol(s)==False:
				if contains_twopairs(s):
					return s

print("Part 1: "+update("hepxcrrq"))
print("Part 2: "+update("hepxxyzz"))