#problem 3
def countPairs(arr,k):
  freq={}
  count=0
  for num in arr:
    complement=k-num
    if complement in freq:
      count+=freq[complement]
    freq[num]=freq.get(num,0)+1
  return count
print(countPairs([1,5,7,-1],6))
print(countPairs([1,5,7,-1,5],6))