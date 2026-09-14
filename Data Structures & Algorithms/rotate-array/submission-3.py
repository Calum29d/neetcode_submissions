class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        temp = [0] * len(nums)

        for i in range(len(nums)):
            temp[(i + k) % len(nums)] = nums[i]
        
        nums[:] = temp

        #O(n) time and space

        