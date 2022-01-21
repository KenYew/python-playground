def trap(height):
    if len(height) <= 2: return 0
    n = len(height)
    maxLeft, maxRight = height[0], height[n-1]
    left, right = 1, n - 2
    ans = 0
    while left <= right:
        if maxLeft < maxRight:
            if height[left] > maxLeft:
                maxLeft = height[left]
            else:
                ans += maxLeft - height[left]
            left += 1
        else:
            if height[right] > maxRight:
                maxRight = height[right]
            else:
                ans += maxRight - height[right]
            right -= 1
    return ans
    
def trap(height):
    left_max, right_max = height[0], height[-1]
    l, r = 1, len(height) - 2
    res = 0
    while l <= r:
        left_max = max(left_max, height[l])
        right_max = max(right_max, height[r])
        if left_max < right_max:
            res += left_max - height[l]
            l += 1
        else:
            res += right_max - height[r]
            r -= 1
    return res 