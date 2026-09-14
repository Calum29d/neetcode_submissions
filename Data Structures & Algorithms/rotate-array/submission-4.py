class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        def reverseList(l, r): 

            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        reverseList(0, len(nums) - 1) # reverse whole list
        reverseList(0, k - 1) # reverse the first k portion 
        reverseList(k, len(nums) - 1) # reverse everything after k elements

        # O(n) time O(1) space



        