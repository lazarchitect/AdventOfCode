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

with open("9.txt", "r") as f:
    text = f.read()
    for i in text:
        
        if i.isalpha():
            total += 1

        elif i == "(":
            instructions = 