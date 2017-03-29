import hashlib

i = 100
cool = True
while(True):
	i+=1
	x = hashlib.md5(("iwrupvqb"+str(i)).encode('utf-8')).hexdigest()
	
	if i % 10000 == 0: print(".", end="")
	
	if(cool):
		if x[0:5] == "00000":
			cool = False
			print("Part 1: "+str(i))
	
	if x[0:6] == "000000":
		print("Part 2: "+str(i))
		break
		
		