def trap_water(height):
    n=len(height)
    trapped_water=0
    for i in range(n):
        left_max=max(height[:i+1])
        right_max=max(height[i:])   
        trapped_water += min(left_max,right_max)-height[i]
    return trapped_water 
print(trap_water([0,1,0,2,1,0,1,3,2,1,2,1]))  
print(trap_water([4,2,0,3,2,5]))