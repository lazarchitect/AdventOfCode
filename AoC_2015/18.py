
grid = []

for line in open("18.txt").readlines():
	grid.append([])
	for char in line:
		if char==".": grid[len(grid)-1].append(0)
		elif char=="#": grid[len(grid)-1].append(1)

def printgrid():
	for i in grid:
		for j in i:
			print(j, end="")
		print()	

def count():
	return sum([sum([i for i in j]) for j in grid])

def neighbors(y, x):
	pass
	
def update():
	old = grid
	new = old
	for eachLine in grid:
		for eachCell in eachLine:
			 
	
	
	
for x in range(100):
	update()
	
printgrid()
print(count())