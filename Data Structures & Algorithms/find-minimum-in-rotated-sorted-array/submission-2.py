class Solution:
        def findMin(self, nums: List[int]) -> int:
            #when an array is rotated the number of times it was rotated is the index of the min number
            #but how do i find out how many times it was rotated
            #i found that if you find the last element that is bigger than the first number in array then the index+1 is the rotation
            #but if i can find the biggest element why cant i just find the min?

            start, end = 0, len(nums)-1

            if nums[start] <= nums[end]:
                return nums[0] #this checks if any rotations have happened
            
            while start < end:
                mid = (start+end) // 2

                if nums[mid] > nums[end]: #if middle is greater than last element then min must be on the right
                    start = mid + 1 #so move to the right
                else:
                    end = mid

            return nums[start]

            #this is another way to do it











