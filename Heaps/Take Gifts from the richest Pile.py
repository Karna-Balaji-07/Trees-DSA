# Take gifts from the richest pile

import heapq as heap
import math as m
def solution(arr,k):
    arrs = [-x for x in arr]
    heap.heapify(arrs)
    sums = 0
    while k > 0:
        mini = -1*(heap.heappop(arrs))
        sums = m.floor(m.sqrt(mini))
        heap.heappush(arrs,-sums)
        k -=1
    sums = -1 * sum(arrs)
    return sums

gifts = [25,64,9,4,100]
k = 4
print(solution(gifts,k))
