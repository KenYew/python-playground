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