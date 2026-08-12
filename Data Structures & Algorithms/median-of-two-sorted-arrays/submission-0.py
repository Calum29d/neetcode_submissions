class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        A,B = nums1, nums2
        total = len(nums1) + len(nums2) #get the total merged length
        half = total // 2 # get partition length

        if len(B) < len(A):#make sure A is always the smaller array
            A,B = B, A
 
        l,r  = 0, len(A) - 1
        while True:
            i = (l + r) // 2 #A middle
            j = half - i - 2 #partition of B

            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if (i + 1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")

            #if partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                #odd
                if total % 2:
                    return min(Aright, Bright)
                
                #even 
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

                # O(log(n + m)) time and O(1) space
                
        

        
        