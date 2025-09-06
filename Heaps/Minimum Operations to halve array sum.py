# Minimum operations to halvve array sum
import heapq as heap
class Solution:
    def halveArray(self, arr: List[int]) -> int:
        sums = sum(arr)
        target = sums/2
        curr = sums
        arr = [-x for x in arr]
        heap.heapify(arr)
        count = 0
        while curr > target:
            maxi = -heap.heappop(arr)
            half = maxi/2
            curr -= half
            heap.heappush(arr, -half)
            count += 1
        return count


nums = [3,8,20]
print(solution(nums))