# O(n) time | O)(1) space
def findThreeLargestNumbers(array):
    threeLargest = [None for i in range(3)]
    for num in array:
        updateLargest(threeLargest, num)
    return threeLargest

def updateLargest(threeLargest, num):
    if threeLargest[2] is None or num > threeLargest[2]:
        shiftAndUpdate(threeLargest, num, 2) 
    elif threeLargest[1] is None or num > threeLargest[1]:
        shiftAndUpdate(threeLargest, num, 1) 
    elif threeLargest[0] is None or num > threeLargest[0]:
        shiftAndUpdate(threeLargest, num, 0) 
        
def shiftAndUpdate(threeLargest, num, indexToUpdate):
    for i in range(indexToUpdate + 1):
        # if we've iterated to the final position,
        # we update i-th value to the new largest number
        if i == indexToUpdate: 
            threeLargest[i] = num
        # else, shift the value from i + 1 into i
        else:
            threeLargest[i] = threeLargest[i + 1]
            
array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
print(findThreeLargestNumbers(array))