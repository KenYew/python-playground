def searchNextLetter(array, key): 
  start, end = 0, len(array) - 1
  while start <= end: 
    mid = (start + end) // 2
    if key < array[mid]: 
      end = mid - 1
    else: 
      start = mid + 1
  return array[start % len(array)]

def main():
  print(searchNextLetter(['a', 'c', 'f', 'h'], 'f'))
  print(searchNextLetter(['a', 'c', 'f', 'h'], 'b'))
  print(searchNextLetter(['a', 'c', 'f', 'h'], 'm'))

if __name__ == "__main__":
  main()