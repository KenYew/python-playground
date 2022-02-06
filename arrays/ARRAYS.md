<style>
details > summary {
  padding: 4px;
  width: 100px;
  background-color: #3c3d3c;
  border: none;
  box-shadow: 1px 1px 2px #101010;
  cursor: pointer;
}
</style>

<img src="https://www.python.org/static/community_logos/python-logo-generic.svg" width="500px"/><br/>

#### 📖 Author: `Ken Yew Piong`
#### 📆 Last Modified:  <img src="https://img.shields.io/badge/dynamic/json?style=flat-square&labelColor=0039A9&color=027DFF&label=UTC&query=currentDateTime&url=http%3A%2F%2Fworldclockapi.com%2Fapi%2Fjson%2Futc%2Fnow&logo=AzureDevOps&logoColor=3399FF"/>
<a href="https://github.com/KenYew">
  <img src="https://img.shields.io/badge/GitHub-black?style=social&logo=GitHub"/>
</a>
<a href="https://gitlab.com/KenYew">
  <img src="https://img.shields.io/badge/GitLab-black?style=social&logo=GitLab"/>
</a>

---
# <div id='arrays'/> 🎹 **Arrays**

#### Blind 75
- ✅ Two Sum - https://leetcode.com/problems/two-sum/
- ✅ Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
- ✅ Contains Duplicate - https://leetcode.com/problems/contains-duplicate/
- ✅ Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/
- ✅ Maximum Subarray - https://leetcode.com/problems/maximum-subarray/
- Maximum Product Subarray - https://leetcode.com/problems/maximum-product-subarray/
- Find Minimum in Rotated Sorted Array - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
- Search in Rotated Sorted Array - https://leetcode.com/problems/search-in-rotated-sorted-array/
- ✅ 3Sum - https://leetcode.com/problems/3sum/
- Container With Most Water - https://leetcode.com/problems/container-with-most-water/

#### LeetCode Patterns
- `217` Contains Duplicate - https://leetcode.com/problems/contains-duplicate/
- `268` Missing Number - https://leetcode.com/problems/missing-number/
- `448` Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
- `136` Single Number - https://leetcode.com/problems/single-number/
- `2022` Convert 1D Array Into 2D Array - https://leetcode.com/problems/convert-1d-array-into-2d-array/
- ✅ `238` Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/
- `287` Find the Duplicate Number - https://leetcode.com/problems/find-the-duplicate-number/
- `442` Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/
- `73` Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/
- `54` Spiral Matrix - https://leetcode.com/problems/spiral-matrix/
- `48` Rotate Image - https://leetcode.com/problems/rotate-image/
- `128` Longest Consecutive Sequence - https://leetcode.com/problems/longest-consecutive-sequence/
- `41` First Missing Positive - https://leetcode.com/problems/first-missing-positive/
#### [📋 **Back to Table of Contents**](#toc)

---
## [🟩 Two Sum](https://leetcode.com/problems/two-sum/)
> Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
- [x] Input: `nums = [2, 7, 11, 15], target = 9`
- [x] Output: `[0, 1]`
- [x] Explanation: `Because nums[0] + nums[1] == 9, we return [0, 1].`
<details><summary><b>Solution</b></summary>
<p>

### **Brute Force**
```python
# O(n^2) Time | O(1) Space
def TwoSums(array, target):
    for i in range(len(array) - 1): 
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []
```

### **Hash Table**
```python
# O(n) time | O(n) space
def twoNumberSum(array, target): 
	nums = {}
	for num in array: 
		potentialMatch = target - num
		if potentialMatch in nums: 
			return [potentialMatch, num]
		else:
			nums[num] = True
	return []
```
</p>
</details>

✅ **HASH TABLE:** _Use hash table to instantly check for difference value, map will add index of last occurrence of a num, don’t use same element twice_

<details><summary><b>Solution</b></summary>
<p>

