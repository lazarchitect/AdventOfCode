class City:
	def __init__(self, n):
		self.visited = False
		self.name = n
		self.distances = []#filled with pairs of the form ("CityName", distanceToThere)


class Graph:
	def __init__(self):
		self.cities = []
		for each in open("9.txt").readlines():
			words = each.split(" ")
			place1 = words[0]
			place2 = words[2]
			distance = int(words[4][:-1])
	
			if place1 not in self.getCityNames():
				self.cities.append(City(place1))
	
			if place2 not in self.getCityNames():
				self.cities.append(City(place2))
		
			self.getCityByName(place1).distances.append((place2, distance))
			self.getCityByName(place2).distances.append((place1, distance))
		
	def getCityNames(self):
		retval = []
		for i in self.cities:
			retval.append(i.name)
		return retval	
	
	def getCityByName(self, n):
		for i in self.cities:
			if(i.name == n): return i
		# return None #should never happen ideally
	
	def getDistance(self, n1, n2):
		city1 = self.getCityByName(n1)
		for i in city1.distances:
			if i[0] == n2:
				return i[1]
		return -1 #again, should never happen			
	
	def toString(self):
		for i in self.cities:
			print(i.name+": ", end="")
			for j in i.distances:
				print(j, end = "")
				print(", ",end="")
			print()	
				
g = Graph()
longest = 0

def startAt(i):
	print(i)
	for j in g.getCityNames():
			travel(i, j, [i], 0)

def travel(lastCity, currentCity, v, total):
	global longest
	total+=g.getDistance(lastCity, currentCity)
	v.append(currentCity)
	# v.append(lastCity)
	if len(v)==8:
		print(v)		
		if total>longest: longest = total
		return
	for i in g.getCityNames():
		if i not in v:
			travel(currentCity, i, v, total)
			
for i in g.getCityNames():
	startAt(i)



print(longest)















