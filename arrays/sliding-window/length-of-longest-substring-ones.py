def lengthOfLongestSubstring(array, k):
  windowStart, maxLength, maxOneCount = 0, 0, 0

  for windowEnd in range(len(array)):
    if array[windowEnd] == 1:
      maxOneCount += 1

    if (windowEnd - windowStart + 1 - maxOneCount) > k:
      if array[windowStart] == 1:
        maxOneCount -= 1
      windowStart += 1

    maxLength = max(maxLength, windowEnd - windowStart + 1)
  return maxLength

def main():
    array = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
    k = 2
    print(lengthOfLongestSubstring(array, k))
    
main()