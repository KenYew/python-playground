import re 
def mostCommonWord(string, banned): 
  words = re.findall(r'\w+', string.lower())
  legalWords = []
  for word in words: 
    if word not in set(banned): 
      legalWords.append(word)
  
  wordFrequency = {}
  for word in legalWords:
    if word not in wordFrequency: 
      wordFrequency[word] = 0
    wordFrequency[word] += 1
  return max(wordFrequency, key=wordFrequency.get)

import unittest
class UnitTest(unittest.TestCase): 
  def testCase(self): 
    string = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    actual = mostCommonWord(string, banned)
    expected = "ball"
    self.assertEqual(actual, expected) 

if __name__ == '__main__':
  unittest.main(argv=[''], verbosity=2, exit=False)