#Solution 7
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

def successful_pairs(spells, potions, success):
    potions.sort()  # Sort potions array
    result = []

    for spell in spells:
        min_potion = (success + spell - 1) // spell  
        index = binary_search(potions, min_potion)
        result.append(len(potions) - index)

    return result

# Example cases
print(successful_pairs([5,1,3], [1,2,3,4,5], 7))
print(successful_pairs([3,1,2], [8,5,8], 16))
