from time import sleep

with open("1.txt", "r") as f:
    arr = f.read().split("\n")
    
    increases = 0
    prev = arr[0]

    for i in arr:
        if int(i) > int(prev):
            increases+=1
        # print(prev, i, i>prev, increases)    
        prev = i

    print("part 1:", increases)


    sum_increases = 0
    first_sum = int(arr[0]) + int(arr[1]) + int(arr[2])
    prev_sum = first_sum

    for i in range(2, len(arr)):
        window_sum = int(arr[i]) + int(arr[i-1]) + int(arr[i-2])
        if window_sum > prev_sum:
            sum_increases += 1

        # print(prev_sum, window_sum, window_sum>prev_sum, sum_increases)
        
        prev_sum = window_sum

    print("part 2: ", sum_increases)