### **Two Pointers**
```python
# O(nlogn) Time | O(1) Space
def TwoSums(array, target):
    left = 0
    right = len(array) - 1
    array.sort()
    while (left < right):
        sum = array[left] + array[right]
        if sum > target:
            right -= 1
        elif sum < target:
            left += 1
        elif sum == target:
            return [array[left], array[right]]
    return -1 
```
</p>
</details>

✅ **TWO POINTERS:** _Sort the array, use two pointers on each end of the array and move pointers based on comparison between sum and targetNum_


---
## [🟩 Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
>* Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
>* A subarray is a contiguous part of an array.

- [x] Input: `nums = [-2,1,-3,4,-1,2,1,-5,4]`
- [x] Output: `6`
- [x] Explanation: `[4,-1,2,1] has the largest sum = 6.`
<details><summary><b>Solution</b></summary>
<p>

### **Kadane's Algorithm** 
```python
# O(n) Time | O(1) Space
def maximumSubarraySum(self, arr):
    # 1: Initialise maxSum and currentSum
    maxSum = float("-inf")
    currentSum = 0

    # 2: Traverse through each value in the input array
    for val in arr:
        # 3: Add the new value of the current element to our currentSum
        currentSum = currentSum + val
        # 4: If currentSum is bigger than maxSum, update maxSum with the new bigger number from currentSum
        if currentSum > maxSum:
            maxSum = currentSum
        # 5: If currentSum is less than zero, update currentSum to zero
        if currentSum < 0:
            currentSum = 0
    return maxSum
```
</p>
</details>

---
## [🟩 Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
>* You are given an array prices where `prices[i]` is the price of a given stock on the ith day.
>* You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
>* Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

- [x] Input: `prices = [7,1,5,3,6,4]`
- [x] Output: `5`
- [x] Explanation: 
  - `Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.`
  - `Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.`

<img src="https://leetcode.com/media/original_images/121_profit_graph.png" width="500"  /><br/>
The points of interest are the peaks and valleys in the given graph. We need to find the largest peak following the smallest valley. We can maintain two variables - minprice and maxprofit corresponding to the smallest valley and maximum profit (maximum difference between selling price and minprice) obtained so far respectively.
<details><summary><b>Solution</b></summary>
<p>

### **Kadane's Algorithm**
```python
# O(n) Time | O(1) Space
def maxProfit(prices):
    minPrice = float("inf")
    maxProfit = 0
    
    for price in prices: 
        if price < minPrice:
            minPrice = price
        elif price - minPrice > maxProfit:
            maxProfit = price - minPrice
    return maxProfit

# Kadane's Algorithm
# O(n) Time | O(1) Space
def maxProfit(prices):
    if len(prices) < 1:
        return 0
    
    minPrice = prices[0]
    maxProfit = 0
    for price in prices:
        minPrice = min(minPrice, price)
        profit = price - minPrice
        maxProfit = max(maxProfit, profit)
    return maxProfit
```
</p>
</details>

---
## [🟩 Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
> Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.
- [x] Input: `nums = [1,2,3,1]`
- [x] Output: `true`
<details><summary><b>Solution</b></summary>
<p>

### **Brute Force**
```python
# O(n^2) Time | O(1) Space - where n is the length of the input
def containsDuplicate(nums):
    for i in range(len(nums)):
        currentValue = nums[i]
        for j in range(i + 1, len(nums)):
            valueToCompare = nums[j]
            if currentValue == valueToCompare:
                return True
    return False
```
### **Hash Set**
```python
# O(n) Time | O(n) Space - where n is the length of the input
def containsDuplicate(nums):
    seen = set() # create a set which is an unordered collection of UNIQUE items
    for num in nums: # for every num in nums, we add to the set
        if num in seen: # but if we already find that num in the set, then we have a duplicate!
            return True
        seen.add(num)
    return False
```

### **Space Optimized**
```python
# O(n) Time | O(1) Space - where n is the length of the input
def containsDuplicate(nums):
    for num in nums: 
        absNum = abs(num)
        if nums[absNum - 1] < 0:
            return absNum
        nums[absNum - 1] *= -1
    return -1
```
### **One-Liner**
```python
# One-liner solution
def containsDuplicate(self, nums):
    return len(nums) > len(set(nums))
```
</p>
</details>

