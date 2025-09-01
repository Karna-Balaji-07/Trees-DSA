# Longest happy string

import heapq
def solution(a,b,c):
    heap = []
    for count, char in ([(-a,'a'),(-b,'b'),(-c,'c')]):
        heapq.heappush(heap, (count,char))
    
    result = []
    while heap:
        count1, char1 = heapq.heappop(heap)
        if len(result) >= 2 and result[-1] == result[-2] == char1:
            if not heap:
                break
            count2, char2 = heapq.heappop(heap)
            result.append(char2)
            count2 +=1 
            if count2 != 0:
                heapq.heappush(heap, (count2, char2))
            heapq.heappush(heap,(count1, char1))
            
        else:
            result.append(char1)
            count1 +=1
            if count1 != 0:
                heapq.heappush(heap,(count1, char1))
            
    return "".join(result)