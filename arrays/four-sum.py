def fourSum(array, targetSum):
  result = []
  for idx in range(len(array) - 3):
    if idx > 0 and array[idx - 1] == array[idx]:
      continue
    for jdx in range(1, len(array) - 2): 
      if jdx > idx + 1 and array[jdx - 1] == array[jdx]:
        continue
      twoSum(idx, jdx, array, targetSum, result)
  return result

def twoSum(first, second, array, targetSum, result): 
  left = second + 1
  right = len(array) - 1
  while left < right: 
    _sum = array[first] + array[second] + array[left] + array[right]
    if _sum < targetSum: 
      left += 1
    elif _sum > targetSum: 
      right -= 1
    else: 
      result.append([array[first], array[second], array[left], array[right]])
      left += 1
      right -= 1
      while left < right and array[left - 1] == array[left]: 
        left += 1
      while left < right and array[right + 1] == array[right]:
        right -= 1

def main(): 
  array = [-3, -2, -1, 0, 1, 1, 2, 2, 3, 3]
  targetSum = 4
  print(fourSum(array, targetSum))

if __name__ == "__main__":
  main()