✅ **HASH SET:** _Use hash set to add and keep track of unique values in array, if value is seen in hash set, we found our duplicate_

---
## [🟩 Sorted Squared Array](https://www.algoexpert.io/questions/Sorted%20Squared%20Array)
>* Write a function that takes in a non-empty array of integers that are sorted in ascending order.
>* Return a new array of the same length with the squares of the original integers also sorted in ascending order.
- [x] Input: `array = [1, 2, 3, 5, 6, 8, 9]`
- [x] Output: `[1, 4, 9, 25, 36, 64, 81]`
<details><summary><b>Solution</b></summary>
<p>

### **Two Pointers**
```python
# O(n) Time | O(n) Space - where n is the length of the input array
def sortedSquaredArray(array):
    # 1: Initialise output array of size input array with dummy values
    ans = [0 for _ in array]
    # 2: Initialise two pointers on each end of the array
    left, right = 0, len(array) - 1
    # 3: Traversing idx pointer from end to beginning of the array because we want to write the largest to the smallest values
    for idx in reversed(range(len(array))): 
        # 4: If abs(left-most value) is > abs(right-most value) e.g.: [-4, 1, 2]
        if abs(array[left]) > abs(array[right]):
            # 5: Insert the square of the largest value at the current iteration idx (from n-th to 0)
            ans[idx] = array[left] * array[left]
            # 6: Then, increment the left pointer
            left += 1
        # 7: Else if abs(right-most value) is >= abs(left-most value) e.g.: [1, 2, 3]
        else: 
            # 8: Insert the square of the largest value at the current iteration idx (from n-th to 0)
            ans[idx] = array[right] * array[right]
            # 9: Then, decrement the right pointer
            right -= 1
    # 10: Finally, return the sorted squared array
    return ans
```
</p>
</details>

✅ **TWO POINTERS:** _Initialise output array with 0's, and left and right pointers on each end of array. Traverse idx from end to beginning of the array, if abs(leftVal) > abs(rightVal), write the ans[idx] = leftVal ** 2 and increment left, else abs(rightVal) >= abs(leftVal), write the ans[idx] = rightVal **2 and decrement right._

---
## [🟨 Validate Subsequence](https://www.algoexpert.io/questions/Validate%20Subsequence)
>* Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.
>* A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order as they appear in the array. 
>* For instance, the numbers `[1, 3, 4]` form a subsequence of the array `[1, 2, 3, 4]`, and so do
the numbers `[2, 4]`. 
>* Note that a single number in an array and the array itself are both valid subsequences of the array.
- [x] Input: `array = [5, 1, 22, 25, 6, -1, 8, 10], sequence = [1, 6, -1, 10]`
- [x] Output: `true`
<details><summary><b>Solution</b></summary>
<p>

### **Two Pointers**
```python
# O(n) Time | O(1) Space - where n is the length of the array
def isValidSubsequence(array, sequence):
    # 1: Initialise pointers for both the input array and input sequence
    arrIdx = 0
    seqIdx = 0
    
    # 2: While we have not finished traversing both the input array and input sequence,
    while arrIdx < len(array) and seqIdx < len(sequence):
        
        # 3: If the current values in both array and seq match, increment the seqIdx to look for the next pair of equal numbers
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1

        # 4: Otherwise, increment arrIdx and keep traversing the array to look for next pair of equal numbers
        arrIdx += 1

    # 5: Once we have incremented seqIdx enough times, return the Boolean answer of whether the sequence is valid (only if seqIdx == len(sequence))
    return seqIdx == len(sequence)
```
</p>
</details>

✅ **TWO POINTERS:** _Initialise pointer for both input arrays (arr, seq). While both pointers have not fully traversed their arrays, if values from both array match, increment seqIdx, otherwise keep incrementing arrIdx. Return Boolean logic seqIdx == len(sequence)_

