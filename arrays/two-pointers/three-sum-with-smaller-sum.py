# Return counts
# O(nlogn) Time 
def threeSumSmaller(array, targetSum): 
    array.sort()
    totalCount = 0 
    
    # 1: Iterate *idx for X 
    for idx in range(len(array) - 2):
        # 2: We need to search a pair of numbers (Y & Z) such that it is less than targetSum - X 
        # Since the equation goes X + Y + Z < targetSum so Y + Z < targetSum - X
        totalCount += searchPair(array, targetSum - array[idx], idx)
        
    return totalCount

# O(n) Time 
# 3: Helper function to search for Y and Z such that they are < targetSum - X using two pointers approach
def searchPair(array, targetSum, idx):
    count = 0
    left, right = idx + 1, len(array) - 1
    while left < right: 
        _sum = array[left] + array[right]
        if _sum < targetSum: 
            count += right - left
            left += 1
        else: 
            right -= 1
    return count

# Total Time Complexity: O(nlogn + n) is asymptotically equivalent to O(n)
# Total Space Complexity: O(n) for the output array

# Return arrays   
# O(nlogn) Time 
def threeSumSmaller(array, targetSum): 
    array.sort()
    triplets = []
    
    # 1: Iterate *idx for X 
    for idx in range(len(array) - 2):
        # 2: We need to search a pair of numbers (Y & Z) such that it is less than targetSum - X 
        # Since the equation goes X + Y + Z < targetSum so Y + Z < targetSum - X
        searchPair(array, targetSum - array[idx], idx, triplets)
    return triplets

# O(n^2) Time
# 3: Helper function to search for Y and Z such that they are < targetSum - X using two pointers approach
def searchPair(array, targetSum, idx, triplets):
    left, right = idx + 1, len(array) - 1
    while left < right: 
        _sum = array[left] + array[right]
        if _sum < targetSum: 
            for jdx in range(right, left, -1):
                triplets.append([array[idx], array[left], array[jdx]])
            left += 1
        else: 
            right -= 1
    return triplets

# Total Time Complexity: O(nlogn + n^2) is asymptotically equivalent to O(n^3)
# Total Space Complexity: O(n) for the output array

def main():
    array = [-1, 0, 2, 3]
    targetSum = 3
    print(threeSumSmaller(array, targetSum))
    array = [-1, 4, 2, 1, 3]
    targetSum = 5 
    print(threeSumSmaller(array, targetSum))
    
main()