def containsDuplicate(nums):
    seen = set()
    for num in nums: 
        if num in seen:
            return True
        seen.add(num)
    return False

nums = [2, 1, 5, 2, 3, 3, 4]
print(containsDuplicate(nums))