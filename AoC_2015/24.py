packages = [1,2,3,7,11,13,17,19,23,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113]

def weight(group):
    return sum(group)

def findThreeGroups():

    smallGroup = [] #doesnt matter at first, all are zero
    middleGroup = []
    largestGroup = []

    """   logic
    iterate thru packages, put each package in smallest (by sum) list
    at the end the packages will be similar weights but not exact
    then you have to move packages from the largest group to the smallest repeatedly until it balances

    actually super simple code
    """
    def printout():
        print("Small:", weight(smallGroup), "\nMiddle:", weight(middleGroup), "\nLarge:", weight(largestGroup))
        print()

    
    def evenlyBalanced():
        return weight(smallGroup) == weight(largestGroup) and weight(smallGroup) == weight(middleGroup)

    def relabel(smallGroup, middleGroup, largestGroup):
        if weight(largestGroup) < weight(smallGroup): #did adding to smallGroup make it the new largest?
            smallGroup, middleGroup, largestGroup = middleGroup, largestGroup, smallGroup  #swap em

        elif weight(middleGroup) < weight(smallGroup): #did adding to smallGroup make it the real median?
            middleGroup, smallGroup = smallGroup, middleGroup #swap em

        return (smallGroup, middleGroup, largestGroup)    

    for i in packages:
        
        smallGroup.append(i)
        smallGroup, middleGroup, largestGroup = relabel(smallGroup, middleGroup, largestGroup) #verify that labels are still correct given new i in smallGroup
        
        printout()

    #at this point all groups should be semi balanced

    while not evenlyBalanced():
        temp = max(largestGroup)
        smallGroup.append(temp)
        largestGroup.remove(temp)

        smallGroup, middleGroup, largestGroup = relabel(smallGroup, middleGroup, largestGroup)
        printout()



findThreeGroups()