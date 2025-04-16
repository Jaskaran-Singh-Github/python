def smallestMissing(nums):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == mid:
            low = mid + 1
        else:
            high = mid - 1

    return low
# Test case 1
nums1 = [0, 1, 2, 6, 9, 11, 15]
print("Test case 1 Output:", smallestMissing(nums1))  # Output: 3

# Test case 2
nums2 = [1, 2, 3, 4, 6, 9, 11, 15]
print("Test case 2 Output:", smallestMissing(nums2))  # Output: 0

# Additional test case
nums3 = [0, 1, 2, 3, 4, 5]
print("Test case 3 Output:", smallestMissing(nums3))  # Output: 6
