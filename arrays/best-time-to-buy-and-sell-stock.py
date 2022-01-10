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

def maxProfit(prices):
    minPrice = float("inf")
    maxProfit = 0
    
    for price in prices: 
        if price < minPrice:
            minPrice = price
        elif price - minPrice > maxProfit:
            maxProfit = price - minPrice
    return maxProfit