def getNeighborValue(grid, y, x):
	if y < 0 or x < 0 or y > 99 or x > 99:
		return 0
	if x in [0, 99] and y in [0, 99]:
		return 1
	return grid[y][x]

def neighborCount(grid, y, x):
	
	# print(grid[y][x])	
	retval = 0
	for horz1 in [-1, 0, 1]:
		retval += getNeighborValue(grid, y-1, x+horz1)
	for horz2 in [-1, 1]:
		retval += getNeighborValue(grid, y, x+horz2)
	for horz3 in [-1, 0, 1]:
		retval += getNeighborValue(grid, y+1, x+horz3)
	return retval


def update(oldgrid):
	newgrid = []

	for y in range(100):

		newgrid.append([])

		for x in range(100):

			n = neighborCount(oldgrid, y, x)
			status = oldgrid[y][x]

			if x in [0, 99] and y in [0, 99]:
				 newgrid[y].append(1)

			elif status == 1:

				if n != 2 and n != 3:
					newgrid[y].append(0)
				else:
					newgrid[y].append(1)

			else: #status = 0

				if n == 3:
					newgrid[y].append(1)
				else:
					newgrid[y].append(0)

	return newgrid								


grid = []

for line in open("18.txt").readlines():
	grid.append([])
	for char in line:
		if char==".": grid[len(grid)-1].append(0)
		elif char=="#": grid[len(grid)-1].append(1)
	
for x in range(100):
	grid = update(grid)
	# print(x)

print("Part 2:", sum([sum(i) for i in grid]))