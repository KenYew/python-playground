# O(n^2) time | O(n) space
def threeNumberSum(array, targetSum):
    array.sort()
    ans = []
    for idx in range(len(array) - 2): # since we're looking for a triplet, in the n-th iteration of the for loop, the idxPointer will always be 3rd from last of the array to allow for leftPointer and rightPointer to fit in the triplet
        left = idx + 1
        right = len(array) - 1 # since we're dealing with pointers, we must account for Python's zero indexing
        while left < right:
            currentSum = array[idx] + array[left] + array[right] 
            if currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
            elif currentSum == targetSum:
                ans.append([array[idx], array[left], array[right]])
                left += 1
                right -= 1
    return ans
    
array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0
print(threeNumberSum(array, targetSum))