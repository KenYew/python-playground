<img src="https://www.python.org/static/community_logos/python-logo-generic.svg" width="500px"/><br/>

# **💻 Python Coding Patterns**
### 📖 **Author:** **`Ken Yew Piong`**
### 📆 **Last Modified:**  <img src="https://img.shields.io/badge/dynamic/json?style=flat-square&labelColor=0039A9&color=027DFF&label=UTC&query=currentDateTime&url=http%3A%2F%2Fworldclockapi.com%2Fapi%2Fjson%2Futc%2Fnow&logo=AzureDevOps&logoColor=3399FF"/>
<a href="https://github.com/KenYew">
  <img src="https://img.shields.io/badge/GitHub-black?style=social&logo=GitHub"/>
</a>
<a href="https://gitlab.com/KenYew">
  <img src="https://img.shields.io/badge/GitLab-black?style=social&logo=GitLab"/>
</a>

---
# <div id='toc'/> 📋 **Table of Contents** 
1. ### [🎹 **Arrays**](#arrays)
0. ### [🔢 **Matrix**](#matrix)
0. ### [🔤 **Strings**](#strings)
0. ### [📝 **Linked Lists**](#linkedlists)
0. ### [📈 **Graphs**](#graphs) 
0. ### [🎄 **Trees**](#trees)
0. ### [🏔 **Heaps**](#heaps)
0. ### [🥞 **Stacks**](#stacks)
0.  ### [⏱ **Intervals**](#intervals)
0.  ### [🔎 **Search Algorithms**](#search)
0. ### [📚 **Sorting Algorithms**](#sort)
0. ### [📱 **Dynamic Programming**](#dp)
0. ### [♽ **Recursion**](#recursion)
0. ### [⚡️ **Binaries**](#binaries)

---
# 📱 [Coding Patterns](https://seanprashad.com/leetcode-patterns/)
## 🎹 **If input array is sorted:**
- `Binary search`
- `Two pointers`

## 🔢 **If asked for all permutations/subsets:**
- `Backtracking`

## 🎄 **If given a tree:**
- `DFS`
- `BFS`

## 📈 **If given a graph:**
- `DFS`
- `BFS`

## 📝 **If given a linked list:**
- `Two pointers`

## ♽ **If recursion is banned:**
- `Stack`

## 🔎 **If must solve in-place:**
- `Swap corresponding values`
- `Store one or more different values in the same pointer`

## 🎹 **If asked for maximum/minumum subarray/subset/options:**
- `Dynamic programming`

## 📚 **If asked for top/least K items:**
- `Heap`

## 🔤 **If asked for common strings:**
- `Map`
- `Trie`

## 📱 **Else**
- `Map/Set for O(1) time & O(n) space`
- `Sort input for O(nlogn) time and O(1) space`
---
# <div id='arrays'/> 🎹 **Arrays**

- ✅ Two Sum - https://leetcode.com/problems/two-sum/
- ✅ Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
- ✅ Contains Duplicate - https://leetcode.com/problems/contains-duplicate/
- Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/
- ✅ Maximum Subarray - https://leetcode.com/problems/maximum-subarray/
- Maximum Product Subarray - https://leetcode.com/problems/maximum-product-subarray/
- Find Minimum in Rotated Sorted Array - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
- Search in Rotated Sorted Array - https://leetcode.com/problems/search-in-rotated-sorted-array/
- ✅ 3Sum - https://leetcode.com/problems/3sum/
- Container With Most Water - https://leetcode.com/problems/container-with-most-water/
### [📋 **Back to Table of Contents**](#toc)

---
## [🟩 Two Sum](https://leetcode.com/problems/two-sum/)
> Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
- [x] Input: `nums = [2, 7, 11, 15], target = 9`
- [x] Output: `[0, 1]`
- [x] Explanation: `Because nums[0] + nums[1] == 9, we return [0, 1].`

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
✅ **TWO POINTERS:** _Sort the array, use two pointers on each end of the array and move pointers based on comparison between sum and targetNum_

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
✅ **HASH TABLE:** _Use hash map to instantly check for difference value, map will add index of last occurrence of a num, don’t use same element twice_

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

### **Sliding Window**
```python
# O(n) Time | O(1) Space
def maxProfit(prices: List[int]) -> int:
  if len(prices) <= 1:
      return 0
  buy_idx, sell_idx, min_idx, ans = 0, 1, 0, 0
  while sell_idx < len(prices):
      if prices[buy_idx] > prices[min_idx]:
          buy_idx = min_idx
      ans = max(ans, prices[sell_idx] - prices[buy_idx])
      if prices[sell_idx] < prices[min_idx]:
          min_idx = sell_idx
      sell_idx += 1
  return ans
```
✅ **SLIDING WINDOW:** _Find local min and search for local max using a sliding window_

---
## [🟩 Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
> Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.
- [x] Input: `nums = [1,2,3,1]`
- [x] Output: `true`

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
### **One-Liner**
```python
# One-liner solution
def containsDuplicate(self, nums):
    return len(nums) > len(set(nums))
```
✅ **HASH SET:** _Use hash set to add and keep track of unique values in array, if value is seen in hash set, we found our duplicate_

---
## [🟩 Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
>* Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
>* A subarray is a contiguous part of an array.

