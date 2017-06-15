grid = []

code = 20151125

for i in range(1,6060):
	grid.append([])
	for j in range(i):
		grid[i-1-j].append(code)
		code = (code * 252533) % 33554393

print("Part 1:", grid[2980][3074])