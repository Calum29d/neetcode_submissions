class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if i can find where the array splits then i can do a binary search on both parts
        #If i use the way to find the minimum in the array then i can use that to choose where to search
        
        start, end = 0, len(nums)-1
        splittingIndex = 0

        if nums[start] >= nums[end]: #only run if the array is rotated
            while start <= end:
                mid = (start+end) // 2

                if nums[mid] > nums[-1]: #if middle is greater than last element then min must be on the right
                    start = mid + 1 #so move to the right
                else:
                    end = mid - 1

            splittingIndex = start

        start, end = 0, len(nums) - 1
        if nums[splittingIndex] <= target <= nums[end]:
            start = splittingIndex
        else:
            end = splittingIndex - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                return mid
        return -1
            

        
            

    
        