- [x] Input: `nums = [-2,1,-3,4,-1,2,1,-5,4]`
- [x] Output: `6`
- [x] Explanation: `[4,-1,2,1] has the largest sum = 6.`

### [**Divide and Conquer**](https://leetcode.com/problems/maximum-subarray/discuss/1595195/C%2B%2BPython-7-Simple-Solutions-w-Explanation-or-Brute-Force-%2B-DP-%2B-Kadane-%2B-Divide-and-Conquer)
```python
# O(nlogn) Time | O(logn) Space
def maxSubArray(self, nums):
    def maxSubArray(A, L, R):
        if L > R: return -inf
        mid, left_sum, right_sum, cur_sum = (L + R) // 2, 0, 0, 0
        for i in range(mid-1, L-1, -1):
            left_sum = max(left_sum, cur_sum := cur_sum + A[i])
        cur_sum = 0
        for i in range(mid+1, R+1):
            right_sum = max(right_sum, cur_sum := cur_sum + A[i])
        return max(maxSubArray(A, L, mid-1), maxSubArray(A, mid+1, R), left_sum + A[mid] + right_sum)
    return maxSubArray(nums, 0, len(nums)-1)
```
✅ **DIVIDE AND CONQUER:** _pattern: prev subarray cant be negative, dynamic programming: compute max sum for each prefix_

---
## [🟨 3Sum](https://leetcode.com/problems/3sum/)
> Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.
- [x] Input: `nums = [-1,0,1,2,-1,-4]`
- [x] Output: `[[-1,-1,2],[-1,0,1]]`

- [x] Input: `nums = []` or `nums = [0]`
- [x] Output: `[]`

### [**Two Pointers**](https://leetcode.com/problems/two-sum/discuss/737092/Sum-MegaPost-Python3-Solution-with-a-detailed-explanation)
```python
# O(n^2) Time | O(n) Space
def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    ans = []
    
    for idx, val in enumerate(nums): 
        if idx > 0 and nums[idx] == nums[idx - 1]: # Skip iteration if there are two adjacent elements of the same value (e.g.: [-2, -2, 0, 0, 2, 2])
            continue
        
        # Once the idx pointer (1st pointer) has been accounted for, we simply perform TwoSum (Two Pointer Approach)
        left = idx + 1 # Left pointer (2nd pointer) needs to be next to the idx pointer (1st pointer)
        right = len(nums) - 1 # Right pointer (3rd pointer) is at the end of the array
        while left < right: # While both pointers haven't traversed the entire list yet,
            threeSum = nums[idx] + nums[left] + nums[right] # Compute threeSum
            if threeSum < 0: # if threeSum is smaller than 0, our threeSum is too SMALL, so incrememt the left pointer to increase the threeSum
                left += 1
            elif threeSum > 0: # if threeSum is bigger than 0, our threeSum is too BIG, so decrement the right pointer to decrease the threeSum 
                right -= 1
            else: # else, we have found the threeSum that equates to 0, so we append the answer
                ans.append([nums[idx], nums[left], nums[right]])
                left += 1 # keep traversing to find the next threeSum
                right -= 1

                # EDGE CASE TO SKIP DUPLICATES
                #  [-3 -2, -2, 0, 0, 2, 2]
                # [ IDX L               R]
                while nums[left] == nums[left - 1] and left < right: # Keep moving the left pointer if there are two adjacent elements of the same value and while the pointers haven't traversed the entire list yet,
                    left += 1
    return ans
```
✅ **TWO POINTERS:** 
- `ThreeSum: A + B + C = 0` 
- _Sort input array, perform a FOR loop for A, then set Two Pointers (L & R) for B and C. Increment L if sum is too small and decrement R if sum is too big._
- _To prevent duplicates, if A == prevA, skip FOR loop iteration. If B == prevB, increment L in the TwoPointer WHILE loop_

### **TargetSum Variant**
```python
# O(n^2) time | O(n) space
def threeNumberSum(array, targetSum):
    array.sort()
    ans = []
    for idx in range(len(array) - 2): # since we're looking for a triplet, in the n-th iteration of the for loop, the idxPointer will always be 3rd from last of the array to allow for leftPointer and rightPointer to fit in the triplet
        left = idx + 1
        right = len(array) - 1 # since we're dealing with pointers, we must account for Python's zero indexing
        # POINTERS VISUALIZATION
        # [  -3  -2   -2  0  0  2  2]
        # [ IDX LEFT             RIGHT]
        # FORLOOP ^---TWO POINTER---^
        while left < right:
            currentSum = array[idx] + array[left] + array[right] 
            if currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
            elif currentSum == targetSum:
                ans.append([array[idx], array[left], array[right]])
                left += 1
                right -= 1
    return ans
```
✅ **TWO POINTERS:** 
- `ThreeSum: A + B + C = 0` 
- _Sort input array, perform a FOR loop for A, then set Two Pointers (L & R) for B and C. Increment L if sum is too small and decrement R if sum is too big. When targetSum is found, find the next targetSum by traversing both L & R inwards._

---
# <div id='matrix'/> 🔢 **Matrix**

- Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/
- ✅ Spiral Matrix - https://leetcode.com/problems/spiral-matrix/
- Rotate Image - https://leetcode.com/problems/rotate-image/
- Word Search - https://leetcode.com/problems/word-search/
### [📋 **Back to Table of Contents**](#toc)
---
## [🟨 Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)
>* Given an m x n matrix, return all elements of the matrix in spiral order.

- [x] Input: `matrix = [[1,2,3],[4,5,6],[7,8,9]]`
- [x] Output: `[1,2,3,6,9,8,7,4,5]`

<img src="https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg" width="250" align="left" /><br/>
<img src="https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg" width="300"  /><br/>

### **Two Pointers**
```python
# O(n) Time | O(n) Space
def spiralTraverse(array):
    startRow, endRow = 0, len(array) - 1 # Iteration 1: 0, 3
    startCol, endCol = 0, len(array[0]) - 1 # Iteration 1: 0, 3
    ans = []
    
    while startRow <= endRow and startCol <= endCol: 
        for col in range(startCol, endCol + 1): # Iteration 1: 0, 4 (0 -> 3) Iteration 2: 1, 3 (1 -> 2)
            ans.append(array[startRow][col])
        for row in range(startRow + 1, endRow + 1): # Iteration 1: 1, 4 (1 -> 3) Iteration 2: 2, 3 (2)
            ans.append(array[row][endCol])
        for col in reversed(range(startCol, endCol)): # Iteration 1: 3, 0 (2 -> 0) Iteration 2: 2, 1 (1)
            if startRow == endRow: # Handle the edge case when there's a single row in the middle of the matrix. In this case, we don't want to double-count the values in this row, which we've already counted in the first for loop above.
                break
            ans.append(array[endRow][col])
        for row in reversed(range(startRow + 1, endRow)): # Iteration 1: 3, 1 (2 -> 1) Iteration 2:  2, 2 (BREAK)
            if startCol == endCol: # Handle the edge case when there's a single column in the middle of the matrix. In this case, we don't want to double-count the values in this column, which we've already counted in the second for loop above.
                break
            ans.append(array[row][startCol])
        startRow += 1 # Value Updated: 1
        endRow -= 1 # Value Updated: 2
        startCol += 1 # Value Updated: 1
        endCol -= 1 # Value Updated: 2
```
✅ **TWO POINTERS:** _Keep track of visited cells; keep track of boundaries, layer-by-layer_

---
# <div id='strings'/> 🔤 **Strings**

- Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/
- Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/
- Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/
- Valid Anagram - https://leetcode.com/problems/valid-anagram/
- ✅ Group Anagrams - https://leetcode.com/problems/group-anagrams/
- Valid Parentheses - https://leetcode.com/problems/valid-parentheses/
- Valid Palindrome - https://leetcode.com/problems/valid-palindrome/
- Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/
- Palindromic Substrings - https://leetcode.com/problems/palindromic-substrings/
- Encode and Decode Strings (Leetcode Premium) - https://leetcode.com/problems/encode-and-decode-strings/
### [📋 **Back to Table of Contents**](#toc)
---
## [🟨 Group Anagrams](https://leetcode.com/problems/group-anagrams/)
>* Given an array of strings `strs`, group the **anagrams** together. You can return the answer in **any order**.
>* An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

- [x] Input: `strs = ["eat","tea","tan","ate","nat","bat"]`
- [x] Output: `[["bat"],["nat","tan"],["ate","eat","tea"]]`

### **Hash Map**
```python
# O(w * nlog(n)) time | O(w * n) space
# w - the number of words
# n - the length of the longest word
def groupAnagrams(words):
    anagrams = {}
    for word in words: 
        sortedWord = "".join(sorted(word))
        if sortedWord in anagrams:
            anagrams[sortedWord].append(word)
        else:
            anagrams[sortedWord] = [word]
    return list(anagrams.values())
```
✅ **HASH MAP:** _Loop and sort each word, append `sortedWord/word` key/value pairs in `anagrams_dict`, if sortedWord is in `anagrams_dict`, set `anagrams_dict[sortedWord].append(word)`, return `anagram_dict.values()`_

---
## [🟩 Caesar Cipher Encryptor](https://www.algoexpert.io/questions/Caesar%20Cipher%20Encryptor)
>* Given a non-empty string of lowercase letters and a non-negative integer representing
a key, write a function that returns a new string obtained by shifting every letter in the
input string by k positions in the alphabet, where k is the key.
>* Note that letters should "wrap" around the alphabet; in other words, the letter `z` shifted by one returns the letter `a`

- [x] Input: `string = xyz, key = 2`
- [x] Output: `zab`

### **ORD/CHR String Manipulation with Modulo Wrapping**
```python
# O(n) Time | O(n) Space
def caesarCipherEncryptor(string, key):
	newLetters = []
	newKey = key % 26 # ensures that keys larger than 26 are reseted back to 0 (to preserve key range of 0-26)
	
	for letter in string:
		newLetters.append(getNewLetter(letter, newKey))
	return "".join(newLetters) # converts array of convertedLetters into a continuous string
	
def getNewLetter(letter, key):
	newLetterCode = ord(letter) + key
	if newLetterCode <= 122:
		return chr(newLetterCode)
	else:
		return chr(96 + newLetterCode % 122)
```
✅ **ORD/CHR AND MODULO:** 
- `ASCII: A = 96, Z = 122`
- _Loop each letter, convert letter into ASCII + KEY using ORD, then re-convert using CHR while handling for Z->A wrapping using MODULO 122_

