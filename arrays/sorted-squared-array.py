# O(n) Time | O(n) Space - where n is the length of the input array
def sortedSquaredArray(array):
    # 1: Initialise output array of size input array with dummy values
    ans = [0 for _ in array]
    # 2: Initialise two pointers on each end of the array
    left, right = 0, len(array) - 1
    # 3: Traversing idx pointer from end to beginning of the array because we want to write the largest to the smallest values
    for idx in reversed(range(len(array))): 
        # 4: If abs(left-most value) is > abs(right-most value) e.g.: [-4, 1, 2]
        if abs(array[left]) > abs(array[right]):
            # 5: Insert the square of the largest value at the current iteration idx (from n-th to 0)
            ans[idx] = array[left] * array[left]
            # 6: Then, increment the left pointer
            left += 1
        # 7: Else if abs(right-most value) is >= abs(left-most value) e.g.: [1, 2, 3]
        else: 
            # 8: Insert the square of the largest value at the current iteration idx (from n-th to 0)
            ans[idx] = array[right] * array[right]
            # 9: Then, decrement the right pointer
            right -= 1
    # 10: Finally, return the sorted squared array
    return ans

# O(n) Time | O(n) Space - where n is the length of the input array
def sortedSquaredArray(array):
    squares = [0 for _ in array]
    highestSquareIdx = len(array) - 1
    left, right = 0, len(array) - 1
    
    while left <= right: 
        leftSquare = array[left] * array[left]
        rightSquare = array[right] * array[right]
        if leftSquare > rightSquare: 
            squares[highestSquareIdx] = leftSquare
            left += 1
        else:
            squares[highestSquareIdx] = rightSquare
            right -= 1
        highestSquareIdx -= 1
    return squares

array = [1, 2, 3, 5, 6, 8, 9]
print(sortedSquaredArray(array))