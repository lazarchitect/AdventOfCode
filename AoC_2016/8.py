arr = [([0 for j in range(50)]) for i in range(6)]

for each in open("8.txt").readlines():
	words = each.split(" ")
	if(words[0] == "rect"):
		for i in range(int(words[1][0:words[1].index("x")])):
			for j in range(int(words[1][words[1].index("x")+1:words[1].index("x")+2])):
				arr[j][i] = "S"
		continue
	num = int(words[2][words[2].index("=")+1:])
	amount = int(words[4][:-1])
	if words[1] == "column":
		old = []
		for x in range(6):
			old.append(arr[x][num])
		for x in range(6):
			arr[x][num] = old[(x-amount)%6]	 
	else: arr[num] = [arr[num][i] for i in range(50-amount, 50)] + [arr[num][i] for i in range(50-amount)]

print("Part 1: ",end="")
retval = 0
for i in arr:
	for j in i:
		if j == "S": retval+=1
print(retval)
print("Part 2: \n")
for i in arr:
	for j in i:
		print((j if j == "S" else " "), end="")
	print()