def smallestSubarraySum(s, array):
    windowStart, windowSum, minLength = 0, 0, float("inf")
    
    for windowEnd in range(len(array)): 
        windowSum += array[windowEnd]
        
        while windowSum >= s: 
            minLength = min(minLength, windowEnd - windowStart + 1)
            windowSum -= array[windowStart]
            windowStart += 1
            
    if minLength == float("inf"):
        return 0
    return minLength

def main(): 
    s = 7
    array = [2, 1, 5, 2, 3, 2]
    print(smallestSubarraySum(s, array))
    
main()