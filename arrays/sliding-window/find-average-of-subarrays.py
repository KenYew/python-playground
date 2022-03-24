# Brute Force
# Time O(n * k) | Space O(n) where n is the number of elements in the array
def findAverageOfSubarrays(k, array): 
    result = []
    # 1: Loop through each element of the array but keep track of completed elements with - k + 1
    for idx in range(len(array) - k + 1):
        # 2: Initialise _sum variable of float type
        _sum = 0.0
        # 3: Loop through each element of the array again from idx to idx + k
        for jdx in range(idx, idx + k):
            # 4: Sum all traversed elements of the array
            _sum += array[jdx]
        # 5: Append the mean of total sum as the answer 
        result.append(_sum/k)
    return result

# Sliding Window
# Time O(n) | Space O(n) where n is the number of elements in the array
def findAverageOfSubarrays(k, array): 
    result = []
    # 1: Initialise windowSum for the sum of k elements of subarray and windowStart pointer for the beginning of the sliding window
    windowSum, windowStart = 0.0, 0
    # 2: Increment the windowEnd pointer in a for loop
    for windowEnd in range(len(array)): 
        # 3: Sliding the window, we add the next element going in
        windowSum += array[windowEnd]
        # 4: Don't start the sliding window until we have incremented windowEnd to the required window size of k
        if windowEnd >= k - 1:
            # 5: Calculate the average of current windowSum and append the result
            result.append(windowSum / k) 
            # 6: Sliding the window, we subtract the element going out
            windowSum -= array[windowStart]
            # 7: Move the sliding window one element at a time
            windowStart += 1
    return result


def main(): 
    k = 5
    array = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    print(findAverageOfSubarrays(k, array))
    
main()