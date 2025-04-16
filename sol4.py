#Solution 4
def singleNumber(nums):
    xor_all=0
    for num in nums:
        xor_all ^=num
    diff=xor_all & -xor_all
    res=[0,0] 
    for num in nums:
        if num & diff:
            res[0] ^=num
        else:
            res[1] ^=num
    return res
print(singleNumber([1,2,1,3,2,5]))
print(singleNumber([-1,0]))
print(singleNumber([0,1]))                