def longestConsecutive(nums):
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak
nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(nums))  

nums = [0,3,7,2,5,8,4,6,0,1]
print(longestConsecutive(nums))  

nums = [1,0,1,2]
print(longestConsecutive(nums))