---
## [🟨 Valid IP Addresses](https://www.algoexpert.io/questions/Valid%20IP%20Addresses)
>* You're given a string of length 12 or smaller, containing only digits. Write a function that returns all the possible IP addresses that can be created by inserting three `.`s in the string.
>* An IP address is a sequence of four positive integers that are separated by `.`s, where each individual integer is within the range `0 - 255`, inclusive.
>* An IP address isn't valid if any of the individual integers contains leading `0`s. 
>* For example, `"192.168.0.1"` is a valid IP address, but `"192.168.00.1"` and `"192.168.0.01"` aren't, because they contain `00` and `01`, respectively.
>* Another example of a valid IP address is `"99.1.1.10"`; conversely, `"991.1.1.0"` isn't valid, because `"991"` is greater than 255.
>* Your function should return the IP addresses in string format and in no particular order. If no valid IP addresses can be created from the string, your function should return an empty list.

- [x] Input: `string = "1921680"`
- [x] Output: `['1.9.216.80', '1.92.16.80', '1.92.168.0', '19.2.16.80', '19.2.168.0', '19.21.6.80', '19.21.68.0', '19.216.8.0', '192.1.6.80', '192.1.68.0', '192.16.8.0']`

### **Three Pointers**
```python
# O(1) Time | O(1) Space
# Time Complexity: Since an IP address is a 32 bit integer (e.g.: 0-255.0-255.0-255.0-255), you will only need to compute at most at a constant 2^32 numbers hence O(2^32) which can be reduced to O(1). The size of the input, n is independent and 2^32 is the absolute constant upper bound.
# Space Complexity: Since you can only generate a list that is at most 2^32 IP addresses in it (2^32 being the absolute constant upper bound), the space complexity is O(2^32) which can be reduced to O(1).

def validIPAddresses(string):
    ipAddressesFound = []
    # [192 . 1 . 68 . 0]
    # [    i   j    k  ] # i, j, k pointers represent the dots in the IP adddresses
    
    # For the 1st octet, you can only place the dot at positions 1 - 3. The pointer i gives a range to slice the string for the first IP octet.
    for i in range(1, min(len(string), 4)): # We start at range 1 so that we will never have an empty string
        currentIPAddressParts = ['', '', '', ''] 
        currentIPAddressParts[0] = string[:i] # slice the input string until pointer i for the 1st IP octet
        if not isValidPart(currentIPAddressParts[0]): # then check of this sliced string is a valid IP (0-255) with not leading zeroes (e.g.: 01)
            continue # skip if 1st IP octet is invalid
        
        # For thhe 2nd octet, we select a range (for j) after pointer i and spanning at most 3 digits (to honour the valid IP range of 0-255)
        for j in range(i + 1, i + min(len(string) - i, 4)): 
            currentIPAddressParts[1] = string[i:j] # slice the input string starting from index i to j for 2nd IP octet
            if not isValidPart(currentIPAddressParts[1]):
                continue # skip if 2nd IP octet is invalid
            
            # For the 3rd octet, we select a range (for k) after pointer j and spanning at most 3 digits (to honour the valid IP range of 0-255)
            for k in range(j + 1, j + min(len(string) - j, 4)):
                currentIPAddressParts[2] = string[j:k] # slice the input string starting from index j to k for 3rd IP octet
                currentIPAddressParts[3] = string[k:] # slice the rest of the input string starting index k onwards for 4th IP octet
                # if 3rd and 4th IP octets are valid, then we found the right combinations of IP dot pointers that make a valid IP address,
                if isValidPart(currentIPAddressParts[2]) and isValidPart(currentIPAddressParts[3]):
                    ipAddressesFound.append('.'.join(currentIPAddressParts)) # Add the answer and delimiting all IP address octets with '.'
    
    return ipAddressesFound
        
def isValidPart(string):
    stringAsInt = int(string) # Converting str to int helps remove any leading zeroes in string (e.g.: 00 -> 0 and 01 -> 1)
    if stringAsInt > 255: 
        return False
    return len(string) == len(str(stringAsInt)) # Checks if there are any leading 0's

# SOLUTION: 
```
✅ **THREE POINTERS**: _Set 3 pointers i, j, k for each IP dots, create 3 FOR loops for each pointer to slice string into 4 possible IP octets and check if the octets are valid (0-255) using a helper function. If all 4 octets are valid, then join the valid octets with '.' and append to answers array._
# <div id='linkedlists'/> 📝 **Linked Lists**

- Reverse a Linked List - https://leetcode.com/problems/reverse-linked-list/
- Detect Cycle in a Linked List - https://leetcode.com/problems/linked-list-cycle/
- ✅ Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/
- Merge K Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/
- Remove Nth Node From End Of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/
- Reorder List - https://leetcode.com/problems/reorder-list/
### [📋 **Back to Table of Contents**](#toc)
---

## [🟩 Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
>* You are given the heads of two sorted linked lists `list1` and `list2`.
>* Merge the two lists in a one **sorted** list. The list should be made by splicing together the nodes of the first two lists.
>* Return the **head of the merged linked list**.

