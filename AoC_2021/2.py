

with open("2.txt", "r") as f:
    arr = f.read().split("\n")

    x = 0
    y = 0

    for instruction in arr:
        cmds = instruction.split(" ")
        direction = cmds[0]
        amount = cmds[1]

        if direction == "forward":
            x += int(amount)
        elif direction == "down":
            y += int(amount)
        elif direction == "up":
            y -= int(amount)

    print("part 1:", x, y, x*y)

    x = 0
    aim = 0
    depth = 0

    for instruction in arr:
        cmds = instruction.split(" ")
        direction = cmds[0]
        amount = cmds[1]

        if direction == "forward":
            x += int(amount)
            depth += int(amount)*aim

        elif direction == "down":
            aim += int(amount)

        elif direction == "up":
            aim -= int(amount)

    print("part 2:", x, depth, x*depth)