
def diffCost(x):
	return sum(range(1, x+1))

# print(diffCost(2))
# exit()

def moveCost(positions, location):
	total = 0
	for position in positions:
		total += abs(position - location)
	return total

def moveDiffCost(positions, location):
	total = 0
	for position in positions:
		diff = abs(position - location)
		total += diffCost(diff)
	return total

with open("7.txt", "r") as f:
	
	positions = [int(x) for x in f.read().split(",")]

	smallest = min(positions)
	largest = max(positions)

	lowestCost = 200000000

	for p in range(smallest, largest):
		cost = moveCost(positions, p)
		if cost < lowestCost:
			lowestCost = cost
	#brute force.
	print("Part 1:", lowestCost)

	lowestDiffCost = 200000000

	for p in range(smallest, largest):
		cost = moveDiffCost(positions, p)
		if cost < lowestDiffCost:
			lowestDiffCost = cost
	#HELLA brute force.
	print("Part 2:", lowestDiffCost)