- [x] Input: `list1 = [1,2,4], list2 = [1,3,4]`
- [x] Output: `[1,1,2,3,4,4]`

<img src="https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg" width="500"/>


### **Iteratively In-Place**
```python
class LinkedList: 
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n + m) Time where n is the length of the 1st linked list and m is the length of the 2nd linked list
# O(1) Space - we mutated the linked lists in place
def mergeLinkedLists(headOne, headTwo):
    p1 = headOne # current node of the 1st linked list
    p1Prev = None # previous node of the 1st linked list (iteration #1: this is a None)
    p2 = headTwo # current node of the 2nd linked list
    
    while p1 is not None and p2 is not None: # while both pointers are not None, we still have nodes to traverse 
        if p1.value < p2.value: # EASY CASE: we keep moving the prev and p1 pointers onto the next subsequent nodes
            p1Prev = p1 
            p1 = p1.next
        else: # HARD CASE (p2.value < p1.value): perform the 4 pointer mutation in order for this hard case
            if p1Prev is not None: # if p1Prev is not at the None end of the linked list
                p1Prev.next = p2 # continue setting the next of p1Prev to p2
            p1Prev = p2 # we need to get p1Prev = p2 before we overwrite the p2 below
            p2 = p2.next # we need to keep track of the next value of p2
            p1Prev.next = p1 # overwriting the former p2 with p1
    # we can get out of this while loop if either p1 is None or p2 is None, meaning we have traversed to the end of linked list
    
    # EDGE CASE
    if p1 is None: # if we run out of nodes to traverse in the 1st linked list and we still have values to append from the 2nd linked list
        p1Prev.next = p2 # in this case, p1Prev is the final node of the 1st linked list and its next value should immediately connect to the 2nd linked list at p2
    return headOne if headOne.value < headTwo.value else headTwo # return the correct head of the linkedlist with the smaller value
```
✅ **ITERATIVELY IN-PLACE:** 
- _Create 3 pointers (p1Prev, p1, p2)_
- _If NodeL1 < NodeL2, keep moving prev and p1 to the next nodes._
- _If NodeL2 < NodeL1, set p1Prev.next = p2 and p1Prev = p2 to keep track of value, move p2 = p2.next and then we can finally set p1Prev.next = p1_
- _Insert each node from one list into the other_

---
# <div id='graphs'/> 📈 **Graphs**

- Clone Graph - https://leetcode.com/problems/clone-graph/
- Course Schedule - https://leetcode.com/problems/course-schedule/
- Pacific Atlantic Water Flow - https://leetcode.com/problems/pacific-atlantic-water-flow/
- ✅ Number of Islands - https://leetcode.com/problems/number-of-islands/
- Longest Consecutive Sequence - https://leetcode.com/problems/longest-consecutive-sequence/
- Alien Dictionary (Leetcode Premium) - https://leetcode.com/problems/alien-dictionary/
- Graph Valid Tree (Leetcode Premium) - https://leetcode.com/problems/graph-valid-tree/
- Number of Connected Components in an Undirected Graph (Leetcode Premium) - https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
### [📋 **Back to Table of Contents**](#toc)

---
## [🟨 Number of Islands](https://leetcode.com/problems/number-of-islands/)
>* Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return the number of islands.
>* An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

```yaml
# Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
# Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```
### **Depth First Search**
```python
def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if not grid: return 0
    r, c = len(grid), len(grid[0])
    visited = [[False for _ in range(c)] for _ in range(r)]

    def dfs(i, j):
        if i < 0 or i >= r or j < 0 or j >= c or grid[i][j] == '0' or visited[i][j]:
            return
        visited[i][j] = True
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    count = 0
    for i in range(r):
        for j in range(c):
            if not visited[i][j] and grid[i][j] == '1':
                dfs(i, j)
                count += 1
    return count
```
✅ **DEPTH FIRST SEARCH (ITERATIVE)**: _for each cell, if cell is 1 and unvisited, run dfs, increment count and mark each contiguous 1's as visited in auxiliary matrix_

---
## [🟨 Max Area of Island](https://leetcode.com/problems/max-area-of-island/)
>* You are given an `m x n` binary matrix `grid`. An island is a group of `1`'s (representing land) connected **4-directionally** (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
>* The **area** of an island is the number of cells with a value `1` in the island.
>* Return the maximum **area** of an island in `grid`. If there is no island, return `0`.

<img src="https://assets.leetcode.com/uploads/2021/05/01/maxarea1-grid.jpg" width="500"  /><br/>

```yaml
Input: grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
```
### [**Depth First Search (Iterative)**](https://leetcode.com/problems/max-area-of-island/solution/)
```python
def maxAreaOfIsland(self, grid):
    seen = set()
    ans = 0
    for r0, row in enumerate(grid):
        for c0, val in enumerate(row):
            if val and (r0, c0) not in seen:
                shape = 0
                stack = [(r0, c0)]
                seen.add((r0, c0))
                while stack:
                    r, c = stack.pop()
                    shape += 1
                    for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                        if (0 <= nr < len(grid) and 0 <= nc < len(grid[0])
                                and grid[nr][nc] and (nr, nc) not in seen):
                            stack.append((nr, nc))
                            seen.add((nr, nc))
                ans = max(ans, shape)
    return ans
```
✅ **DEPTH FIRST SEARCH (ITERATIVE)**: _for each cell, if cell is 1 and unvisited, run dfs, increment count and mark each contiguous 1's as visited in auxiliary matrix_

