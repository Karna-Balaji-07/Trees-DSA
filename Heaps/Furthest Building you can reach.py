# The furthest building you can reach

import heapq as heap
def solution(arr,ladder, bricks):
    heaps = []
    for i in range(1, len(arr)):
        diff = arr[i+1] - arr[i]
        if diff > 0:
            heap.heappush(heaps, diff)
            if len(heaps) > ladder:
                bricks -= heap.heappop(heaps)
                
            if bricks < 0:
                return i
            
    return len(arr)-1
    
    
def solutions(heights, ladders, bricks):
    for i in range( len(heights)-1):
        diff = heights[i+1] - heights[i]
        if diff > 0:
            if diff > bricks and ladders != 0:
                ladders -=1
            elif diff <= bricks and bricks != 0:
                bricks -= diff

            else:
                return i
    return len(heights)-1
                