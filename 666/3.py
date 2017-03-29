total1 = 0

for each in open("3.txt").readlines():
	sides = each.split("  ")
	try:
		x = int(sides[1])
		try:
			y = int(sides[2])
			try:
				z = int(sides[3][:-1])
			except ValueError:
				z = int(sides[4][:-1])	
		except ValueError:
			y = int(sides[3])
			z = int(sides[4][:-1])
	except ValueError:
		x = int(sides[2])
		y = int(sides[3])
		z = int(sides[4][:-1])
	
	b = max(x, y, z)

	if (b==x and x<y+z) or (b==y and y<x+z) or (b==z and z<x+y): total1+=1
	
left = []
center = []
right = []	
count = 0
total2 = 0
	
for each in open("3.txt").readlines():
	sides = each.split("  ")
	try:
		x = int(sides[1])
		try:
			y = int(sides[2])
			try:
				z = int(sides[3][:-1])
			except ValueError:
				z = int(sides[4][:-1])	
		except ValueError:
			y = int(sides[3])
			z = int(sides[4][:-1])
	except ValueError:
		x = int(sides[2])
		y = int(sides[3])
		z = int(sides[4][:-1])
	
	#x, y, and z are established
	left.append(x)
	center.append(y)
	right.append(z)
	count+=1

print(count)	
	
for i in range(int(count/3)):
	x = left[0]
	y = left[1]
	z = left[2]
	left = left[3:]
	b = max(x, y, z)
	if (b==x and x<y+z) or (b==y and y<x+z) or (b==z and z<x+y): total2+=1
	
	x = center[0]
	y = center[1]
	z = center[2]
	center = center[3:]
	b = max(x, y, z)
	if (b==x and x<y+z) or (b==y and y<x+z) or (b==z and z<x+y): total2+=1
	
	x = right[0]
	y = right[1]
	z = right[2]
	right = right[3:]
	b = max(x, y, z)
	if (b==x and x<y+z) or (b==y and y<x+z) or (b==z and z<x+y): total2+=1
	
	
print("Part 1: "+str(total1))
print("Part 2: "+str(total2))