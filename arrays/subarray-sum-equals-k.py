def subarraySum(array, targetSum):
  runningSum, totalSum = 0, 0
  prefixSums = { 0:1 }

  for value in array: 
    runningSum += value
    prefixSum = runningSum - targetSum
    totalSum += prefixSums.get(prefixSum, 0)
    prefixSums[runningSum] = 1 + prefixSums.get(runningSum, 0)
  return totalSum

def main(): 
  array1 = [1, 1, 1]
  k1 = 2
  array2 = [1, 2, 3]
  k2 = 3
  print(subarraySum(array1, k1))
  print(subarraySum(array2, k2))

if __name__ == "__main__":
  main()