---
## [🟨 River Sizes](https://www.algoexpert.io/questions/River%20Sizes)
>* You're given a two-dimensional array (a matrix) of potentially unequal height and width containing only `0`'s and `1`'s. Each `0` represents land, and each `1` represents part of a river. A river consists of any number of `1`'s that are either horizontally or vertically adjacent (but not diagonally adjacent). The number of adjacent 1s forming a river determine its size.
>* Note that a river can twist. In other words, it doesn't have to be a straight vertical line or
a straight horizontal line; it can be L-shaped, for example.
>* Write a function that returns an array of the sizes of all rivers represented if the input
matrix. The sizes don't need to be in any particular order.

```yaml
Input: matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
  ]
Output: [1, 2, 2, 2, 5] # The numbers could be ordered differently
Explanation: matrix = [ # The rivers can be clearly seen here:
    [1,  ,  , 1,  ],
    [1,  , 1,  ,  ],
    [ ,  , 1,  , 1],
    [1,  , 1,  , 1],
    [1,  , 1, 1,  ]
  ]
```
### **Depth First Search (Iterative)**
```python
# O(n) Time - we only need to traverse all of the elements in the matrix once
# O(n) Space - we are using an auxiliary matrix of size n to keep track of visited nodes
# n - the number of elements in the matrix
def riverSizes(matrix):
    sizes = [] # answer array
    # Auxiliary matrix to keep track of nodes that already been visited
    visited = [[False for value in row] for row in matrix] 
    for i in range(len(matrix)): # for every row,
        for j in range(len(matrix[i])): # for every column,
            if visited[i][j]: # if node is already marked as visited in our auxiliary matrix, we skip it
                continue
            traverseNode(i, j, matrix, visited, sizes) # otherwise if unvisited, traverse node at position (i, j)
    return sizes

def traverseNode(i, j, matrix, visited, sizes): 
    currentRiverSize = 0 # initializing a potentially new river
    # ==============================
    # Depth First Search (Iterative)
    # ==============================
    nodesToExplore = [[i, j]] # stack of nodes to explore (Iterative DFS implementation)

    # STEP 1: EXPLORE NODES, USE STACK AND ITERATE DFS ON POPPED NODES THAT ARE RIVERS (1's)
    while len(nodesToExplore): # while we still have nodes to explore,
        currentNode = nodesToExplore.pop() # pop out the final value of the nodesToExplore array
        i, j = currentNode[0], currentNode[1]

        # STEP 2: SKIP IF ALREADY VISITED OR LAND
        if visited[i][j]: # if node has already been visited, we skip it
            continue
        visited[i][j] = True # otherwise if not visited, mark the current node being traversed as visited to keep track
        if matrix[i][j] == 0: # if it is a piece of land, we skip it
            continue

        # STEP 3: OTHERWISE, WE FOUND A RIVER!
        currentRiverSize += 1

        # STEP 4: NOW, CHECK ADJACENT NEIGHBOURS AND ITERATE DFS ON NEWLY APPENDED NEIGHBOUR NODES THAT ARE RIVERS
        unvisitedNeighbours = getUnvisitedNeighbours(i, j, matrix, visited) # get unvisited neighbours around our current node and add it to nodesToExplore stack
        for neighbour in unvisitedNeighbours:
            nodesToExplore.append(neighbour) # append new unvisited neighbours to explore in the stack

    # STEP 5: AFTER A FULL DFS ON A RIVER, APPEND ANSWER TO OUR RIVER SIZES ARRAY
    if currentRiverSize > 0: # if we have an actual river, we append to our sizes answer array
        sizes.append(currentRiverSize)
    
def getUnvisitedNeighbours(i, j, matrix, visited):
    unvisitedNeighbours = []
    # Check if the 4 surrounding adjacent neighbours are valid neighbours (unvisited and within the matrix boundary)
    # ==========================================
    # ROWS CHECK FOR NEIGHBOURS ABOVE AND BELOW
    # ==========================================
    if i > 0 and not visited[i - 1][j]: # if we are not in the top row and not visited the neighbour above,
        unvisitedNeighbours.append([i - 1, j]) # append the node (with indices) of the neighbour above us
    if i < len(matrix) - 1 and not visited[i + 1][j]: # if we are not in the bottomw row and not visited neighbour below,
        unvisitedNeighbours.append([i + 1, j]) # append the node (with indices) of the neighbour below us
    # ============================================
    # COLUMNS CHECK FOR NEIGHBOURS LEFT AND RIGHT
    # ============================================
    if j > 0 and not visited[i][j - 1]: # if we are not in the left-most column and not visited the neighbour to the left,
        unvisitedNeighbours.append([i, j - 1]) # append the node (with indices) of the left neighbour
    if j < len(matrix[0]) - 1 and not visited[i][j + 1]: # if we are not in the right-most column and not visited the neighbour to the right, 
        unvisitedNeighbours.append([i, j + 1]) # append the node (with indices) of the right neighbour
    return unvisitedNeighbours # finally, return the array containing nodes of all unvisited adjacent neighbours
```
✅ **DEPTH FIRST SEARCH (ITERATIVE)**: _for each cell, if cell is 1 and unvisited, run dfs, increment count and mark each contiguous 1's as visited in auxiliary matrix_

