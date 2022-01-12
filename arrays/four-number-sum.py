def fourNumberSum(array, targetSum):
    allPairSums = {}
    quadruplets = []
    for i in range(1, len(array) - 1):
        for j in range(i + 1, len(array)):
            currentSum = array[i] + array[j]
            difference = targetSum - currentSum
            if difference in allPairSums:
                for pair in allPairSums[difference]:
                    quadruplets.append(pair + [array[i], array[j]])
        
        for k in range(0, i):
            currentSum = array[i] + array[k]
            if currentSum not in allPairSums:
                allPairSums[currentSum] = [[array[k], array[i]]]
            else:
                allPairSums[currentSum].append([array[k], array[i]])
                
    return quadruplets

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
    
def fourNumberSum(array, targetSum):
    ans = []
    array.sort()
    for idx in range(len(array) - 3): 
        if idx == 0 or array[idx] != array[idx - 1]:
            threeNumberSums = threeNumberSum(array[idx + 1:], targetSum - array[idx])
            for sum in threeNumberSums: 
                ans.append([array[idx]] + sum)
    return ans

array = [2,2,2,2,2]
targetSum = 8
print(fourNumberSum(array, targetSum))