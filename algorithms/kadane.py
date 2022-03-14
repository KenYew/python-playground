# O(n) Time | O(1) Space - where n is the length of the input array
def kadane(array): 
    maxSumEndingHere = array[0]
    maxSoFar = array[0]
    
    for idx in range(1, len(array)): 
        num = array[idx]
        maxSumEndingHere = max(num, maxSumEndingHere + num)
        maxSoFar = max(maxSoFar, maxSumEndingHere)
    return maxSoFar

""" 
Example:
Input: 
[3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
maxSumEndingHere = max(currentNum, maxSumEndingHere)
[3, 8, -1, 1, 4, 2, 5, 9, 16, 18, 9, 15, 18, 19, 14, 18]
maxSoFar = max(maxSoFar, maxSumEndingHere)
[3, 8, 8, 8, 8, 8, 8, 9, 16, 18, 18, 18, 18, 19, 19, 19]
Output: 19
"""