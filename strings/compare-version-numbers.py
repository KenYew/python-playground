def compareVersion(version1, version2): 
  v1 = version1.split('.') # e.g.: "1.01" -> ["1", "0", "1"]
  v2 = version2.split('.') # e.g.: "1.001" -> ["1", "0", "0", "1"]

  for idx in range(max(len(v1), len(v2))): 
    n1 = 0 if idx >= len(v1) else int(v1[idx])
    n2 = 0 if idx >= len(v2) else int(v2[idx])

    if n1 < n2: 
      return -1 
    elif n1 > n2: 
      return 1
      
  return 0

import unittest
class UnitTest(unittest.TestCase): 
  def testCase1(self): 
    version1 = "1.01"
    version2 = "1.001"
    actual = compareVersion(version1, version2)
    expected = 0
    self.assertEqual(actual, expected)

  def testCase2(self): 
    version1 = "1.0"
    version2 = "1.0.0"
    actual = compareVersion(version1, version2)
    expected = 0
    self.assertEqual(actual, expected)

  def testCase3(self): 
    version1 = "0.1"
    version2 = "1.1"
    actual = compareVersion(version1, version2)
    expected = -1
    self.assertEqual(actual, expected)

  def testCase4(self): 
    version1 = "2.1"
    version2 = "1.1"
    actual = compareVersion(version1, version2)
    expected = 1
    self.assertEqual(actual, expected)

if __name__ == '__main__': 
  unittest.main(argv=[''], verbosity=2, exit=False)