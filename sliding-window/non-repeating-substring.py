def nonRepeatingSubstring(string): 
    windowStart, maxLength = 0, float("-inf")
    charIndexMap = {}
    
    for windowEnd in range(len(string)): 
        rightChar = string[windowEnd]

        if rightChar in charIndexMap:
            windowStart = max(windowStart, charIndexMap[rightChar] + 1)
            
        charIndexMap[rightChar] = windowEnd
        maxLength = max(maxLength, windowEnd - windowStart + 1)
        
    return maxLength

def main():
    string = "abccde"
    print(nonRepeatingSubstring(string))
    
main()