## Method 1: O(1) Time for push() and O(1) Amortized Time for pop()
class MyQueue:
  def __init__(self):
    self.stack1 = []
    self.stack2 = []

  def push(self, number):
    self.stack1.append(number)

  def pop(self):
    self.peek()
    return self.stack2.pop()

  def peek(self):
    if not self.stack2:
      while self.stack1:
        self.stack2.append(self.stack1.pop())
    return self.stack2[-1]        
  
  def empty(self):
    return not self.stack1 and not self.stack2

## Method 2: O(n) Time for push()
class MyQueue:
  def __init__(self):
    self.stack1 = []
    self.stack2 = []

  def push(self, number):
    while self.stack1:
      self.stack2.append(self.stack1.pop())
    self.stack1.append(number)
    while self.stack2:
        self.stack1.append(self.stack2.pop())

  def pop(self):
    return self.stack1.pop()

  def peek(self):
    return self.stack1[-1]

  def empty(self):
    return not self.stack1