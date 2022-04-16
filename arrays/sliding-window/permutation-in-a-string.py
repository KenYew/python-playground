# O(N + M) Time - where ‘N’ and ‘M’ are the number of characters in the input string and the pattern, respectively.
# O(M) Space - since, in the worst case, the whole pattern can have distinct characters that will go into the HashMap.
def findPermutation(string, pattern): 
    windowStart, matched = 0, 0
    charFrequency = {}
    
    # 1: Create a HashMap to calculate the frequencies of all characters in the pattern.
    for char in pattern:
        if char not in charFrequency: 
            charFrequency[char] = 0 
        charFrequency[char] += 1
        
    # 2: Iterate through the string, adding one character at a time in the sliding window.
    for windowEnd in range(len(string)): 
        rightChar = string[windowEnd]
        
        # 3: If the character being added matches a character in the HashMap, decrement its frequency in the map. 
        # If the character frequency becomes zero, we got a complete match.
        if rightChar in charFrequency: 
            charFrequency[rightChar] -= 1
            if charFrequency[rightChar] == 0:
                matched += 1
        
        # 4: If at any time, the number of characters matched is equal to the number of distinct characters in the pattern
        # (i.e., total characters in the HashMap), we have gotten our required permutation.
        if matched == len(charFrequency): 
            return True
        
        # 5: If the window size is greater than the length of the pattern, shrink the window to make it equal to the pattern’s size. 
        if windowEnd >= len(pattern) - 1: 
            leftChar = string[windowStart]
            windowStart += 1
            # 6: At the same time, if the character going out was part of the pattern, put it back in the frequency HashMap.
            if leftChar in charFrequency: 
                if charFrequency[leftChar] == 0:
                    matched -= 1
                charFrequency[leftChar] += 1
    return False

def main():
    print('Permutation exist: ' + str(findPermutation("oidbcaf", "abc")))
    print('Permutation exist: ' + str(findPermutation("odicf", "dc")))
    print('Permutation exist: ' + str(findPermutation("bcdxabcdy", "bcdyabcdx")))
    print('Permutation exist: ' + str(findPermutation("aaacb", "abc")))


main()