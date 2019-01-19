"""
simple text scan
letter?
    add 1 to total
parentheses?
    parse out length of string (L) and string (S)
    add L*S to total
    jump forward L (or L+1?) spaces after the closing paren
EOF?
    return total

"""

length = 0

with open("9.txt", "r") as f:
    text = f.read()
    i = 0
    while True:

        if i >= 10586:
            break
        
        if text[i].isalpha():
            length += 1
            i+=1

        elif text[i] == "(":
            instructions = text[i+1: text.find(")", i)]
            chars= int(instructions[0:instructions.find("x")])
            reps = int(instructions[instructions.find("x")+1:])
            
            toAdd = chars * reps

            length += toAdd
            
            sequenceEndIndex = text.find(")", i) + 1 + toAdd

            i = sequenceEndIndex

print(length)