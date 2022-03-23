def fruitsIntoBaskets(array):
    windowStart, maxLength = 0, float("-inf")
    fruitBasket = {}
    
    for windowEnd in range(len(array)):
        rightFruit = array[windowEnd]
        if rightFruit not in fruitBasket:
            fruitBasket[rightFruit] = 0
        fruitBasket[rightFruit] += 1
        
        while len(fruitBasket) > 2:
            leftFruit = array[windowStart]
            fruitBasket[leftFruit] -= 1
            
            if fruitBasket[leftFruit] == 0:
                del fruitBasket[leftFruit]
            
            windowStart += 1
        maxLength = max(maxLength, windowEnd - windowStart + 1)
    return maxLength