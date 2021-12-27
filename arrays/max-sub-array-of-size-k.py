# Input: [2, 1, 5, 1, 3, 2], k=3 
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3]

def maxSubArrayOfSizeK(k, arr):
    ans = []
    for i in range(len(arr) - k - 1):
        sum = 0
        for j in range(i, k - 1):
            sum += arr[j]
        ans.append(sum/k)
    return ans

arr = [2, 1, 5, 1, 3, 2]
k = 3
print(maxSubArrayOfSizeK(k, arr))

