# BRUTE FORCE: O(n^2) time | O(n) space
def findAveragesOfSubarrays(k, arr):
    ans = []
    for i in range(len(arr) - k + 1):
        sum = 0
        for j in range(i, i + k):
            sum += arr[j]
        ans.append(sum/k)
    return ans

# Sliding Window Approach: O(n) time | O(n) space
def findAveragesOfSubarrays(k, arr):
    ans = []
    windowSum = 0.0
    windowStart = 0
    
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        
        if windowEnd >= k - 1:
            ans.append(windowSum / k)
            windowSum -= arr[windowStart]
            windowStart += 1

    return ans

arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5
print(findAveragesOfSubarrays(k, arr))
# Output: [2.2, 2.8, 2.4, 3.6, 2.8]