loc = [0,0]
facing = "north"
from time import sleep
for each in open("1.txt").read().split(", "):
	d = int(each[1:])
	if(d > 180): print(loc)
	if(each[0] == "L"):
		if(facing=="north"):
			facing = "west"
			loc[0]-= int(d)
		elif(facing=="south"):
			facing = "east"
			loc[0]+= int(d)
		elif(facing=="east"):
			facing = "north"
			loc[1]+= int(d)
		elif(facing=="west"):
			facing = "south"
			loc[1]-= int(d)		
	
	else: #R
		if(facing=="north"):
			facing = "east"
			loc[0]+= int(d)
		elif(facing=="south"):
			facing = "west"
			loc[0]-= int(d)
		elif(facing=="east"):
			facing = "south"
			loc[1]-= int(d)
		elif(facing=="west"):
			facing = "north"
			loc[1]+= int(d)

x = abs(loc[0]) + abs(loc[1])
		
print("Part 1: "+ str(x))