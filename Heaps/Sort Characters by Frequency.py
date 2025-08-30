# Sort characters by frequency

import heapq as heap
def solution(s):
    arr = list(s)
    print(arr)
    dicts = {}
    for i in arr:
        dicts[i]  =dicts.get(i,0)+1
    heaps = [(-count, ch) for ch, count in dicts.items()]
    heap.heapify(heaps)
    result = []
    while heaps:
        count, char = heap.heappop(heaps)
        result.append(-count * (char))
        
    return "".join(result)

s = "tree"
print(solution(s))