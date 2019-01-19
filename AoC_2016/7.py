def containsABBA(string):
    for i in range(len(string)-3):
        if string[i] == string[i+3]:
            if string[i+1] == string[i+2]:
                if string[i] != string[i+1]:
                    return True
    return False                

def hasTLS(line):
    outsideText = ""
    insideText = ""
    insideBrackets = False
    for i in line:
        if insideBrackets == True and i != "]":
            insideText += i
        if i == "[":
            insideBrackets = True
            outsideText += "_"
            continue
        if insideBrackets == False:
            outsideText += i
        if i == "]":
            insideBrackets = False


    if containsABBA(outsideText):
        if containsABBA(insideText):
            return False
        else:
            return True
    
    return False

hasSSL(line):


######################
    ### MAIN ###
######################

part1 = 0

for ip in open("7.txt", "r").readlines():
    part1 += 1 if hasTLS(ip) else 0

print("Part 1:", part1)