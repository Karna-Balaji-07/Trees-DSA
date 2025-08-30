# Heapq

import heapq as heap

arr = [25, 20, 15, 30, 40]
heap.heapify(arr)
heap.heappush(arr,10)
heap.heappush(arr,35)
mini = heap.heappop(arr)
print(arr)
print('Minimum Element from the list : ',mini)

large = heap.nlargest(2,arr)
small = heap.nsmallest(2,arr)
print(large," ",small)