---
## [🟨 Array Of Products](https://www.algoexpert.io/questions/Array%20Of%20Products)
>* Write a function that takes in a non-empty array of integers and returns an array of the same length, where each element in the output array is equal to the product of every other number in the input array.
>* In other words, the value at `output [i]` is equal to the product of every number in the input array other than `input[i]`.
>* Note that you're expected to solve this problem without using division.
- [x] Input: `array = [5, 1, 4, 2]`
- [x] Output: `[8, 40, 10, 20]`
- [x] Explanation:
```python
8 is equal to 1 x 4 x 2
40 is equal to 5 x 4 x 2
10 is equal to 5 x 1 x 2
20 is equal to 5 x 1 x 4
```
<details><summary><b>Solution</b></summary>
<p>

### **Brute Force**
```python
# O(n^2) Time | O(n) Space - where n is the length of the input array
def arrayOfProducts(array):
    result = []
    for i in range(len(array)):
        product = 1
        for j in range(len(array)):
            if i != j: 
                product *= array[j] 
        result.append(product)
    return result
```
### **Two Pointers - Less Optimised**
```python
# O(n) Time | O(n) Space - where n is the length of the input array
def arrayOfProducts(array):
    """
     *---L---->
    [5, 1, 4, 2]
    leftProducts = [1, 5, 5, 20]
     <---R----*
    [5, 1, 4, 2]
    rightProducts = [8, 8, 2, 1]
    products = [8, 40, 10, 20]
    """
    # 1: Initialise products arrays with 1s and size equals to input array
    products = [1 for _ in range(len(array))]
    leftProducts = [1 for _ in range(len(array))]
    rightProducts = [1 for _ in range(len(array))]
    
    # 2: Initialise leftRunningProduct = 1 to enable multiplication of running products from left to right
    leftRunningProduct = 1
    # 3: Loop through each element from left to right,
    for idx in range(len(array)): 
        # 4: Set the values of the leftProducts array with the leftRunningProduct value
        leftProducts[idx] = leftRunningProduct
        # 5: Multiplying up each element from left to right in a leftRunningProduct variable
        leftRunningProduct *= array[idx]

    # 6: Initialise rightRunningProduct = 1 to enable multiplication of running products from right to left
    rightRunningProduct = 1
    # 7: Loop through each element from right to left,
    for idx in reversed(range(len(array))): 
        # 8: Set the values of the rightProducts array with the rightRunningProduct value
        rightProducts[idx] = rightRunningProduct
        # 9: Multiplying up each element from right to left in a rightRunningProduct variable
        rightRunningProduct *= array[idx]
        
    # 10: Loop through each element from left to right,
    for idx in range(len(array)): 
        # 11: Multiply the elements of both leftProducts and rightProducts arrays
        products[idx] = leftProducts[idx] * rightProducts[idx]

    return products
```
### **Two Pointers - Optimised**
```python
# O(n) Time | O(n) Space - where n is the length of the input array
def arrayOfProducts(array):
    """
     *---L---->
    [5, 1, 4, 2]
    products = [1, 5, 5, 20]
     <---R----*
    [5, 1, 4, 2]
    products = [8, 40, 10, 20]
    """
    # 1: Initialise products array with 1s and size equals to input array
    products = [1 for _ in range(len(array))]
    
    # 2: Initialise leftRunningProduct = 1 to enable multiplication of running products from left to right
    leftRunningProduct = 1
    # 3: Loop through each element from left to right,
    for idx in range(len(array)):
        # 4: Set the values of each element in the answer array with the leftRunningProduct value
        products[idx] = leftRunningProduct
        # 5: Multiplying up each element from left to right in a leftRunningProduct variable
        leftRunningProduct *= array[idx]
        
    # 6: Initialise rightRunningProduct = 1 to enable multiplication of running products from right to left
    rightRunningProduct = 1
    # 7: Loop through each element from right to left,
    for idx in reversed(range(len(array))): 
        # 8: Set the values of each element in the answer array with the rightRunningProduct value
        products[idx] *= rightRunningProduct
        # 9: Multiplying up each element from right to left in a rightRunningProduct variable
        rightRunningProduct *= array[idx]
        
    return products
```
</p>
</details>