---
# <div id='trees'/> 🎄 **Trees**

- Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/
- Same Tree - https://leetcode.com/problems/same-tree/
- Invert/Flip Binary Tree - https://leetcode.com/problems/invert-binary-tree/
- Binary Tree Maximum Path Sum - https://leetcode.com/problems/binary-tree-maximum-path-sum/
- Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/
- Serialize and Deserialize Binary Tree - https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
- Subtree of Another Tree - https://leetcode.com/problems/subtree-of-another-tree/
- Construct Binary Tree from Preorder and Inorder Traversal - https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
- Validate Binary Search Tree - https://leetcode.com/problems/validate-binary-search-tree/
- Kth Smallest Element in a BST - https://leetcode.com/problems/kth-smallest-element-in-a-bst/
- Lowest Common Ancestor of BST - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
- Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/
- Add and Search Word - https://leetcode.com/problems/add-and-search-word-data-structure-design/
- Word Search II - https://leetcode.com/problems/word-search-ii/
### [📋 **Back to Table of Contents**](#toc)

---
## [🟩 Branch Sums](https://www.algoexpert.io/questions/Branch%20Sums)
>* Write a function that takes in a Binary Tree and returns a list of its branch sums
ordered from leftmost branch sum to rightmost branch sum.
>* A branch sum is the sum of all values in a Binary Tree branch. A Binary Tree branch is a
path of nodes in a tree that starts at the root node and ends at any leaf node.
>* Each `BinaryTree` node has an integer `value`, a `left` child node, and a `right`
child node. Children nodes can either be BinaryTree nodes themselves or `None`/`null`.

- [x] Input: 
```python
           1
        /    \
      2        3
     /  \     /  \
   4     5   6    7 
  / \    /
 8   9  10
```
- [x] Output: 
```python
Output: [15, 16, 18, 10, 11]
15 == 1 + 2 + 4 + 8
16 == 1 + 2 + 4 + 9
18 == 1 + 2 + 5 + 10
10 == 1 + 3 + 6
11 == 1 + 3 + 7
```

### **Recursion**
```python

# O(n) Time | O(n) Space
# Time: traversing all of each node at least once with constant time operations
# Space: returning a list of branch sums with the length of the number of leaf nodes in the input BT
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
            
def branchSums(root):
    sums = []
    # Initialising parameters for the root node where initially there are no runningSums 
    calculateBranchSums(root, 0, sums)

def calculateBranchSums(node, runningSum, sums):
    if node is None: 
        return
    # Recursively compute sum all the way to leaf node
    newRunningSum = runningSum + node.value
    # If node is a leaf node (reached the end of the branch), add the complete running sum to the answer
    if node.left is None and node.right is None: 
        sums.append(newRunningSum)
        return
    # Recursively calls the helper function to continue traversing and summing up nodes on both branches
    calculateBranchSums(node.left, newRunningSum, sums)
    calculateBranchSums(node.right, newRunningSum, sums)
```
✅ **RECURSION:** _Recursively call the calculateBranchSums helper function to traverse down the branch (both left and right), summing up nodes and append the totalSum when a leaf node is reached (node.left and node.right are None)_

---
# <div id='heaps'/> 🏔 **Heaps**

- Merge K Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/
- Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/
- Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/
### [📋 **Back to Table of Contents**](#toc)
---
# <div id='intervals'/> ⏱ **Intervals**

- Insert Interval - https://leetcode.com/problems/insert-interval/
- ✅ Merge Intervals - https://leetcode.com/problems/merge-intervals/
- Non-overlapping Intervals - https://leetcode.com/problems/non-overlapping-intervals/
- Meeting Rooms (Leetcode Premium) - https://leetcode.com/problems/meeting-rooms/
- Meeting Rooms II (Leetcode Premium) - https://leetcode.com/problems/meeting-rooms-ii/
### [📋 **Back to Table of Contents**](#toc)
---
## [🟨 Merge Intervals](https://leetcode.com/problems/merge-intervals/)
> Given an array of intervals where `intervals[i] = [starti, endi]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

- [x] Input: `intervals = [[1,3],[2,6],[8,10],[15,18]]`
- [x] Output: `[[1,6],[8,10],[15,18]]`
- [x] Explanation: `Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].`

### **Sort, Check and Mutate**
```python
# O(nlogn) Time | O(n) Space
def mergeOverlappingIntervals(intervals):
    # Sorting the array of intervals based on the 1st elements of arrays
    sortedIntervals = sorted(intervals, key=lambda x: x[0])
    
    mergedIntervals = []
    currentInterval = sortedIntervals[0] 
    mergedIntervals.append(currentInterval) # At least 1 interval is required for the algorithm to work
    
    for nextInterval in sortedIntervals:
        # Decomposing currentInterval into 2 variables (e.g.: currentInterval = [1, 2] gives _ = 1 and currentIntervalEnd = 2)
        _, currentIntervalEnd = currentInterval 
        # Decomposing nextInterval into 2 variables (e.g.: nextInterval = [3, 5] gives nextIntervalStart = 3 and nextIntervalEnd = 5)
        nextIntervalStart, nextIntervalEnd = nextInterval 
        
        # This check determines if two intervals are overlapping by comparing the intervalEnd value of the current interval is bigger or equal than the intervalStart value of the next interval
        if currentIntervalEnd >= nextIntervalStart:
            currentInterval[1] = max(currentIntervalEnd, nextIntervalEnd) # mutate the currentIntervalEnd to be the highest number between the intervalEnd values of the currentInterval and nextInterval
        else: 
            currentInterval = nextInterval # if there are no overlapping, then immediately append the interval to answer
            mergedIntervals.append(currentInterval)
            
    return mergedIntervals
