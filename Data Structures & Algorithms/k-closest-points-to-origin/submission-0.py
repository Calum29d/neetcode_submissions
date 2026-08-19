import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []

        for x, y in points:
            minHeap.append([(x ** 2) + (y ** 2), x, y])

        heapq.heapify(minHeap)
        
        for _ in range(k):
            dist, x, y = heapq.heappop(minHeap)
            res.append([x,y])
        
        return res

        # Time: O(n + klogn) where n is len of list and k is number of closest points
        # Space O(n)

        