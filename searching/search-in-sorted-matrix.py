matrix = [
    [1, 4, 7, 12, 15, 1000], # ------------> # | Values increases from left to right
    [2, 5, 19, 31, 32, 1001],                # |       
    [3, 8, 24, 33, 35, 1002],                # | 
    [40, 41, 42, 44, 45, 1003],              # | 
    [99, 100, 103, 106, 128, 1004]           # v Values increases from top to bottom
  ]
target = 44
# Output: [3, 3]
  
# O(n + m) time | O(1) space
def searchInSortedMatrix(matrix, target):
    # Initialise pointers for row and col
    row = 0
    col = len(matrix[0]) - 1
    while row < len(matrix) and col >= 0: 
        if matrix[row][col] > target: # If current number is larger than targetNum,
            col -= 1 # move left in columns to decrement the number
        elif matrix[row][col] < target: # If current number is smaller than targetNum,
            row += 1 # move right in rows to increment the number
        else: # If current number is exactly the targetNum, return the answer
            return [row, col]
    return [-1, -1] # If we are unable to find number equal to targetNum, default to returning [-1, -1]

print(searchInSortedMatrix(matrix, target))
