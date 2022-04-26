def findMaxInBitonicArray(array): 
  start, end = 0, len(array) - 1
  while start < end: 
    mid = (start + end) // 2
    if array[mid] > array[mid + 1]: 
      end = mid 
    else:
      start = mid + 1 
  return array[start]

def main():
  print(findMaxInBitonicArray([1, 3, 8, 12, 4, 2]))
  print(findMaxInBitonicArray([3, 8, 3, 1]))
  print(findMaxInBitonicArray([1, 3, 8, 12]))
  print(findMaxInBitonicArray([10, 9, 8]))

if __name__ == "__main__":
  main()