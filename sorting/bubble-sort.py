# BUBBLE SORT
# BEST: O(n) Time | O(1) Space
# AVG: O(n^2) Time | O(1) Space
# WORST: O(n^2) Time | O(1) Space
def bubbleSort(array):
    isSorted = False
    counter = 0
    while not isSorted: 
        isSorted = True
        for idx in range(len(array) - 1 - counter):
            if array[idx] > array[idx + 1]:
                swap(idx, idx + 1, array)
                isSorted = False
        counter += 1
    return array

# Helper Functions
def swap(left, right, array):
	array[left], array[right] = array[right], array[left]

myArray = [8, 5, 2, 9, 5, 6, 3]
print(bubbleSort(myArray))