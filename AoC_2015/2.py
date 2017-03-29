def part1(s):
	return (2*l*w)+(2*l*h)+(2*w*h)+min(l*w, w*h, h*l)

def part2(s):
	x = max(l, h, w)
	if(x==l): return 2*h+2*w + l*h*w
	if(x==w): return 2*h+2*l + l*h*w	
	return 2*l+2*w + l*h*w
	
paper  = 0
ribbon = 0

for each in open("2.txt").readlines():
	d = each[0:len(each)-1].split('x')
	l = int(d[0])
	w = int(d[1])
	h = int(d[2])
	paper +=part1(each)
	ribbon+=part2(each)
		
print("Part 1: "+str(paper))
print("Part 2: "+str(ribbon))