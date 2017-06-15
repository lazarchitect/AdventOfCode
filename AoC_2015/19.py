
def removeDuplicates(dupe_list):
	retval = []
	for i in dupe_list:
		if i not in retval:
			retval.append(i)
	return retval		

arr = []

for line in open("19.txt").readlines():
	arr.append(line[:-1])

molecule = arr[-1] + "l"
arr = arr[:-2]

can_replace = []
mod_list = []
for i in arr:
	can_replace.append(i[0:i.index(" ")])
	mod_list.append(i[i.index("> ")+2:])

semifinal = []

for i in range(len(molecule)):

	if molecule[i] in can_replace:
		for j in range(len(can_replace)):
			if molecule[i] == can_replace[j]:
				replacement = mod_list[j]
				semifinal.append(molecule[0:i]+replacement+molecule[i+1:]) #could cause an out of bounds error...?

	elif (i!=len(molecule)-1 and molecule[i]+molecule[i+1] in can_replace):
		for j in range(len(can_replace)):
			if molecule[i]+molecule[i+1] == can_replace[j]:
				replacement = mod_list[j]
				semifinal.append(molecule[0:i]+replacement+molecule[i+2:]) #note the 2. could cause an out of bounds error...?


final = removeDuplicates(semifinal)

print("Part 1:", len(final))
#####################################################################
def getAllMods(molecule):
	semifinal = []
	for i in range(len(molecule)):

		if molecule[i] in can_replace:
			for j in range(len(can_replace)):
				if molecule[i] == can_replace[j]:
					replacement = mod_list[j]
					semifinal.append(molecule[0:i]+replacement+molecule[i+1:]) #could cause an out of bounds error...?

		elif (i!=len(molecule)-1 and molecule[i]+molecule[i+1] in can_replace):
			for j in range(len(can_replace)):
				if molecule[i]+molecule[i+1] == can_replace[j]:
					replacement = mod_list[j]
					semifinal.append(molecule[0:i]+replacement+molecule[i+2:]) #note the 2. could cause an out of bounds error...?
	return semifinal

stepCount = 0
possibilities = ["e"]

print(len(molecule))
import time
time.sleep(1)
while True:

	if molecule in possibilities:
		break

	step_add = []

	for i in possibilities:
		step_add += getAllMods(i)
		# print(len(i))
	
	# time.sleep(.4)
	# print(possibilities)

	possibilities = step_add
	print(len(possibilities[0]))

	stepCount+=1


print("Part 2:", stepCount)
