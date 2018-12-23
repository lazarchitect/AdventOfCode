total = 0

with open("2.txt") as f:
	for line in f:
		
		arr = line.split("\t")
		
		for i in range(len(arr)):
			arr[i] = int(arr[i])

		biggest = max(arr)
		smallest = min(arr)
		diff = biggest - smallest
		total+=diff

print("Part 1:", total)

with open("2.txt") as f:
	for line in f:
		
		arr = line.split("\t")
		
		for i in range(len(arr)):
			arr[i] = int(arr[i])

				

		diff = #############

		total+=diff