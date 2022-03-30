# O(n) Time | O(1) Space
def dutchFlagSort(array): 
    # all elements < low are 0, and all elements > high are 2
    # all elements from >= low < i are 1
    idx, low, high = 0, 0, len(array) - 1 
    # *low is the pivot for all 0s and *high is the pivot for all 2s
    while idx <= high:
        if array[idx] == 0: 
            array[idx], array[low] = array[low], array[idx]
            # increment 'i' and 'low'
            idx += 1
            low += 1
        elif array[idx] == 1: 
            idx += 1
        else: # if array[idx] == 2
            array[idx], array[high] = array[high], array[idx]
            # decrement 'high' only, after the swap the number at index 'i' could be 0, 1 or 2
            high -= 1
            
def main():
    array = [1, 0, 2, 1, 0]
    dutchFlagSort(array)
    print(array)
    
    array = [2, 2, 0, 1, 2, 0]
    dutchFlagSort(array)
    print(array)
    
main()