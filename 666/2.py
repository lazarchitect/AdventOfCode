loc = 5
result1 = ""

for each in open("2.txt").readlines():
	for c in each:
		if c == "U" and loc not in [1,2,3]: loc -= 3
		if c == "L" and loc not in [1,4,7]: loc -= 1
		if c == "R" and loc not in [3,6,9]: loc += 1
		if c == "D" and loc not in [7,8,9]: loc += 3
	result1+=str(loc)


grid = [
	[-1, -1,  1, -1, -1],
	[-1,  2,  3,  4, -1],
	[ 5,  6,  7,  8,  9],
	[-1, 10, 11, 12, -1],
	[-1, -1, 13, -1, -1]
]


loc = [2, 0]
result2 = ""

for each in open("2.txt").readlines():
	for c in each:
		try:
			if c == "U" and grid[loc[0]-1][loc[1]]!=-1: loc[0] -= 1
			if c == "L" and grid[loc[0]][loc[1]-1]!=-1: loc[1] -= 1
			if c == "R" and grid[loc[0]][loc[1]+1]!=-1: loc[1] += 1
			if c == "D" and grid[loc[0]+1][loc[1]]!=-1: loc[0] += 1
		except IndexError:
			print(grid[loc[0]][loc[1]], c)
	x = grid[loc[0]][loc[1]]
	if  (x==10): result2+="A"
	elif(x==11): result2+="B"
	elif(x==12): result2+="C"
	elif(x==13): result2+="D"
	else: result2+=str(grid[loc[0]][loc[1]])



print("Part 1: "+result1)
print("Part 2: "+result2)