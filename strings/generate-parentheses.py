def generateParentheses(n): 
  stack = [] 
  result = []

  def backtrack(numberOfOpen, numberOfClosed):
    if numberOfOpen == numberOfClosed == n: 
      result.append("".join(stack))
    
    if numberOfOpen < n:
      stack.append("(")
      backtrack(numberOfOpen + 1, numberOfClosed)
      stack.pop() # clean up stack for next use

    if numberOfClosed < numberOfOpen:
      stack.append(")")
      backtrack(numberOfOpen, numberOfClosed + 1)
      stack.pop() # clean up stack for next use

  backtrack(0, 0)
  return result

def main(): 
  n = 3
  print(generateParentheses(n))

if __name__ == "__main__":
  main()