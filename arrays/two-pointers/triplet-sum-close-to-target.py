# O(n^2) Time - O(nlogn) + O(n^2) asymptotically equivalent to O(n^2)
# O(n) Space
def threeSumClosest(array, targetSum): 
  array.sort()
  smallestDifference = float("inf")
  for idx in range(len(array) - 2): 
    if idx > 0 and array[idx - 1] == array[idx]: 
      continue
    left, right = idx + 1, len(array) - 1
    while left < right: 
      targetDifference = targetSum - array[idx] - array[left] - array[right]
      if targetDifference == 0: 
        return targetSum

      if abs(targetDifference) < abs(smallestDifference) or (abs(targetDifference) == abs(smallestDifference) and targetDifference > smallestDifference):
        smallestDifference = targetDifference
      
      if targetDifference > 0: 
        left += 1
      else: 
        right -= 1

  return targetSum - smallestDifference

def threeSumClosest(array, target): 
  if len(array) < 3: 
    return
  array.sort() 
  closestSum = array[0] + array[1] + array[2]
  for idx in range(len(array) - 2): 
    if idx > 0 and array[idx - 1] == array[idx]: 
      continue
    left = idx + 1
    right = len(array) - 1 
    while left < right: 
      currentSum = array[idx] + array[left] + array[right]
      if currentSum == target:
        return currentSum
      elif currentSum < target: 
        left += 1
      elif currentSum > target:
        right -= 1
      if abs(currentSum - target) < abs(closestSum - target):
        closestSum = currentSum
  return closestSum

import unittest
class UnitTest(unittest.TestCase): 
  def testCase1(self):
    array = [-2, 0, 1, 2]
    target = 2
    actual = threeSumClosest(array, target)
    expected = 1
    self.assertEqual(actual, expected)
    
  def testCase2(self):
    array = [-3, -1, 1, 2]
    target = 1
    actual = threeSumClosest(array, target)
    expected = 0
    self.assertEqual(actual, expected)
    
  def testCase3(self):
    array = [1, 0, 1, 1]
    target = 100
    actual = threeSumClosest(array, target)
    expected = 3
    self.assertEqual(actual, expected)
    
if __name__ == '__main__':
  unittest.main(verbosity=2, exit=False)