✅ **TWO POINTERS:** 
- Initialise the result array with 1s and equal to the size of the input array. 
- Starting with leftRunningProduct = 1, loop through each element of the input array from left to right, setting each element of the result array with leftRunningProduct as leftRunningProduct multiplies up each element from left to right. 
- Starting with rightRunningProduct = 1, loop through each element of the input array from right to left, multiplying each element of the result array with rightRunningProduct as rightRunningProduct multiplies up each element from right to left. 
- Return the result array.

---
## [🟨 Smallest Difference](https://www.algoexpert.io/questions/Smallest%20Difference)
>* Write a function that takes in two non-empty arrays of integers, finds the pair of numbers (one from each array) whose absolute difference is closest to zero, and returns an array containing these two numbers, with the number from the first array in the first position.
>* Note that the absolute difference of two integers is the distance between them on the real number line. For example, the absolute difference of -5 and 5 is 10, and the absolute difference of -5 and -4 is 1.
>* You can assume that there will only be one pair of numbers with the smallest difference.
- [x] Input: `arrayOne = [-1, 5, 10, 20, 28, 3], arrayTwo = [26, 134, 135, 15, 17]`
- [x] Output: `[28, 26]`
<details><summary><b>Solution</b></summary>
<p>

### **Two Pointers**
```python
# O(nlog(n) + mlog(m)) time | O(1) space
def smallestDifference(arrayOne, arrayTwo):
    # 1: Sort both input arrays first required for two pointer traversal
    arrayOne.sort() # O(nlog(n))
    arrayTwo.sort() # O(mlog(m))
    # 2: Initialise pointers, ans list and set MAX placeholders for smallestNum variable to be replaced by currentNum
    idxOne = idxTwo = currentNum = 0
    currentNum = smallestNum = float("inf")
    smallestPair = []
    
    ## EXAMPLE INPUT: 
    # sortedArrayOne = [-1, 3, 5, 10, 20, 28]
    #                    * <-- idxOne pointer
    # sortedArrayTwo = [15, 17, 26, 134, 135]
    #                    * <-- idxTwo pointer
    # Iteration #1: -1 < 15 so idxOne += 1 to bring the gap closer for min difference
    
    # 3: While both idx1 and idx2 pointers have not fully traversed the end of the list,
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum, secondNum = arrayOne[idxOne], arrayTwo[idxTwo]

        # 4: if num1 in array1 < num2 in array2, calculate the difference and increment idx1 (to close the gap and move closer to the smallest difference between both nums)
        if firstNum < secondNum: 
            currentNum = secondNum - firstNum
            idxOne += 1
        # 5: elif num2 in array2 < num1 in array1, calculate the difference and increment idx2 (to close the gap and move closer to the smallest difference between both nums)
        elif secondNum < firstNum:
            currentNum = firstNum - secondNum 
            idxTwo += 1
        else: 
            # 6: else if we're lucky to get two exactly same num1 and num2 values, this is the best answer possible with smallest difference = 0
            return [firstNum, secondNum]
        
        # 7: To keep track on the smallest difference, we keep updating the smallestNum if currentNum < smallestNum in this iteration,
        if currentNum < smallestNum: 
            smallestNum = currentNum # update smallestNum if currentNum < smallestNum in this iteration
            smallestPair = [firstNum, secondNum] # store also the smallest pair of nums in this iteration
    return smallestPair
```
</p>
</details>

✅ **TWO POINTERS:** 
1. Sort both input array1 and array2. 
2. While idx1 and idx2 pointers have not fully traversed their arrays,
3. If num1 < num2, calculate the difference and increment idx1, elif num2 < num1, calculate the difference and increment idx2, else return [num1, num2]. 
4. Incrementing idx1 or idx2 pointers will close the gap between two array values and move closer to the smallest difference
5. Keep track of smallestNum and smallestPair if currentNum < smallestNum.

