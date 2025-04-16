#Solution 5
class SparseVector:
    def __init__(self,nums):
        self.data={i:num for i,num in enumerate(nums)if num!=0}
    def dotProduct(self,vec):
        return sum(self.data[i]*vec.data[i] for i in self.data if i in vec.data)    
    
v1=SparseVector([1,0,0,2,3])    
v2=SparseVector([0,3,0,4,0])   
print(v1.dotProduct(v2)) 

v3=SparseVector([0,1,0,0,0])    
v4=SparseVector([0,0,0,0,2])   
print(v3.dotProduct(v4))