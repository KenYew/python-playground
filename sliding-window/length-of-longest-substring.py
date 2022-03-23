def lengthOfLongestSubstring(string, k):
    windowStart, maxLength, maxRepeatingLetterCount = 0, 0, 0
    frequencyMap = {}
    
    for windowEnd in range(len(string)): 
        rightChar = string[windowEnd]
        if rightChar not in frequencyMap:
            frequencyMap[rightChar] = 0
        frequencyMap[rightChar] += 1
        maxRepeatingLetterCount = max(maxRepeatingLetterCount, frequencyMap[rightChar])
        
        if (windowEnd - windowStart + 1 - maxRepeatingLetterCount) > k:
            leftChar = string[windowStart]
            frequencyMap[leftChar] -= 1
            windowStart += 1
        maxLength = max(maxLength, windowEnd - windowStart + 1)
    return maxLength