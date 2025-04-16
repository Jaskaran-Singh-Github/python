def productExceptSelf(nums):
    n = len(nums)
    answer = [1] * n

    # Compute prefix products
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    # Compute suffix products and multiply with prefix products
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer

# Example usage
print("Output is:")
print(productExceptSelf([1,2,3,4]))  # Output: [24, 12, 8, 6]
print(productExceptSelf([-1,1,0,-3,3]))  # Output: [0, 0, 9, 0, 0]
