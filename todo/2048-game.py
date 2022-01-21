"""
https://flothesof.github.io/2048-game.html
Input: [2, 2, 8, 8]
Output: [4, 16, 0, 0]
"""
# O(n) Time | O(n) Space
def swipeLeft(array):
    # 1: Create an auxiliary output array of zeros with equal length of input array
    outputArray = [0 for _ in range(len(array))]
    previousValue, newIdx = None, 0
    
    # 2: Traversing through each element of the input array, 
    for idx in range(len(array)):
        # 3: If the current element is non-zero,
        if array[idx] != 0: 
            # 4: If this is the first iteration at the first element, previousValue is None initally.
            if previousValue == None: 
                # 5: Set the previousValue to be the first element of the input array
                previousValue = array[idx]
            # 5: Else, we are traversing from the 2nd element onwards,
            else:
                # 6: If array[idx - 1] == array[idx] (e.g.: [2, 2, 0, 0] -> [4, 0, 0, 0])
                if previousValue == array[idx]:
                    # 7: Same the two adjacent elements of the same value and store it in another auxiliary output array at newIdx
                    outputArray[newIdx] = 2 * array[idx]
                    # 8: Move the newIdx pointer to the next element to fill in the output array
                    newIdx += 1
                    # 9: Reset the previousValue to None again
                    previousValue = None
                # 7: If array[idx - 1] != array[idx] (e.g.: [2, 0, 0, 0])
                else: 
                    # 8: Store the previousValue into the auxiliary output array at newIdx
                    outputArray[newIdx] = previousValue
                    # 9: Move the newIdx pointer to the next element to fill in the output array
                    newIdx += 1
                    # 10: Update the previousValue with the current element value
                    previousValue = array[idx]

    # 11: If the previousValue is an integer (not a None),
    if previousValue != None: 
        # 12: Store the previousValue into the auxiliary output array at newIdx
        outputArray[newIdx] = previousValue
    # 13: Return the completed auxiliary matrix
    return outputArray

def swipeLeft(array):
    output = [0 for _ in range(len(array))]
    previous, jdx = None, 0
    for idx in range(len(array)): 
        if array[idx] != 0: 
            if previous == None: 
                previous = array[idx]
            else: 
                if previous == array[idx]:
                    output[jdx] = 2 * array[idx]
                    jdx += 1
                    previous = None
                else: 
                    output[jdx] = previous
                    jdx += 1
                    previous = array[idx]
    if previous != None: 
        output[jdx] = previous
    return output

array = [2, 2, 8, 8]
print(swipeLeft(array))