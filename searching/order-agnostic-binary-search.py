def binarySearch(array, key): 
    start, end = 0, len(array) - 1
    isAscending = array[start] < array[end]

    while start <= end: 
        mid = (start + end) // 2
        if key == array[mid]: 
            return mid

        if isAscending: 
            if key < array[mid]: 
                end = mid - 1 
            else:
                start = mid + 1
        else:
            if key > array[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1 

def main():
  print(binarySearch([4, 6, 10], 10))
  print(binarySearch([1, 2, 3, 4, 5, 6, 7], 5))
  print(binarySearch([10, 6, 4], 10))
  print(binarySearch([10, 6, 4], 4))

if __name__ == "__main__":
    main()