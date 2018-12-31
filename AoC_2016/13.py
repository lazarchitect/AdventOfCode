puzzleInput = 1362

def isOpen(x, y):
    A = x*x + 3*x + 2*x*y + y + y*y
    B = puzzleInput
    C = A + B
    binary = bin(C)
    string = str(binary)
    toEval = string[2:]
    OneCount = sum(int(i) for i in toEval)
    evenCount = (OneCount % 2 == 0)
    return evenCount

def generateGrid():
    grid = ""

    for y in range(401):
        for x in range(401):
            if x == 31 and y == 39:
                grid += "G"
            if(isOpen(x, y)):
                grid += "_"
            else:
                grid += "0"
        grid += "\n"

    return grid        


##### START MAIN

grid = generateGrid()

with open("13.txt", "w") as fileDescriptor:
    fileDescriptor.write(grid)

with open("13.txt", "r") as f:
    print(f.read())