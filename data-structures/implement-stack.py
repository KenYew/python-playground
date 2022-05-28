class MinMaxStack:
  def __init__(self):
    self.minMaxStack = [] 
    self.stack = [] 
	
  def peek(self):
    return self.stack[len(self.stack) - 1] 

  def pop(self):
    self.minMaxStack.pop() 
    return self.stack.pop()

  def push(self, number):
    newMinMax = {"min": number, "max": number}
    if len(self.minMaxStack): 
      lastMinMax = self.minMaxStack[len(self.minMaxStack) - 1]
      newMinMax["min"] = min(lastMinMax["min"], number)
      newMinMax["max"] = max(lastMinMax["max"], number)
    self.minMaxStack.append(newMinMax)
    self.stack.append(number)
	
  def getMin(self):
      return self.minMaxStack[len(self.minMaxStack) - 1]["min"] 

  def getMax(self):
      return self.minMaxStack[len(self.minMaxStack) - 1]["max"] 
      
  def view(self): 
    return self.stack

import unittest
class UnitTest(unittest.TestCase): 
  def testCase1(self): 
    stack = MinMaxStack()
    stack.push(3)
    stack.push(1)
    stack.push(-2)
    stack.push(-1)
    stack.push(4)
    stack.pop()
    stack.peek()
    stack.getMin()
    stack.getMax()
    stack.view()
    actual = stack.view()
    expected = [3, 1, -2, -1]
    self.assertEqual(actual, expected)

if __name__ == '__main__':
  unittest.main(verbosity=2, exit=False)