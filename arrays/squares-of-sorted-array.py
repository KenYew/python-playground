# O(nlogn) time | O(1) space
def sortedSquaresNaive(nums): 
    n = len(nums)
    ans = []
    for num in nums: 
        ans.append(num**2)
    ans.sort()
    return ans

def sortedSquares(A: 'List[int]') -> 'List[int]':
    answer = [] # list
    l, r = 0, len(A) - 1
    while l <= r:
        left, right = abs(A[l]), abs(A[r])
        if left > right:
            answer.append(left * left)
            l += 1
        else:
            answer.append(right * right)
            r -= 1
    return (answer[::-1]) # reverse list using step of -1 [::-1]

nums = [-4, -1, 0, 3, 10]
print(sortedSquares(nums))