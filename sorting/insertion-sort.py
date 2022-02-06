# INSERTION SORT
# O(n^2) Avg Time | O(1) Space
def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            swap(j, j - 1, array)
            j -= 1
    return array

# Helper Functions
def swap(left, right, array):
	array[left], array[right] = array[right], array[left]

myArray = [8, 5, 2, 9, 5, 6, 3]
print(insertionSort(myArray))