def maxProduct(nums):
    maxProduct, minProduct, result = nums[0], nums[0], nums[0]
    for i in range(1, len(nums)):
        postiveProduct = max(nums[i], maxProduct*nums[i], minProduct*nums[i])
        negativeProduct = min(nums[i], maxProduct*nums[i], minProduct*nums[i])            
        maxProduct, minProduct = postiveProduct, negativeProduct
        result = max(maxProduct, result)
    return result