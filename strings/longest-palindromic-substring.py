def longestPalindromicSubstring(string): 
    longestString = ""
    for i in range(len(string)): 
        for j in range(i, len(string)): 
            substring = string[i : j + 1]
            if len(substring) > len(longestString) and isPalindrome(substring):
                longestString = substring
    return longestString

def isPalindrome(string):
    if string == string[::-1]:
        return True
    return False