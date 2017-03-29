import turtle
import random

bob = turtle.Turtle()
jeff = turtle.Turtle()
for each in open("1.txt").read().split(", "):
	if(each[0] == "L"): bob.left(90)	
	else: bob.right(90)
	jeff.forward(12)
	bob.forward(2*int(each[1:]))

turtle.getscreen()._root.mainloop()