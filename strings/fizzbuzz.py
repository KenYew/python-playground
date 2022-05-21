def fizzBuzz(n):
  result = []
  for idx in range(1, n + 1): 
      currentString = ""
      if idx % 3 == 0: 
          currentString += "Fizz"
      if idx % 5 == 0:
          currentString += "Buzz"
      if not currentString:
          result.append(str(idx))
      else:
          result.append(currentString)
  return result

def main():
  t1 = 0
  t2 = 1
  t3 = -1 
  t4 = 5
  print(fizzBuzz(t1))
  print(fizzBuzz(t2))
  print(fizzBuzz(t3))
  print(fizzBuzz(t4))

if __name__ == "__main__":
  main()