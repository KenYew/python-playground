# O(n) Time | O(1) Space where n is the number of elements in the array
def removeDuplicates(array): 
    idx, nextNonDuplicate = 0, 1
    while (idx < len(array)):
        if array[nextNonDuplicate - 1] != array[idx]:
            array[nextNonDuplicate] = array[idx]
            nextNonDuplicate += 1
        idx += 1
    return nextNonDuplicate

def main():
    array = [2, 3, 3, 3, 6, 9, 9]
    print(removeDuplicates(array))
    
main()