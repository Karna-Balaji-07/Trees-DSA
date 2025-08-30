# The last stone weight

import heapq as heap
def solution(arr):
    arr = [-x for x in arr]
    heap.heapify(arr)
    while len(arr) > 1:
        stone1 = heap.heappop(arr)
        stone2 = heap.heappop(arr)
        diff = stone1 - stone2
        if diff == 0:
            continue
        heap.heappush(arr,diff)
        
    return [-x for x in arr]

stones = [2,7,4,1,8,1]
print(solution(stones))