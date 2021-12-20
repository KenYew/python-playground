arr = [1, 5, 4, 3, 2]
#1-maxIdxSwap: [5, 1, 4, 3, 2]
#1-pancakFlip: [2, 3, 4, 1, 5]

#2-maxIdxSwap: [4, 3, 2, 1, 5]
#2-pancakFlip: [1, 2, 3, 4, 5]

#3-maxIdxSwap: [3, 2, 1, 4, 5]
#3-pancakFlip: [1, 2, 3, 4, 5]

#4-maxIdxSwap: [2, 1, 3, 4, 5]
#4-pancakFlip: [1, 2, 3, 4, 5]

# O(n^2) Time | O(1) Space
def pancakeSort(arr):
    n = len(arr)
    while n > 1:
        maxIndex = findMaxIndex(arr, n) # find maxIndex in the array
        pancakeFlip(arr, maxIndex) # flip elements up to maxIndex
        pancakeFlip(arr, n - 1) # flip all elements
        n -= 1
    return arr

def findMaxIndex(arr, n):
    ans = 0
    for i in range(n):
        if arr[i] > arr[ans]:
            ans = i
    return ans

def pancakeFlip(arr, right): 
    left = 0
    while left < right: 
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

print(pancakeSort(arr))