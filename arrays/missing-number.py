def missingNumber(array):
  result = len(array)
  for idx in range(len(array)): 
    result += (idx - array[idx])
  return result 

def main(): 
  array = [9, 6, 4, 2, 3, 5, 7, 0, 1]
  print(missingNumber(array))

if __name__ == "__main__":
  main()