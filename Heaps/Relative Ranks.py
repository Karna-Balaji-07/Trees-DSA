# Relative ranks

import heapq as heap
def solution(score):
# Pair each score with its original index
    indexed_scores = [(s, i) for i, s in enumerate(score)]
    # Sort the scores in descending order
    indexed_scores.sort(reverse=True)
    
    # Prepare the result array
    result = [''] * len(score)
    for rank, (s, i) in enumerate(indexed_scores):
        if rank == 0:
            result[i] = "Gold Medal"
        elif rank == 1:
            result[i] = "Silver Medal"
        elif rank == 2:
            result[i] = "Bronze Medal"
        else:
            result[i] = str(rank + 1)
    return result
    
    

arr = [5,2,10,9,6,8]
print(solution(arr))