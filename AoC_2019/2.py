

def attempt(arr, noun, verb):
    index = 0
    arr[1] = noun
    arr[2] = verb

    while(1):        
        operand = arr[index]    

        if(operand == 99):
            break

        elif(operand == 1):
            arr[arr[index+3]] = arr[arr[index+1]] + arr[arr[index+2]]
        
        elif(operand == 2):
            arr[arr[index+3]] = arr[arr[index+1]] * arr[arr[index+2]]

        index += 4
    return arr[0]


f = open("2.txt", "r")

arr = f.read().split(",")

arr = [int(i) for i in arr]

print("Part 1:", attempt(arr, 12, 2))

goal = 19690720
part2 = 0

for noun in range(0,100):
    for verb in range(0, 100):
        try:
            x = attempt(arr, noun, verb)
            print("hi")
            if(x == goal):
                part2 = 100*noun+verb
                break;
        except IndexError:
            pass

print("Part 2:", part2)