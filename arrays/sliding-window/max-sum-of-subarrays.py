def maxSumSubarraysOfSizeK(k, array):
    windowSum, windowStart, maxSum = 0, 0, float("-inf")
    for windowEnd in range(len(array)): 
        windowSum += array[windowEnd]
        
        if windowEnd >= k - 1:
            maxSum = max(maxSum, windowSum)
            windowSum -= array[windowStart]
            windowStart += 1
    return maxSum

def main(): 
    k = 3
    array = [2, 1, 5, 1, 3, 2]
    print(maxSumSubarraysOfSizeK(k, array))
    
main()