class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        last = len(nums1) - 1 # where we place elements

        # merge in reverse order
        while m > 0 and n > 0: # while we still have elements in both arrays 
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1
        
        while n > 0:
            nums1[last] = nums2[n - 1]
            n, last = n - 1, last - 1
        

        