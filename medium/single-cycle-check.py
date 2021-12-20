# O(n) Time | O(1) Space
def hasSingleCycle(array):
    numElementsVisited = 0
    currentIdx = 0 # initialise the current index to be zero-th element of the array
    while numElementsVisited < len(array): 
        # CHECK #1: If we're passed the first element and yet we find out index back at 0, then we have multiple cycles!
        if numElementsVisited > 0 and currentIdx == 0:
            return False
        # otherwise, we will keep traversing
        numElementsVisited += 1
        currentIdx = getNextIdx(currentIdx, array)
    # CHECK #2: Once we have visited all elements, check if the currentIdx has looped back to the beginning index and return its Boolean
    return currentIdx == 0 

def getNextIdx(currentIdx, array):
    # calculate the value of the next index to jump (nextIdx) to based on the value of the currentIdx (jump)
    jump = array[currentIdx]
    # EDGE CASE #1: use mod(len(array)) to wrap back to the array when the jump goes out of bounds of array 
    nextIdx = (currentIdx + jump) % len(array)
    # EDGE CASE #2: else nextIdx + len(array) accounts for wrapping around arrays when your jump is a large negative value. + len(array) ensures that your nextIdx will be the equivalent positive index value of the negative index value since -ve indices are problematic.
    return nextIdx if nextIdx >= 0 else nextIdx + len(array)
    
# PATTERN RECOGNITION: Anything that requires wrapping around data, use MODULO!

array = [2, 3, 1, -4, -4, 2] # Sample Output: True
print(hasSingleCycle(array))