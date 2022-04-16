# O(N + M) Time - where ‘N’ and ‘M’ are the number of characters in the input string and the pattern, respectively.
# O(M) Space - since, in the worst case, the whole pattern can have distinct characters that will go into the HashMap.
def smallestWindowSubstring(string, pattern): 
    windowStart, substringStart, matched = 0, 0, 0
    minLength = len(string) + 1
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
        if rightChar in charFrequency: 
            charFrequency[rightChar] -= 1
            
            # 4: We will keep a running count of every matching instance of a character.
            if charFrequency[rightChar] >= 0:
                matched += 1

    # 5: Whenever we have matched all the characters, we will try to shrink the window from the beginning, 
    # keeping track of the smallest substring that has all the matching characters.
    # We will stop the shrinking process as soon as we remove a matched character from the sliding window. 
    while matched == len(pattern): 
        if minLength > windowEnd - windowStart + 1: 
            minLength = windowEnd - windowStart + 1
            substringStart = windowStart
        
        leftChar = string[windowStart]
        windowStart += 1
        if leftChar in charFrequency: 
            # 6: Note that we could have redundant matching characters, therefore we'll decrement the
            # matched count only when a useful occurrence of a matched character is going out of the window
            # One thing to note here is that we could have redundant matching characters, 
            # e.g., we might have two ‘a’ in the sliding window when we only need one ‘a’. 
            # In that case, when we encounter the first ‘a’, we will simply shrink the window without decrementing the matched count. 
            # We will decrement the matched count when the second ‘a’ goes out of the window.
            if charFrequency[leftChar] == 0: 
                matched -= 1
            charFrequency[leftChar] += 1
            
    if minLength > len(string): 
        return "" 
    return string[substringStart : substringStart + minLength]
            
def main():
    print(smallestWindowSubstring("aabdec", "abc"))
    print(smallestWindowSubstring("aabdec", "abac"))
    print(smallestWindowSubstring("abdbca", "abc"))
    print(smallestWindowSubstring("adcad", "abc"))

main()