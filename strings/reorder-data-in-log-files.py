def reorder(logs):
  digits, letters, result = [], [], [] 
  for log in logs:
    if log.split()[1].isdigit(): 
      digits.append(log)
    else: 
      letters.append(log) 
  letters.sort(key = lambda x : x.split()[0]) # sort by 1st element (identifier)
  letters.sort(key = lambda x : x.split()[1:]) # sort by remaining elements (content)
  result = letters + digits
  return result 

import unittest
class UnitTest(unittest.TestCase): 
  def testCase(self): 
    logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    expected = ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
    actual = reorder(logs) 
    self.assertEqual(actual, expected)

if __name__ == '__main__':
  unittest.main(argv=[''], verbosity=2, exit=False)