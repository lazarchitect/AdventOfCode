instructions = []

for x in open("23.txt").readlines():
	instructions.append(x.rstrip('\n'))

def d(num):
	registers = {"a": num, "b": 0}

	i = 0

	def parse(s, i):
		#theres a 3-letter instruction code
		#3 are just math ops with one parameter, the register
		x = s.split(" ")
		
		code = x[0]
		
		if code == "jmp": 
			return i + int(x[1].lstrip("+"))
		
		if code == "jie" and registers[x[1].rstrip(",")]%2==0: 
			return i + int(x[2].lstrip("+")) 
		
		if code == "jio" and registers[x[1].rstrip(",")] == 1: 
			return i + int(x[2].lstrip("+")) 
		
		if code == "inc": 
			registers[x[1]]+=1
		
		elif code == "hlf": 
			registers[x[1]]/=2
		
		elif code == "tpl": 
			registers[x[1]]*=3
		
		return i + 1

	while True:
		if i > 46: break
		i = parse(instructions[i], i)

	return registers["b"]



print("Part 1:", d(0))
print("Part 2:", d(1))