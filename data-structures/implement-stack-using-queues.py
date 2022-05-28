from collections import deque
class MyStack: 
  def __init__(self): 
    self.queue = deque()
  
  # O(1) Time | O(1) Space
  def peek(self): 
    return self.queue[len(self.queue) - 1]
  
  # O(n) Time | O(1) Space
  def pop(self): 
    for idx in range(len(self.queue) - 1): 
      self.queue.append(self.queue.popleft())
    return self.queue.popleft()
  
  # O(1) Time | O(1) Space
  def push(self, number): 
    self.queue.append(number)
  
  # O(1) Time | O(1) Space
  def empty(self): 
    return len(self.queue) == 0