def findRange(array, key): 
  result = [-1, -1] 
  result[0] = binarySearch(array, key, False)
  if result[0] != -1: 
    result[1] = binarySearch(array, key, True) 
  return result

def binarySearch(array, key, findMaxIdx):
  keyIdx = -1
  start, end = 0, len(array) - 1
  while start <= end: 
    mid = (start + end) // 2
    if key < array[mid]: 
      end = mid - 1
    elif key > array[mid]: 
      start = mid + 1
    else: 
      keyIdx = mid
      if findMaxIdx: 
        start = mid + 1 
      else: 
        end = mid - 1
  return keyIdx

def main():
  print(findRange([4, 6, 6, 6, 9], 6))
  print(findRange([1, 3, 8, 10, 15], 10))
  print(findRange([1, 3, 8, 10, 15], 12))

if __name__ == "__main__":
  main()