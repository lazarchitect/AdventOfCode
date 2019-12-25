
def geth(direction):
    return {"U":90, "L": 180, "R":0, "D":270}[direction]

f = open("3.txt", "r")
x = f.readlines()

PathA = x[0].split(",")
PathB = x[1].split(",")

import turtle, time

divisor = 40

locA = (0,0)
locB = (0,0)

for move in range(301):

    turtle.color("blue")

    turtle.seth(geth(move[0]))
    turtle.forward(int(move[1:])/divisor)

    turtle.penup()

    turtle.color("red")
    turtle.goto(0,0)

    turtle.pendown()

    turtle.seth(geth(move[0]))
    turtle.forward(int(move[1:])/divisor)


time.sleep(1000000)

