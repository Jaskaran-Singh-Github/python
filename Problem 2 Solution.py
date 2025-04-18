#Solution 2
def max_product_triplet(arr):
    if len(arr) < 3:
        return "Array must have at least three elements"

    arr.sort()
    option1 = arr[-1] * arr[-2] * arr[-3]
    option2 = arr[0] * arr[1] * arr[-1]
    if option1 > option2:
        return (arr[-3], arr[-2], arr[-1])
    else:
        return (arr[0], arr[1], arr[-1])
print(max_product_triplet([-4, 1, -8, 9, 6]))
print(max_product_triplet([1, 7, 2, -2, 5]))

