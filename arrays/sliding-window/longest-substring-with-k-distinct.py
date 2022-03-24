def longestSubstrinWithKDistinct(k, string):
    windowStart, maxLength = 0, 0
    charFrequency = {}

    for windowEnd in range(len(string)): 
        rightChar = string[windowEnd]
        if rightChar not in charFrequency: 
            charFrequency[rightChar] = 0
        charFrequency[rightChar] += 1
        
        while len(charFrequency) > k: 
            leftChar = string[windowStart]
            charFrequency[leftChar] -= 1
            if charFrequency[leftChar] == 0:
                del charFrequency[leftChar]
            windowStart += 1
            
        maxLength = max(maxLength, windowEnd - windowStart + 1)
    return maxLength

def main(): 
    k = 2
    string = "araaci"
    print(longestSubstrinWithKDistinct(k, string))
    
main()