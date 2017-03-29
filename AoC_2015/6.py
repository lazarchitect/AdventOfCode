def part1():
	lights = [[0 for c in range(1000)] for r in range(1000)]
	for each in open("6.txt").readlines():
		words = each.split(" ")
		# print(words)
		if(words[0]=="toggle"):
			x1 = words[1].split(",")[0]
			y1 = words[1].split(",")[1]
			x2 = words[3].split(",")[0]
			y2 = words[3].split(",")[1][0:len(words[3].split(",")[1])]
			for i in range(int(x1), int(x2)+1):
				for j in range(int(y1), int(y2)+1):
					lights[i][j] = abs(lights[i][j]-1)
		
		else:
			x1 = words[2].split(",")[0]
			y1 = words[2].split(",")[1]
			x2 = words[4].split(",")[0]
			y2 = words[4].split(",")[1][0:len(words[4].split(",")[1])]
			if(words[1] == "on"):
				for i in range(int(x1), int(x2)+1):
					for j in range(int(y1), int(y2)+1):
						lights[i][j] = 1
			
			else:
				for i in range(int(x1), int(x2)+1):
					for j in range(int(y1), int(y2)+1):
						lights[i][j] = 0
						
	total = 0
	for i in lights:
		for j in i:
			total+=j	
	return total
	
def part2():
	lights = [[0 for c in range(1000)] for r in range(1000)]
	for each in open("6.txt").readlines():
		words = each.split(" ")
		# print(words)
		if(words[0]=="toggle"):
			x1 = words[1].split(",")[0]
			y1 = words[1].split(",")[1]
			x2 = words[3].split(",")[0]
			y2 = words[3].split(",")[1][0:len(words[3].split(",")[1])]
			for i in range(int(x1), int(x2)+1):
				for j in range(int(y1), int(y2)+1):
					lights[i][j] += 2
		
		else:
			x1 = words[2].split(",")[0]
			y1 = words[2].split(",")[1]
			x2 = words[4].split(",")[0]
			y2 = words[4].split(",")[1][0:len(words[4].split(",")[1])]
			if(words[1] == "on"):
				for i in range(int(x1), int(x2)+1):
					for j in range(int(y1), int(y2)+1):
						lights[i][j] += 1
			
			else:
				for i in range(int(x1), int(x2)+1):
					for j in range(int(y1), int(y2)+1):
						if(lights[i][j]!=0): lights[i][j] -= 1
						
	total = 0
	for i in lights:
		for j in i:
			total+=j	
	return total
	
print("Part 1: "+str(part1()))
print("Part 2: "+str(part2()))