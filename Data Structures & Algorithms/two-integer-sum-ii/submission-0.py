class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        #1. loop for each number
        #2. calculate number to find
        #3. perform binary search on every index infront of the current number

        for i in range(len(numbers)):
            numToFind = target - numbers[i]
            
            #declare window for binary search
            l, r = i + 1, len(numbers) - 1

            #binary search
            while l <= r:
                mid = (l + r) // 2

                if numbers[mid] == numToFind:
                    return [1 + i, 1 + mid]
                
                if numbers[mid] > numToFind:
                    r = mid - 1
                    
                else:
                    l = mid + 1
        
        #O(nlogn) time O(1) space thought it would resolve to O(n) time because i thought binary search is just 2 pointers but i guess the actual solution is a lot more simple


        