class Ingredient:
	def __init__(self, c, d, f, t, c2):
		self.capacity = c
		self.durability = d
		self.flavor = f
		self.texture = t
		self.calories = c2

Sprinkles = Ingredient(2, 0, -2, 0, 3)
Butterscotch = Ingredient(0, 5, -3, 0, 3)
Chocolate = Ingredient(0, 0, 5, -1, 8)
Candy = Ingredient(0, -1, 0, 5, 8)

items = [Sprinkles, Butterscotch, Chocolate, Candy]

part1 = 0
part2 = 0
for one in range(101):
	for two in range(101):
		for three in range(101):
			for four in range(101):
				if(one+two+three+four!=100): 
					continue
				teaspoons = [one, two, three, four]
				cap = 0
				dur = 0
				fla = 0
				tex = 0
				cal = 0

				for i in range(4):
					cap += (items[i].capacity * teaspoons[i])
					dur += (items[i].durability * teaspoons[i])
					fla += (items[i].flavor * teaspoons[i])
					tex += (items[i].texture * teaspoons[i])
					cal += (items[i].calories * teaspoons[i])
				if(cap<0 or dur<0 or fla<0 or tex<0): continue
				else: final = cap*dur*fla*tex
				if(cal==500): 
					if final>part2: part2 = final
				if final>part1: part1 = final
print("Part 1: "+str(part1))
print("Part 2: "+str(part2))