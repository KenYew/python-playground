# O(n) Time - Sliding Window
# O(n^2) Time - Nested For-Loop (Worst Case)
# O(n^3) Total Time | O(n) Space 
from collections import deque
def findSubarrays(array, target):
    result = []
    product, left = 1, 0
    # 1: Increment *right to start the sliding window
    for right in range(len(array)): 
        # 2: Sliding the window, multiply all elements going in
        product *= array[right]
        # 3: If product >= target and left < len(array), start shrinking the sliding window!
        while product >= target and left < len(array): 
            # 4: Sliding the window, divide all elements going out
            product /= array[left]
            # 5: Shrink the window one element at a time
            left += 1
            
        # Note: Since the product of all numbers from left to right is less than the target therefore,
        # all subarrays from left to right will have a product less than the target too; to avoid
        # duplicates, we will start with a subarray containing only arr[right] and then extend it
        
        # 6: Instantiate the deque() object - a doubly ended queue with O(1) Time append or pop operations
        tempList = deque()
        # 7: With *left and *right pointers correctly in place, iterate *idx and append all the answers from *right to *left      
        for idx in reversed(range(left, right + 1)): # or for idx in range(right, left - 1, -1):
            # 8: Append all the answers into a temporary subarray (inserting from the left)
            tempList.appendleft(array[idx])
            # 9: Append the subarray into the final result array
            result.append(list(tempList))
    return result

def main():
    print(findSubarrays([2, 5, 3, 10], 30))
    print(findSubarrays([8, 2, 6, 5], 50))
    
main()