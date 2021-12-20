def moveElementToEnd(array, toMove):
    left = 0
    right = len(array) - 1
    while left < right: 
        # keep moving the right pointer inward until we meet a number that is not the targetNum
        while left < right and array[right] == toMove: # we add left < right condition here to ensure we don't keep decrementing the right pointer pass the left pointer and perform an accidental swap when the below if statement was to be true
            right -= 1
        # then keep moving the left pointer inward until we meet a number that is the targetNum to perform a swap
        if array[left] == toMove:
            array[left], array[right] = array[right], array[left]
        left += 1
    return array

 
array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2
print(moveElementToEnd(array, toMove))