def searchRotatedArray(array, key): 
  start, end = 0, len(array) - 1
  while start <= end: 
    mid = (start + end) // 2
    if array[mid] == key:
      return mid

    if array[start] == array[mid] and array[end] == array[mid]:
      start += 1
      end -= 1
    elif array[start] <= array[mid]: 
      if key >= array[start] and key < array[mid]: 
        end = mid - 1
      else: 
        start = mid + 1
    else: 
      if key > array[mid] and key <= array[end]: 
        start = mid + 1
      else: 
        end = mid - 1
    
  return -1

def main():
  print(searchRotatedArray([10, 15, 1, 3, 8], 15))
  print(searchRotatedArray([4, 5, 7, 9, 10, -1, 2], 10))
  print(searchRotatedArray([3, 7, 3, 3, 3], 7))

if __name__ == "__main__":
  main()