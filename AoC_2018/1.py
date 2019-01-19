visited = [0]
curr = 0
revisit = 0
foundIt = False

def loopOverInput(curr, foundIt, revisit, visited):
    for line in open("1.txt", "r").readlines():
        curr += int(line)
        if curr in visited and foundIt == False:
            revisit = curr
            foundIt = True
        visited.append(curr)

loopOverInput(curr, foundIt, revisit, visited)
print("Part 1:", curr)

while foundIt == False:
    loopOverInput(curr, foundIt, revisit, visited)
    
print(visited)

print("Part 2:", revisit)