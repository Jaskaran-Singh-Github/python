import bisect

def lengthOfLIS(nums):
    sub = []

    for num in nums:
        i = bisect.bisect_left(sub, num)
        if i == len(sub):
            sub.append(num)
        else:
            sub[i] = num
        # Print intermediate steps (optional for learning)
        print(f"After processing {num}: sub = {sub}")

    return len(sub)

# Example 1
nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
print("Example 1 Output:", lengthOfLIS(nums1))  # Output: 4

print()

# Example 2
nums2 = [0, 1, 0, 3, 2, 3]
print("Example 2 Output:", lengthOfLIS(nums2))  # Output: 4

print()

# Example 3
nums3 = [7, 7, 7, 7, 7, 7, 7]
print("Example 3 Output:", lengthOfLIS(nums3))  # Output: 1


