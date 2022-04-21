def searchCeilingOfANumber(array, key): 
  start, end = 0, len(array) - 1

  if key > array[end]: 
    return -1
  while start <= end: 
    mid = (start + end) // 2 
    if key < array[mid]:
      start = mid + 1
    elif key > array[mid]:
      end = mid - 1
    else: 
      return mid
  return start

def main():
  print(searchCeilingOfANumber([4, 6, 10], 6))
  print(searchCeilingOfANumber([1, 3, 8, 10, 15], 12))
  print(searchCeilingOfANumber([4, 6, 10], 17))
  print(searchCeilingOfANumber([4, 6, 10], -1))

main()