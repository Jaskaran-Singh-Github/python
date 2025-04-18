#Solution 1
def longest_subarray_with_sum_k(arr, k):
    n = len(arr)
    max_length = 0

    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += arr[j]
            if curr_sum == k:
                max_length = max(max_length, j - i + 1)

    return max_length
print(longest_subarray_with_sum_k([10, 5, 2, 7, 1, -10], 15))
print(longest_subarray_with_sum_k([-5, 8, -14, 2, 4, 12], -5))
print(longest_subarray_with_sum_k([10, -10, 20, 30], 5))
