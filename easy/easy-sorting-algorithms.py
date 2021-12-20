# INSERTION SORT
# O(n^2) Avg Time | O(1) Space
def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            swap(j, j - 1, array)
            j -= 1
    return array
				
# BUBBLE SORT
# O(n^2) Avg Time | O(1) Space
def bubbleSort(array):
    isSorted = False
    incrementor = 0
    while not isSorted: 
        isSorted = True
        for i in range(len(array) - 1 - incrementor):
            if array[i] > array[i + 1]:
                swap(i, i + 1, array)
                isSorted = False
        incrementor += 1
    return array

# SELECTION SORT
# O(n^2) Avg Time | O(1) Space
def selectionSort(array):
	currentIdx = 0 
	while currentIdx < len(array) - 1: 
		smallestIdx = currentIdx
		for i in range(currentIdx + 1, len(array)):
			if array[smallestIdx] > array[i]:
				smallestIdx = i
		swap(currentIdx, smallestIdx, array)
		currentIdx += 1
	return array 

# Helper Functions
def swap(left, right, array):
	array[left], array[right] = array[right], array[left]

myArray = [8, 5, 2, 9, 5, 6, 3]
print(selectionSort(myArray))