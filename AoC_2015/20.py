goal = 36000000 #36 million

# House x receives y*10 presents from each elf #y where y is a factor of X.

#ex. factors of 24: 1, 2, 3, 4, 6, 8, 12, 24

#so house 24 receives 10 + 20 + 30 + 40 + 60 + 80 + 120 + 240 = 600 presents
#algorithm to get n's factors:
#divide number by p in [1 through int(n/2)]
#if it divides cleanly, add p and n/p to list_of_factors

from math import sqrt


def part_1():

	def factor_list(x):

		retval = []
		
		for p in range(1, int(sqrt(x))+1): #because its inclusive-exclusive
			if x/p == int(x/p):
				retval.append(p)
				if p!=x/p:
					retval.append(x/p)

		return retval		

	print("\n\n\n   running...\n\n\n")

	for houseNum in range(1, 1440000):

		# print(houseNum)

		if 10 * sum(factor_list(houseNum)) >= goal:
			print("Part 1:", houseNum)
			break


def part_2():

	def factor_list(x):

		retval = []
		
		for p in range(1, int(sqrt(x))+1): #because its inclusive-exclusive
			if x/p == int(x/p): #if it divides evenly...
				if x <= p*50:
					retval.append(p)
				if x <= x/p*50 and p!=x/p:
					retval.append(x/p)

		return retval		

	print("\n\n\n   running...\n\n\n")

	for houseNum in range(1, goal):

		# print(houseNum)

		if 11 * sum(factor_list(houseNum)) >= goal:
			print("Part 2:", houseNum)
			break




part_2()