```
✅ **SORT, CHECK AND MUTATE:** _Sort intervals by start values, compare end value and start value of adjacent intervals to check for overlap, mutate end value of answer interval to encapsulate merges, iterate checks for all intervals_
### **Problem similar to:**
- 252 Meeting Rooms
- 253 Meetings Rooms II
- 435 Non-overlapping Intervals
---
# <div id='dp'/> 📱 **Dynamic Programming**

- Climbing Stairs - https://leetcode.com/problems/climbing-stairs/
- Coin Change - https://leetcode.com/problems/coin-change/
- Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/
- Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/
- Word Break Problem - https://leetcode.com/problems/word-break/
- Combination Sum - https://leetcode.com/problems/combination-sum-iv/
- House Robber - https://leetcode.com/problems/house-robber/
- House Robber II - https://leetcode.com/problems/house-robber-ii/
- Decode Ways - https://leetcode.com/problems/decode-ways/
- Unique Paths - https://leetcode.com/problems/unique-paths/
- Jump Game - https://leetcode.com/problems/jump-game/
### [📋 **Back to Table of Contents**](#toc)

---
## [🟥 Longest Common Subsequence](https://www.algoexpert.io/questions/Longest%20Common%20Subsequence)
>* Write a function that takes in two strings and returns their longest common subsequence.
>* A subsequence of a string is a set of characters that aren't necessarily adjacent in the string but that are in the same order as they appear in the string. For instance, the characters `["a", "c"', "d"]` form a subsequence of the string `"abcd"`, and so do the characters `["b", "d"]`. 
>* Note that a single character in a string and the string itself are both valid subsequences of the string.
>* You can assume that there will only be one longest common subsequence.

- [x] Input: `str1 = "ZXVVYZW", str2 = "XKYKZPW"`
- [x] Output: `["X", "Y", "Z", "W"]`

### [**Recursion**](https://leetcode.com/problems/longest-common-subsequence/discuss/436719/Python-very-detailed-solution-with-explanation-and-walkthrough-step-by-step.)
```python
"""
                          lcs("AXYT", "AYZX")
                           /              \
             lcs("AXY", "AYZX")            lcs("AXYT", "AYZ")
             /        \                      /              \ 
    lcs("AX", "AYZX") lcs("AXY", "AYZ")   lcs("AXY", "AYZ") lcs("AXYT", "AY")
"""
def longestCommonSubsequence(self, s1: str, s2: str) -> int:
    return self.helper(s1, s2, 0, 0)
    
def helper(self, s1, s2, i, j):
    if i == len(s1) or j == len(s2):
        return 0
    if s1[i] == s2[j]:
        return 1 + self.helper(s1, s2, i + 1, j + 1)
    else:
```
✅ **RECURSION:** _if first chars are equal find lcs of remaining of each, else max of: lcs of first and remain of 2nd and lcs of 2nd remain of first, cache result; nested forloop to compute the cache without recursion_ 
### [**Bottom up dynamic programming**](https://leetcode.com/problems/longest-common-subsequence/discuss/436719/Python-very-detailed-solution-with-explanation-and-walkthrough-step-by-step.)
```python
# O(mn * min(m,n)) Time | O(mn * min(m,n)) Space
# Use a nested loop that visits the array systematically. The only thing we have to worry about is that when we fill in a cell L[i,j], we need to already know the values it depends on, namely in this case L[i+1,j], L[i,j+1], and L[i+1,j+1]. For this reason we'll traverse the array backwards, from the last row working up to the first and from the last column working up to the first.
def longestCommonSubsequence(s1: str, s2: str) -> int:
    m = len(s1)
    n = len(s2)
    LCS = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for row in range(1, m + 1):
        for col in range(1, n + 1):
            if s1[row - 1] == s2[col - 1]:
                LCS[row][col] = 1 + LCS[row - 1][col - 1]
            else:
                LCS[row][col] = max(LCS[row][col - 1], LCS[row - 1][col])

    return LCS[m][n] # LCS[-1][-1] to return List[str] instead
```
✅ **BOTTOM UP DP:** _TBD_

---
# <div id='binaries'/> ⚡️ **Binaries**

- Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/
- Number of 1 Bits - https://leetcode.com/problems/number-of-1-bits/
- Counting Bits - https://leetcode.com/problems/counting-bits/
- Missing Number - https://leetcode.com/problems/missing-number/
- Reverse Bits - https://leetcode.com/problems/reverse-bits/
### [📋 **Back to Table of Contents**](#toc)
---