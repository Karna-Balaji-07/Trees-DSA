# Reorganize String

import heapq as heap
def solution(s):
    dicts = {}
    for i in s:
        dicts[i] = dicts.get(i,0)+1
    
    arr = [(-count,char) for char,count in dicts.items()]
    heap.heapify(arr)
    result = []
    while heap:
        count1,char1 = heap.heappop(arr)
        if result and result[-1] == char1:
            if not heap:
                return ""
            count2, char2 = heap.heappop(arr)
            count2 += 1
            result.append(char2)
            if count2 != 0:
                heap.heappush(arr,(count2, char2))
            heap.heappush(arr,(count1, char1))
        else:
            result.append(char1)
            count1 +=1
            if count1 != 0:
                heap.heappush(arr,(count1, char1))
    return "".join(result)