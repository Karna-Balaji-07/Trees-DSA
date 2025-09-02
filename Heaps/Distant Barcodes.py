# Distant Barcodes

import heapq as heap
def solution(arr):
    dicts = {}
    for i in arr:
        dicts[i] = dicts.get(i,0)+1
    arr = [(-count, value) for value, count in dicts.items()]
    heap.heapify(arr)
    result = []
    while arr:
        count1, value1 = heap.heappop(arr)
        if result and result[-1] == value1:
            count2, value2 = heap.heappop(arr)
            count2 +=1
            result.append(value2)
            if count2 != 0:
                heap.heappush(arr,(count2, value2))
            heap.heappush(arr,(count1, value1))
            
        else:
            result.append(value1)
            count1 += 1
            if count1 != 0:
                heap.heappush(arr,(count1, value1))
                
    return result

barcodes = [1,1,1,1,2,2,3,3]
print(solution(barcodes))    
        