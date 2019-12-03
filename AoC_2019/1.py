
f = open("1.txt", "r")
from math import floor
total1 = 0
total2 = 0

def needs(mass):
    retval = 0
    num = mass
    while(1):
        num = floor(int(num)/3) - 2
        if(num>0):
            retval+=num
        else:
            return retval


for mass in f.readlines():
    total1 += floor(int(mass)/3) - 2
    total2 += needs(mass)

print("Part 1:", total1)
print("Part 2:", total2)