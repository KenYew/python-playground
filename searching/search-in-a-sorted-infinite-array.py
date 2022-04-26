import math
class ArrayReader:
  def __init__(self, array): 
    self.array = array
  
  def get(self, index): 
    if index >= len(self.array): 
      return math.inf
    return self.array[index]

def searchInInfiniteArray(reader, key): 
  start, end = 0, 1
  while reader.get(end) < key: 
    newStart = end + 1
    end += (end - start + 1) * 2
    start = newStart
  return binarySearch(reader, key, start, end)

def binarySearch(reader, key, start, end): 
  while start <= end: 
    mid = (start + end) // 2
    if key < reader.get(mid): 
      end = mid - 1
    elif key > reader.get(mid): 
      start = mid + 1
    else:
      return mid
  return -1 

def main():
  reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
  print(searchInInfiniteArray(reader, 16))
  print(searchInInfiniteArray(reader, 11))
  reader = ArrayReader([1, 3, 8, 10, 15])
  print(searchInInfiniteArray(reader, 15))
  print(searchInInfiniteArray(reader, 200))

if __name__ == "__main__":
  main()