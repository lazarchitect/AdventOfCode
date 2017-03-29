floor = 0
index = 0
basement = False

for c in open("1.txt").read():
	if c == '(':
		floor+=1
	else:
		floor-=1
	if(basement==False):
		index+=1
		if(floor==-1):
			basement = True

print("Part 1: "+str(floor))
print("Part 2: "+str(index))			