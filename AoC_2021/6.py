
with open("6.txt", "r") as f:
	content = f.read()

lanternfishAges = [int(x) for x in content.split(",")]

# lanternfishAges = [3,4,3,1,2]

numDays = 256

for day in range(numDays):
	print(day)
	babiesBorn = 0
	for index, age in enumerate(lanternfishAges):
		if age == 0:
			lanternfishAges[index] = 6
			babiesBorn += 1
		else:
			lanternfishAges[index] -= 1
	for x in range(babiesBorn):
		lanternfishAges.append(8)

	if day == 80:
		print("Part 1:", len(lanternfishAges))

print("Part 2:", len(lanternfishAges))