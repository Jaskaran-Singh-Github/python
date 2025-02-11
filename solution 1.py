#problem 1
def threesum(nums):
  n=len(nums)
  res=set()
  for i in range(n):
    for j in range(i+1,n):
      for k in range (j+1,n):
        if nums[i]+nums[j]+nums[k]==0:
          res.add(tuple(sorted([nums[i],nums[j],nums[k]])))
  return [list(triplet) for triplet in res]
print(threesum([-1,0,1,2,-1,-4]))
print(threesum([0,1,1]))
print(threesum([0,0,0]))