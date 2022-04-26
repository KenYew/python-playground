def searchMinDiffElement(array, key): 
  if key < array[0]: 
    return array[0]
  if key > array[len(array) - 1]: 
    return array[len(array) - 1]

  start, end = 0, len(array) - 1
  while start <= end: 
    mid = (start + end) // 2
    if key < array[mid]: 
      end = mid - 1
    elif key > array[mid]: 
      start = mid + 1
    else: 
      return array[mid]

  # Position of pointers from this line of code: end* -> key -> start*
  if (key - array[end]) < (array[start] - key): 
    return array[end]
  else: 
    return array[start]

def main():
  print(searchMinDiffElement([4, 6, 10], 7))
  print(searchMinDiffElement([4, 6, 10], 4))
  print(searchMinDiffElement([1, 3, 8, 10, 15], 12))
  print(searchMinDiffElement([4, 6, 10], 17))

if __name__ == "__main__":
  main()