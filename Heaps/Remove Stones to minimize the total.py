# Remove stones to minimize the total
import math as m
import heapq as heap
def solution(arr,k):
    arr = [-x for x in arr]
    heap.heapify(arr)
    while k:
        maxi = heap.heappop(arr)
        maxi = m.floor((maxi/2))
        heap.heappush(arr, maxi)
        k -= 1
    sums = sum(arr)
    return -sums

piles = [5,4,9];k = 2
print(solution(piles,k))