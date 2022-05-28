from collections import deque
class MinMaxQueue: 
  def __init__(self): 
    self.minMaxQueue = deque()
    self.queue = deque()

  def peek(self):
    return self.queue[len(self.queue) - 1]

  def pop(self):
    self.minMaxQueue.pop()
    return self.queue.pop()

  def popleft(self):
    self.minMaxQueue.popleft()
    return self.queue.popleft()

  def push(self, number): 
    newMinMax = {
        "min": number, 
        "max": number
    }
    if len(self.minMaxQueue): 
      lastMinMax = self.minMaxQueue[len(self.minMaxQueue) - 1]
      newMinMax["min"] = min(lastMinMax["min"], number)
      newMinMax["max"] = max(lastMinMax["max"], number)
    self.minMaxQueue.append(newMinMax)
    self.queue.append(number)

  def pushleft(self, number): 
    newMinMax = {
        "min": number, 
        "max": number
    }
    if len(self.minMaxQueue): 
      lastMinMax = self.minMaxQueue[len(self.minMaxQueue) - 1]
      newMinMax["min"] = min(lastMinMax["min"], number)
      newMinMax["max"] = max(lastMinMax["max"], number)
    self.minMaxQueue.append(newMinMax)
    self.queue.append(number)
  
  def getMin(self):
    return self.minMaxQueue[len(self.minMaxQueue) - 1]["min"]

  def getMax(self):
    return self.minMaxQueue[len(self.minMaxQueue) - 1]["max"]

  def view(self): 
    return list(self.queue)

import unittest
class UnitTest(unittest.TestCase): 
  def testCase1(self): 
    queue = MinMaxQueue()
    queue.push(3)
    queue.pushleft(1)
    queue.pushleft(-2)
    queue.push(-1)
    queue.pushleft(4)
    queue.pop()
    queue.peek()
    queue.getMin()
    queue.getMax()
    queue.view()
    actual = queue.view()
    expected = [4, -2, 1, 3]
    self.assertEqual(actual, expected)

if __name__ == '__main__':
  unittest.main(argv=[''], verbosity=2, exit=False)