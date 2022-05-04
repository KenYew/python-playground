# O(n^2) Time - O(nlogn) + O(n^2) asymptotically equivalent to O(n^2)
# O(n) Space
def threeSumClosest(array, targetSum): 
  array.sort()
  smallestDifference = float("inf")
  for idx in range(len(array) - 2): 
    if idx > 0 and array[idx - 1] == array[idx]: 
      continue
    left, right = idx + 1, len(array) - 1
    while left < right: 
      targetDifference = targetSum - array[idx] - array[left] - array[right]
      if targetDifference == 0: 
        return targetSum

      if abs(targetDifference) < abs(smallestDifference) or (abs(targetDifference) == abs(smallestDifference) and targetDifference > smallestDifference):
        smallestDifference = targetDifference
      
      if targetDifference > 0: 
        left += 1
      else: 
        right -= 1

  return targetSum - smallestDifference

def main():
  print(threeSumClosest([-2, 0, 1, 2], 2))
  print(threeSumClosest([-3, -1, 1, 2], 1))
  print(threeSumClosest([1, 0, 1, 1], 100))

if __name__ == "__main__":
  main()