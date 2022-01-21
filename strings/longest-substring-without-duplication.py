# O(n) Time | O(min(n, a)) Space
def longestSubstringWithoutDuplication(string): 
    lastSeen = {}
    longest = [0, 1]
    startIdx = 0
    
    for idx, char in enumerate(string):
        if char in lastSeen: 
            startIdx = max(startIdx, lastSeen[char] + 1)
        if longest[1] - longest[0] < (idx + 1 - startIdx):
            longest = [startIdx, idx + 1]
        lastSeen[char] = idx
    return string[longest[0] : longest[1]] 