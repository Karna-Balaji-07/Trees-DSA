# Task Scheduler

import heapq  as heap
def solution(arr,n):
    dicts = {}
    for i in arr:
        dicts[i] = dicts.get(i,0)+1
    
    arr = [(-count, value) for value, count in dicts.items()]
    heap.heapify(arr)
    result = 0
    temp = []
    while arr:
        cycle = []
        for i in range(n+1):
            if arr:
                count1, value1 = heap.heappop(arr)
                temp.append(value1)
                if count1 + 1 < 0:
                    cycle.append((count1+1, value1))
                
            result +=1
            if not arr and not cycle:
                return result
            
            
        for item in cycle:
            heap.heappush(arr, item)
            
    return result