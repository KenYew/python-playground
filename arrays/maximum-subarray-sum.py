# Solution using Kadane's Algorithm
# O(n) Time | O(1) Space - where n is the length of the input array
def maxSubArray(nums):
    # 1: Initialise maxSumEndingHere pointer at the beginning of array and maxSoFar to keep track of max sum so far
    maxSumEndingHere, maxSoFar = 0, float("-inf")
    # 2: Traverse the array and compute for each element
    for currentNum in nums:
        # 3: Using Kadane's algorithm, calculate maxSumEndingHere and maxSoFar with max functions for each element traversed so far
        maxSumEndingHere = max(currentNum, maxSumEndingHere + currentNum)
        maxSoFar = max(maxSoFar, maxSumEndingHere)
    return maxSoFar
    
# Kadane's Algorithm Concept
# O(n) Time | O(1) Space - where n is the length of the input array
def kadane(array): 
    # 1: Initialise maxSumEndingHere pointer at the beginning of array and maxSoFar to keep track of max sum so far
    maxSumEndingHere = array[0] # Summation of all adjacent elements up to this point
    maxSoFar = array[0] # Maximum value of summations calculated so far 
    # 2: Traverse the array and compute for each element
    for idx in range(1, len(array)): 
        currentNum = array[idx]
        # 3: Using Kadane's algorithm, calculate maxSumEndingHere and maxSoFar with max functions for each element traversed so far
        maxSumEndingHere = max(currentNum, maxSumEndingHere + currentNum)
        maxSoFar = max(maxSoFar, maxSumEndingHere)
    return maxSoFar

# Alternative Solution
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