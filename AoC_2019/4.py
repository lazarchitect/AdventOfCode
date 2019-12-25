#4.py

###############
### METHODS ###
###############

def containsRepeat(s):
    for i in range(len(s)):
        if(i!=0) and (s[i] == s[i-1]):
            if(i!=len(s)-1) and (s[i] == s[i+1]):
                continue
            else:
                return True    
    return False

def neverDecrease(s):
    for i in range(len(s)):
        if(i!=0 and int(s[i]) < int(s[i-1])):
            return False
    return True

############################

low = 136760
high = 595730

counter = 0

for i in range(low, high):
    s = str(i)
    if(containsRepeat(s) and neverDecrease(s)):
        counter+=1

print("part 1:",counter)