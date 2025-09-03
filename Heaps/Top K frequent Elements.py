# Top K frequent elements in an array

import heapq as heap
def solution(arr,k):
    dicts = {}
    for i in arr:
        dicts[i] = dicts.get(i,0)+1
    
    arr = [(-count, value) for value,count in dicts.items()]
    heap.heapify(arr)
    result = []
    while k and heap:
        count, value = heap.heappop(arr)
        result.append(value)
        k -= 1
    return result
