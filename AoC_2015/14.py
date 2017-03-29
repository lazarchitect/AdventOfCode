class Reindeer:
	def __init__(self, s, t, r):
		self.speed = s
		self.runTime = t
		self.restTime = r
		self.distance = 0
		
slut = {Reindeer(22, 8, 165):0,
		Reindeer(8, 17, 114):0,
		Reindeer(18, 6, 103):0,
		Reindeer(25, 6, 145):0,
		Reindeer(11, 12, 125):0,
		Reindeer(21, 6, 121):0,
		Reindeer(18, 3, 50):0,
		Reindeer(20, 4, 75):0,
		Reindeer(7, 20, 119):0}

for x in range(2503):
	for i in slut: 
		if ((x%(i.runTime+i.restTime))/i.runTime) < 1: i.distance+=i.speed
	x = max([j.distance for j in slut])
	for i in slut:
		if i.distance == x: slut[i]+=1
	
print("Part 1: "+str(max([i.distance for i in slut])))
print("Part 2: "+str(max([slut[i] for i in slut])))