# reduce Array half the size

import heapq as heap

def solution(arr):
    dicts = {}
    for i in arr:
        dicts[i] = dicts.get(i,0)+1
    heaps = [-count for count in dicts.values()]
    heap.heapify(heaps)
    removed = 0
    total_removed = 0
    half = len(arr) // 2
    while removed < half:
        most = -heap.heappop(heaps)
        removed  += most
        total_removed +=1
    return total_removed

arr = [3,3,3,3,5,5,5,2,2,7]
print(solution(arr))