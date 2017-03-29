class Sue:
	children    = -1
	cats        = -1
	samoyeds    = -1
	pomeranians = -1
	akitas      = -1
	vizslas     = -1
	goldfish    = -1
	trees       = -1
	cars        = -1
	perfumes    = -1

goldenSue = Sue()
goldenSue.children = 3
goldenSue.cats = 7
goldenSue.samoyeds = 2
goldenSue.pomeranians = 3
goldenSue.akitas = 0
goldenSue.vizslas = 0
goldenSue.goldfish = 5
goldenSue.trees = 3
goldenSue.cars = 2
goldenSue.perfumes = 1

def ehh():
	for each in open("16.txt").readlines():
	
		x = Sue()
		words = each.split(" ")
		# print(words)
		x.index = words[1][:-1]
		
		var1 = words[2][:-1]
		val1 = words[3][:-1]
		var2 = words[4][:-1]
		val2 = words[5][:-1]
		var3 = words[6][:-1]
		val3 = words[7][:-1]
		
		exec("x." + var1 + " = " + val1)
		
		exec("x." + var2 + " = " + val2)
		
		exec("x." + var3 + " = " + val3)
		
		if eval("x."+var1+" == goldenSue."+var1):
			if eval("x."+var2+" == goldenSue."+var2):
				if eval("x."+var3+" == goldenSue."+var3):
					print("Part 1: " + x.index)
		points = 0
		
		if(var1 == "cats" or var1 == "trees"): #check for greater than
			if eval("x."+var1+" > goldenSue."+var1):
				points+=1
			
		elif(var1 == "pomeranians" or var1 == "goldfish"): #check for less than
			if eval("x."+var1+" < goldenSue."+var1):
				points+=1
			
		else:#just check for equals
			if eval("x."+var1+" == goldenSue."+var1):
				points+=1
			
		""""""""""""""""""""""""""""""""""""""""""""""""	
		if(var2 == "cats" or var2 == "trees"): #check for greater than
			if eval("x."+var2+" > goldenSue."+var2):
				points+=1
			
		elif(var2 == "pomeranians" or var2 == "goldfish"): #check for less than
			if eval("x."+var2+" < goldenSue."+var2):
				points+=1
				
			
		else:#just check for equals
			if eval("x."+var2+" == goldenSue."+var2):
				points+=1
				
		""""""""""""""""""""""""""""""""""""""""""""""""		
		if(var3 == "cats" or var3 == "trees"): #check for greater than
			if eval("x."+var3+" > goldenSue."+var3):
				points+=1
			
		elif(var3 == "pomeranians" or var3 == "goldfish"): #check for less than
			if eval("x."+var3+" < goldenSue."+var3):
				points+=1
			
		else:#just check for equals
			if eval("x."+var3+" == goldenSue."+var3):
				points+=1				
			
			
			
		if(points==3):
			print("Part 2: "+str(x.index))
			return
											
														

ehh()






