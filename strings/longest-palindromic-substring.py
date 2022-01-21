# O(n^3) Time | O(n) Space
def longestPalindromicSubstring(string): # O(n^2) Time
    longestString = ""
    for i in range(len(string)): 
        for j in range(i, len(string)): 
            substring = string[i : j + 1]
            if len(substring) > len(longestString) and isPalindrome(substring):
                longestString = substring
    return longestString

def isPalindrome(string): # O(n) Time
    left, right = 0, len(string) - 1
    while left < right: 
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True

def isPalindrome(string): # Pythonic
    if string == string[::-1]:
        return True
    return False

# O(n^2) Time | O(n) Space
def longestPalindromicSubstring(string): # O(n) Time
    # 1: Initialising an array of startIdx and endIdx of the current longest palindromic substring
    # [0, 1] enables string[0:1] string slicing to only contain a single letter which is the smallest possible palindromic substring.
    currentLongest = [0, 1] # NOTE: In Python, the endIdx letter of sliced string is not INCLUSIVE.
    
    # 2: Traversing the idx pointer from 1 to len(string). We start at 1 because the first letter is always palindromic
    for idx in range(1, len(string)): 
        # 3: Get odd-length palindrome where the center is the letter between previousLetter and nextLetter
        # e.g.: cab(a)bac
        odd = getLongestPalindromeFrom(string, idx - 1, idx + 1)
        
        # 4: Get even-length palindrome where the center is in between previousLetter and currentLetter
        # e.g.: cab|bac
        even = getLongestPalindromeFrom(string, idx - 1, idx)
        
        # 5: Get the longest palindromic substring of current iteration based on the length between x[1] and x[0]
        # e.g.: odd = [0, 3] even = [0, 6], oddLength = 3 - 0 = 3, evenLength = 6 - 0 = 6, hence: longest = 6
        longest = max(odd, even, key = lambda x: x[1] - x[0])
        
        # 6: Get the longest palindromic substring of all iterations based on the length between x[1] and x[0]
        currentLongest = max(longest, currentLongest, key = lambda x: x[1] - x[0])
    
    # 7: Return the sliced input string using the startIdx and endIdx of currentLongest
    return string[currentLongest[0] : currentLongest[1] + 1] # NOTE: In Python, the endIdx letter of sliced string is not INCLUSIVE so we add 1 to include the final letter at endIdx.

def getLongestPalindromeFrom(string, left, right): # O(n) Time 
    # 1: Starting from the middle of the palindrome, we spread out the left and right pointers until the ends during traversal
    while left >= 0 and right < len(string): 
        # 2: If both pointers are on different letters, this is not a contiguous palindrome so break at this point
        if string[left] != string[right]: 
            break
        # 3: Else both pointers are on the same letters, keep spreading the pointers outwards until the start and end of palindromic substring
        left -= 1
        right += 1
    # 4: Return the startIdx and endIdx of the palindromic substring
    return [left + 1, right - 1] 
    # NOTE: When left and right pointers have moved all the way outwards to the start and end of the palindromic substring and they finally break the while loop condition of left >= 0 and right < len(string), the left and right pointers would have been positioned one step too far to the left and right at left - 1 and right + 1 in order to break the while loop condition. So we return [left + 1, right - 1] to account for this offset.