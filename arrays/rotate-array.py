""" 
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Classical 3-step array rotation:
1. reverse the first n - k elements
2. reverse the rest of them
3. reverse the entire array
"""
def rotate(nums, k):
    if k is None or k <= 0:
        return
    
    k %= len(nums)
    print(k)
    end = len(nums) - 1
    
    reverse(nums, 0, end - k)
    reverse(nums, end - k + 1, end)
    reverse(nums, 0, end)
    return nums
        
def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

nums = [1, 2, 3, 4, 5, 6, 7] # len(nums) = 7
k = 3
print(rotate(nums, k))
print(k % len(nums))