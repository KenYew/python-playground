# O(n) Time | O(n) Space - where n is the length of the input array
def sortedSquaredArray(array):
    squares = [0 for _ in array]
    highestSquareIdx = len(array) - 1
    left, right = 0, len(array) - 1
    
    while left <= right: 
        leftSquare = array[left] * array[left]
        rightSquare = array[right] * array[right]
        if leftSquare > rightSquare: 
            squares[highestSquareIdx] = leftSquare
            left += 1
        else:
            squares[highestSquareIdx] = rightSquare
            right -= 1
        highestSquareIdx -= 1
    return squares