# Top K frequent words

import heapq as heap
def solution(arr,k):
    arr.sort()
    dicts = {}
    for i in arr:
        dicts[i] = dicts.get(i,0)+1
    arr = [(-count, word) for word, count in dicts.items()]
    heap.heapify(arr)
    result = []
    while k:
        count, word = heap.heappop(arr)
        result.append(word)
        k -= 1
    
    return result
words = ["i","love","leetcode","i","love","coding"]; k = 2
print(solution(words, k))
    