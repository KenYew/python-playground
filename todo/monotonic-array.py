# O(n) time | O(1) space
# where n is the length of the array
def isMonotonic(array): 
    isTrendingUpwards = isTrendingDownwards = True
    # Starting from the 2nd element because we need to make a comparison between the first two elements
    for i in range(1, len(array)):
        currentValue = array[i]
        previousValue = array[i - 1]
        if currentValue < previousValue: # if array is decreasing
            isTrendingUpwards = False
        if currentValue > previousValue: # if array is increasing
            isTrendingDownwards = False
    return isTrendingUpwards or isTrendingDownwards

array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
print(isMonotonic(array))