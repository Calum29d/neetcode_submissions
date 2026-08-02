import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = [] #will store (-value, index) so its a max heap
        res = []

        for i, num in enumerate(nums):
            heapq.heappush(heap, (-num, i))

            #delete all entries that have their index out of the range of the current window
            while heap[0][1] <= i - k:
                heapq.heappop(heap)
            
            #once we have seen k elements save the current max
            if i >= k - 1:
                res.append(-heap[0][0])
            
        return res

        #O(nlogn) time and O(n) space