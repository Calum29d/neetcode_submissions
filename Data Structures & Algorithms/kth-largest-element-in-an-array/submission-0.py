import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = nums
        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)

        return nums[0]

        # Time: (nlogk) 
        # Space: O(n)
        