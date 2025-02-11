#problem 4
def minChocolateDifference(arr,m):
  arr.sort()
  min_diff=float('inf')
  for i in range (len(arr)-m+1):
    min_diff=min(min_diff,arr[i+m-1]-arr[i])
  return min_diff
print(minChocolateDifference([7,3,2,4,9,12,56],3))
print(minChocolateDifference([3,4,1,9,56,7,9,12],5))
