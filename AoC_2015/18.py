
grid = []

for line in open("18.txt").readlines():
	grid.append([])
	for char in line:
		if char==".": grid[len(grid)-1].append(0)
		elif char=="#": grid[len(grid)-1].append(1)
			 


def update(oldgrid):
	newgrid = []

	

	return newgrid

	
for x in range(100):
	grid = update(grid)

print("Part 1:", sum([sum(i) for i in grid]))