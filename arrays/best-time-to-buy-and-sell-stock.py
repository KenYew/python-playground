# O(n) Time | O(1) Space
def maxProfit(prices):
    if len(prices) < 1:
        return 0
    
    minPurchase = prices[0]
    maxProfit = 0
    for price in prices:
        minPurchase = min(minPurchase, price)
        profit = price - minPurchase
        maxProfit = max(maxProfit, profit)
    return maxProfit

# Kadane's Algorithm Concept
# O(n) Time | O(1) Space - where n is the length of the input array
def kadane(array): 
    # 1: Initialise two pointers for array traversal (maxSumEndingHere and maxSoFar)
    maxSumEndingHere = array[0] # Summation of all adjacent elements up to this point
    maxSoFar = array[0] # Maximum value of summations calculated so far 
    # 2: Traverse the array and compute for each element
    for idx in range(1, len(array)): 
        currentNum = array[idx]
        # 3: Using Kadane's algorithm, calculate maxSumEndingHere and maxSoFar with max functions for each element traversed so far
        maxSumEndingHere = max(currentNum, maxSumEndingHere + currentNum)
        maxSoFar = max(maxSoFar, maxSumEndingHere)
    return maxSoFar

# Using Kadane's Algorithm
# O(n) Time | O(1) Space - where n is the length of the input array
def maxProfit(prices):
    # EDGE: If input array is empty, return 0
    if len(prices) < 1:
        return 0
    
    # 1: Initialise minBuyPriceEndingHere pointer at the beginning of array and maxProfit value to keep track of max profits so far
    minBuyPriceEndingHere = prices[0] # Minimum value of elements traversed so far
    maxProfitSoFar = 0 # Maximum value of profit calculated so far (profit = currentPrice - minBuyPriceEndingHere)
    # 2: Traverse the array and compute for each value
    for currentPrice in prices:
        # 3: Using Kadane's algorithm, calculate minBuyPriceEndingHere and maxProfitSoFar with min and max functions for each element traversed so far
        minBuyPriceEndingHere = min(minBuyPriceEndingHere, currentPrice)
        profit = currentPrice - minBuyPriceEndingHere # Calculate current profit using currentPrice
        maxProfitSoFar = max(maxProfitSoFar, profit)
    return maxProfitSoFar

# Alternative Solution
def maxProfit(prices):
    minPrice = float("inf")
    maxProfit = 0
    
    for price in prices: 
        if price < minPrice:
            minPrice = price
        elif price - minPrice > maxProfit:
            maxProfit = price - minPrice
    return maxProfit