---
## [🟨 Move Element To End](https://www.algoexpert.io/questions/Move%20Element%20To%20End)
>* You're given an array of integers and an integer. Write a function that moves all instances of that integer in the array to the end of the array and returns the array.
>* The function should perform this in place (i.e., it should mutate the input array) and doesn't need to maintain the order of the other integers.
- [x] Input: `array = [2, 1, 2, 2, 2, 3, 4, 2], toMove = 2`
- [x] Output: `[4, 1, 3, 2, 2, 2, 2, 2]` or `[1, 3, 4, 2, 2, 2, 2, 2]`
### **Two Pointers**
<details><summary><b>Solution</b></summary>
<p>

```python
# O(n) Time | O(1) Space - where n is the length of the input array
def moveElementToEnd(array, toMove):
    # 1: Initialise both left and right pointers of each end of the array
    left = 0
    right = len(array) - 1
    # 2: While both pointers have not fully traverse the array and pass each other,
    while left < right: 
        # 3: If the right pointer is on the value == toMoveNum, we keep decrementing the right pointer until it points to a number != toMoveNum
        while array[right] == toMove and left < right: # EDGE: left < right to ensure we don't keep decrementing the right pointer pass the left pointer and perform an accidental swap below
            right -= 1
        
        # 5: Finally, if left points to a value == toMoveNum (right would've pointed to a value != toMoveNum at this point), perform a swap
        if array[left] == toMove:
            array[left], array[right] = array[right], array[left]
        
        # 4: Then, keep moving the left pointer inward until value == toMoveNum
        left += 1
    return array
```
</p>
</details>

✅ **TWO POINTERS:** _Initialise two pointers (left & right) on each end. While left < right, nested while rightVal == toMoveNum, decrement right to ensure rightVal points to a swappable num != toMoveNum. Keep incrementing left. If leftVal == toMoveNum, perform swap._

### **Two Pointers - Order Preserved**
<details><summary><b>Solution</b></summary>
<p>

```python
# O(n) Time | O(1) Space - where n is the length of the input array
def moveElementToEnd(array, toMove):
    readIdx, writeIdx = 0, 0
    while readIdx < len(array): 
        if array[readIdx] != toMove: 
            array[readIdx], array[writeIdx] = array[writeIdx], array[readIdx]
            writeIdx += 1
        readIdx += 1
    return array

def moveElementToEnd(array, toMove):
    writeIdx = 0
    for readIdx in range(len(array)): 
        if array[readIdx] != toMove: 
            array[readIdx], array[writeIdx] = array[writeIdx], array[readIdx]
            writeIdx += 1
    return array

Working through an example, say we have an array [1, 0, 2, 0, 3] and toMove = 0.
When read = 0, write = 0 and write += 1.
When read = 1, then array[read] == 0 and write = 1.
When read = 2, then we swap array[2] (read) and array[1] (write). The array is now [1, 2, 0, 0, 3] and write = 2.
When read = 3, array[read] == 0 and we skip.
When read = 4, then we swap array[4] (read) and array[2] (write). The final array is [1, 2, 3, 0, 0].
```
</p>
</details>

✅ **TWO POINTERS:** _Initialise two pointers (readIdx & writeIdx) at 0. Iterate through the array with readIdx, if `array[readIdx] != toMove`, swap `array[readIdx], array[writeIdx] = array[writeIdx], array[readIdx]` and increment `writeIdx += 1`, keep traversing array with `readIdx`, return mutated array_

---
## [🟨 Longest Peak](https://www.algoexpert.io/questions/Longest%20Peak)
>* Write a function that takes in an array of integers and returns the length of the longest
peak in the array.
>* A peak is defined as adjacent integers in the array that are strictly increasing until they reach a tip (the highest value in the peak), at which point they become strictly decreasing. At least three integers are required to form a peak.
>* For example, the integers `1, 4, 10, 2` form a peak, but the integers `4, 0, 10` don't and neither do the integers `1, 2, 2, 0`. Similarly, the integers `1, 2, 3` don't form a peak because there aren't any strictly decreasing integers after the `3`.
- [x] Input: `array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]`
- [x] Output: `6`
- [x] Explanation: `0, 10, 6, 5, -1 -3` form the longest peak
<details><summary><b>Solution</b></summary>
<p>

