def searchFloorOfANumber(array, key): 
  start, end = 0, len(array) - 1
  if key < array[start]:
    return -1
  while start <= end: 
    mid = (start + end) // 2
    if key < array[mid]: 
      end = mid - 1
    elif key > array[mid]: 
      start = mid + 1
    else: # key == array[mid]
      return mid 
  return end

def main(): 
  print(searchFloorOfANumber([4, 6, 10], 6))
  print(searchFloorOfANumber([1, 3, 8, 10, 15], 12))
  print(searchFloorOfANumber([4, 6, 10], 17))
  print(searchFloorOfANumber([4, 6, 10], -1))
if __name__ == "__main__":
  main()