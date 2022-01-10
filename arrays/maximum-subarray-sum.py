# O(n) Time | O(1) Space 
def maximumSubarraySum(array):
    maxSum = float("-inf")
    currentSum = 0

    for val in array:
        currentSum = currentSum + val
        if currentSum > maxSum:
            maxSum = currentSum
        if currentSum < 0:
            currentSum = 0
    return maxSum