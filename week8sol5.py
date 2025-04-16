def insert(intervals, newInterval):
    result = []
    inserted = False

    for interval in intervals:
        if interval[1] < newInterval[0]:
            result.append(interval)
        elif interval[0] > newInterval[1]:
            if not inserted:
                result.append(newInterval)
                inserted = True
            result.append(interval)
        else:
            newInterval[0] = min(newInterval[0], interval[0])
            newInterval[1] = max(newInterval[1], interval[1])
    if not inserted:
        result.append(newInterval)

    return result
print(insert([[1,3],[6,9]], [2,5]))  

print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))  
