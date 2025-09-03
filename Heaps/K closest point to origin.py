# K closest point to origin

import math as m
import heapq as heap

def solution(points,k):
    arr = []
    heap.heapify(arr)
    for x,y in points:
        dis = m.sqrt(m.pow(x, 2) + m.pow(y, 2))
        heap.heappush(arr, (dis, [x,y]))
    result = []
    while k:
        dis, points = heap.heappop(arr)
        result.append(points)
        k -= 1
    return result

points = [[1,3],[-2,2]]; k = 1
print(solution(points,k))