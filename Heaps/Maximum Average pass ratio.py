# Maximum average pass ratio

import heapq as heap
def solution(arr,extra):
    maxheap = [(-(a/b)-(a+1)/(b+1),a,b) for a,b in arr]
    heap.heapify(maxheap)
    for i in range(extra):
        arrs,passs, total = heap.heappop(maxheap)
        passs += 1
        total += 1
        
        narrs = -(passs/total-(passs+1) / (total+1))
        heap.heappush(maxheap,(narrs, passs, total))
    total_ratio = sum(pass_students / total_students for _, pass_students, total_students in maxheap)

    return total_ratio / len(arr)