### **Two Pointers**
```python
# O(n) time | O(1) space  - where n is the length of the input array
def longestPeak(array):
    # 1: Initialise peakIdx pointer to be 1 (since we need at least one value to the left to evaluate a potential peak)
    longestPeakLength = 0
    peakIdx = 1

    # 2: While peakIdx has not fully traversed the array,
    while peakIdx < len(array) - 1: 

        # 3: Check previous and next values to see if current peakIdxValue forms a peak
        isPeak = array[peakIdx] > array[peakIdx - 1] and array[peakIdx] > array[peakIdx + 1]

        # 4: If they don't form a peak, keep incrementing peakIdx and skip current iteration
        if not isPeak: 
            peakIdx += 1
            continue

        # 5: Else if current peakIdxValue does form a peak, let's evaluate how long is the peak.

        # 6: For the left side of the peak, set the leftIdx to point to the subsequent previous value (peakIdx - 2) and then perform a while loop that keeps decrementing the leftIdx if the previous values are consecutively decreasing
        leftIdx = peakIdx - 2
        while leftIdx >= 0 and array[leftIdx + 1] > array[leftIdx]: # traverse until leftIdx = 0
            leftIdx -= 1

        # 7: For the right side of the peak, set the rightIdx to point to the subsequent next value (peakIdx + 2) and then perform a while loop that keeps incrementing the rightIdx if the next values are consecutively increasing
        rightIdx = peakIdx + 2
        while rightIdx < len(array) and array[rightIdx - 1] > array[rightIdx]: # traverse until rightIdx = len(array) - 1
            rightIdx += 1
            
        # 8: Evaluate the total length of the peak by using the difference between the two pointers (accounting for zero-indexing)
        currentPeakLength = rightIdx - leftIdx - 1

        # 9: Evaluate only the MAX between the longestPeakLength (from previous iteration) and currentPeakLength (current iteration)
        longestPeakLength = max(longestPeakLength, currentPeakLength) 

        # 10: Update the peakIdx to be the right-most index. This is will be the new starting point to look for the next peak as we keep traversing the array.
        peakIdx = rightIdx
        
    return longestPeakLength
```
</p>
</details>

✅ **TWO POINTERS:** 
1. Intialise peakIdx to traverse the array and find a potential peak.
2. If peak is found, set leftIdx and rightIdx to be peakIdx - 2 and peakIdx + 2 to. 
3. Decrement leftIdx in a while loop if previous values are consecutively decreasing.
4. Increment rightIdx in a while loop if next values are consecutively increasing. 
5. Evaluate currentPeakLength by calculating the difference between leftIdx and rightIdx. 
6. Update peakIdx to be rightIdx to find the next potential longest peak. 
7. Return max(longestPeakLength, currentPeakLength)

---
## [🟨 3Sum](https://leetcode.com/problems/3sum/)
> Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.
- [x] Input: `nums = [-1,0,1,2,-1,-4]`
- [x] Output: `[[-1,-1,2],[-1,0,1]]`

- [x] Input: `nums = []` or `nums = [0]`
- [x] Output: `[]`
<details><summary><b>Solution</b></summary>
<p>

