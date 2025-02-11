#problem 2
def rearrange_numbers(arr):
  n=len(arr)
  j=0
  for i in range(n):
    if arr[i]<0:
      temp=arr[i]
      for k in range(i,j,-1):
        arr[k]=arr[k-1]
      arr[j]=temp
      j+=1
  return arr
print(rearrange_numbers([-12,11,-13,-5,6,-7,5,-3,-6]))
print(rearrange_numbers([-12,11,13,-5,6,-7,5,-3,8]))

