import hashlib

i = 0
part1 = ""
print("This one takes a while...")
for q in range(8):
	while(True):
		x = hashlib.md5(("ffykfhsq"+str(i)).encode('utf-8')).hexdigest()
		i+=1
		
		if x[0:5] == "00000":
			part1+=x[5]
			break

i = 0
sol = []

def occupied(L, position):
	for i in L: 
		if i[0] == position: return True
	return False		

while(True):
		x = hashlib.md5(("ffykfhsq"+str(i)).encode('utf-8')).hexdigest()
		i+=1
		
		if x[0:5] == "00000":
			position = x[5]
			value = x[6]
			if occupied(sol, position): 
				continue
			if position.isdigit() == True and int(position) < 8 and int(position)>=0:
				sol.append([position, value])
				# print(sol)
			if len(sol)==8:
				break
part2 = ""
for i in range(8):
	for j in sol:
		if int(j[0]) == i:
			part2 += j[1]
					
print("Part 1: "+part1)
print("Part 2: "+part2)