### [**Two Pointers**](https://leetcode.com/problems/two-sum/discuss/737092/Sum-MegaPost-Python3-Solution-with-a-detailed-explanation)
```python
# O(n^2) Time | O(n) Space
def threeSum(nums: List[int]) -> List[List[int]]:
    # 1: Sort the input array
    nums.sort()
    ans = []
    
    # 2: Perform a single pass of the input array with idx as the pointer
    for idx, val in enumerate(nums): 
        # EDGE 1: If there are two adjacent elements of the same value for indices after idx = 0, skip iteration to prevent checking for duplicates
        if idx > 0 and nums[idx] == nums[idx - 1]:
            continue

        # 3: With the idx pointer taking care of the 1st valueToSum, intialise left (next to idx) and right pointers
        left = idx + 1 # Left pointer (2nd pointer) needs to be next to the idx pointer (1st pointer)
        right = len(nums) - 1 # Right pointer (3rd pointer) is at the end of the array

        # 4: Perform 2Sum algorithm, while both pointers haven't traversed the entire array yet,
        while left < right: 
            # 5: Compute threeSum with idx, left and right pointers
            threeSum = nums[idx] + nums[left] + nums[right] 
            # 6: If threeSum < 0, threeSum is too small, so left pointer is incremented to increase value of threeSum
            if threeSum < 0: 
                left += 1
            # 7: If threeSum > 0, threeSum is too big, so right pointer is decremented to decrease value of threeSum
            elif threeSum > 0:  
                right -= 1
            # 8: Else, we have found the threeSum that equates to 0, so we append the answer
            else: 
                ans.append([nums[idx], nums[left], nums[right]])

                # EDGE CASE TO SKIP DUPLICATES
                #  [-3 -2, -2, 0, 0, 2, 2]
                # [ IDX L               R]
                # EDGE 2: If two adjacent elements have the same value while the left and right pointers haven't finished traversing the entire array yet, keep moving the pointers to prevent checking for duiplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # 9: Move left and right pointers inwards once to continue traversing the array for next potential threeSum
                left += 1 
                right -= 1
    return ans
```
</p>
</details>

✅ **TWO POINTERS:** 
- `ThreeSum: A + B + C = 0` 
- _Sort input array, perform a FOR loop for A, then set Two Pointers (L & R) for B and C. Increment L if sum is too small and decrement R if sum is too big._
- _To prevent duplicates, if A == prevA, skip FOR loop iteration. If B == prevB, increment L in the TwoPointer WHILE loop_
<details><summary><b>Solution</b></summary>
<p>

### **TargetSum Variant**
```python
# O(n^2) time | O(n) space
def threeNumberSum(array, targetSum):
    # 1: Sort the input array for two pointer traversal
    array.sort()
    ans = []

    # 2: idx pointer loops through all values from index 0 to "n - 2" for the 1st value of the sum
    for idx in range(len(array) - 2): # since we're looking for a triplet, in the n-th iteration of the for loop, the idxPointer will always be 3rd from last of the array to allow for leftPointer and rightPointer to fit in the triplet

        # 3: Initialise left and right pointers for the 2nd and 3rd value of the sum
        left = idx + 1
        right = len(array) - 1 # since we're dealing with pointers, we must account for Python's zero indexing
        # POINTERS VISUALIZATION
        # [  -3  -2   -2  0  0  2  2]
        # [ IDX LEFT             RIGHT]
        # FORLOOP ^---TWO POINTER---^

        # 4: While left and right pointers have not traverse the entire list and pass each other,
        while left < right:

            # 5: Evaluate the currentSum of the current iteration
            currentSum = array[idx] + array[left] + array[right] 

            # 6: If currentSum of the current iteration < targetSum, increment left to increase value
            if currentSum < targetSum:
                left += 1
            # 7: If currentSum of the current iteration > targetSum, decrement right to decrease value
            elif currentSum > targetSum:
                right -= 1

            # 8: If we found the right combination to equal targetSum, append the 3 values of currentSum
            elif currentSum == targetSum:
                ans.append([array[idx], array[left], array[right]])

                # 9: and move both left and right pointers inwards to look for more potential sums
                left += 1
                right -= 1
    return ans
```
</p>
</details>

✅ **TWO POINTERS:** 
- `ThreeSum: A + B + C = 0` 
- _Sort input array, perform a FOR loop for A, then set Two Pointers (L & R) for B and C. Increment L if sum is too small and decrement R if sum is too big. When targetSum is found, find the next targetSum by traversing both L & R inwards._
