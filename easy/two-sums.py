# O(nlogn) Time | O(1) Space
def TwoSums(array, target):
    left = 0
    right = len(array) - 1
    array.sort()
    while (left < right):
        sum = array[left] + array[right]
        if sum > target:
            right -= 1
        elif sum < target:
            left += 1
        elif sum == target:
            return [array[left], array[right]]
    return -1 

myArray = [1, 2, 3, 4, 5]
myTarget = 4
print(TwoSums(myArray, myTarget))