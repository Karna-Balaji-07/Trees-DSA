# kth largest element in the array

import heapq as heap
def solution(arr,k):
    arr = [-x for x in arr]
    heap.heapify(arr)
    mini = 0
    while k and heap:
        mini = heap.heappop(arr)
        k -= 1
    return -mini


nums = [3,2,1,5,6,4]; k = 2
print(solution(nums,k))