# O(n) Time | O(n) Space
def majorityElement(array): 
    count = {}
    result, maxCount = 0, 0
    
    for val in array:
        count[val] = 1 + count.get(val, 0)
        result = val if count[val] > maxCount else result
        maxCount = max(count[val], maxCount)
    return result

# https://leetcode.com/problems/majority-element-ii/discuss/63537/My-understanding-of-Boyer-Moore-Majority-Vote
# O(1) Time | O(1) Space
# Boyer Moore Voting Algorithm
def majorityElement(array): 
    result, count = 0, 0
    
    for value in array:
        if count == 0: 
            result = value
        count += (1 if value == result else - 1)
    return result
        
# O(1) Time | O(1) Space
# Modified Boyer Moore Voting Algorithm
def majorityElementTwo(array):
    if not array:
        return []
    candidateOne, candidateTwo = 0, 1
    countOne, countTwo = 0, 0
    
    for value in array: 
        if value == candidateOne: 
            countOne += 1
        elif value == candidateTwo:
            countTwo += 1
        elif countOne == 0:
            candidateOne, countOne = value, 1
        elif countTwo == 0:
            candidateTwo, countTwo = value, 1
        else:
            countOne, countTwo = countOne - 1, countTwo - 1
    return [value for value in (candidateOne, candidateTwo) if array.count(value) > len(array) // 3]