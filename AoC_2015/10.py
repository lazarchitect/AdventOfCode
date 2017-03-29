initial = "1321131112"


second =  "11131221133112"
	
def lookAndSay(s):
	retval=""
	i = 0
	while i < len(s):
		count = 1
		while(i+1<len(s) and s[i] == s[i+1]):
			count+=1
			i+=1
			
		retval+=(str(count) + s[i])
		i += 1
	return retval		
		
		
for i in range(40):
	print(len(initial))
	initial = lookAndSay(initial)
	
print("Part 1: "+str(len(initial)))

for i in range(10):
	print(len(initial))
	initial = lookAndSay(initial)

print("Part 2: "+str(len(initial)))