a = 0
b = 0
c = 1
d = 0

i = 0

def execute(instruction):
    global a, b, c, d, i
    
    tokens = instruction.split(" ")

    if instruction[0] == "j": #jnz
        if eval(tokens[1]) != 0:
            i += int(tokens[2])
        else:
            i+=1
        return
    
    if instruction[0] == "c": #cpy
        if tokens[2] == "a":
            a = eval(tokens[1])
        elif tokens[2] == "b":
            b = eval(tokens[1])
        elif tokens[2] == "c":
            c = eval(tokens[1])            
        elif tokens[2] == "d":
            d = eval(tokens[1])
        i+=1
        return            
    
    elif instruction[0] == "i": #inc
        if tokens[1] == "a":
            a+=1
        elif tokens[1] == "b":
            b+=1
        elif tokens[1] == "c":
            c+=1
        elif tokens[1] == "d":
            d+=1
        i+=1
        return    

    elif instruction[0] == "d": #dec
        if tokens[1] == "a":
            a-=1
        elif tokens[1] == "b":
            b-=1
        elif tokens[1] == "c":
            c-=1
        elif tokens[1] == "d":
            d-=1
        i+=1
        return
               
instructions = []

for line in open("12.txt", "r").readlines():
    instructions.append(line[:-1])

while i < len(instructions):
    execute(instructions[i])
    
print(a,b,c,d)