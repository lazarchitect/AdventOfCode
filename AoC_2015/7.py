	
"""
command list:
	AND
	OR
	NOT
	RSHIFT
	LSHIFT
	...nothing?
"""

wires = {}
instructions = []

for each in open("7.txt").readlines():
	instructions.append(each)
		
for line in instructions:	
	try:
		words = line.split(" ")
		# print(words)
		output = words[len(words)-1][0:len(words[len(words)-1])-1]
		# print(output)
		
		if(words[1] == "->"):#basic assignment
			wires[output] = int(words[0])
		
		if(words[0] == "NOT"):
			input0 = words[1]
			wires[output] = ~ wires[input0]
		
		else:
			input1 = words[0]
			input2 = words[2]
			
			if(words[1] == "AND"):				
				wires[output] = wires[input1] &  wires[input2]
			
			elif(words[1] == "OR"):
				wires[output] = wires[input1] |  wires[input2]
			
			elif(words[1] == "LSHIFT"):
				wires[output] = wires[input1] << wires[input2]
		
			elif(words[1] == "RSHIFT"):
				wires[output] = wires[input1] >> wires[input2]
	except KeyError:
		passw