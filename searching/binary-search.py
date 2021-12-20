# Time complexity: O(nlogn) # sorted 
# Space complexity: O(1) # not introducing any new data structure
def binarySearch(array, target):
    low = 0
    high = len(array) - 1
	
    while (low <= high):
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        else:
            if (array[mid] < target):
                low = mid + 1
            else: 
                high = mid - 1
    return -1

array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33
print(binarySearch(array, target))