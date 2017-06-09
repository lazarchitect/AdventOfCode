def a():
	pass


def b():
	pass


main_list = []
matches = 0

# for E in open("17.txt").readlines():
# 	main_list.append(int(E))

main_list = [100, 90, 60, 50, 30, 30, 30]
overall_list = main_list

for i in overall_list:
	matches += a()

print("Part 1 (should be 6): ", matches)