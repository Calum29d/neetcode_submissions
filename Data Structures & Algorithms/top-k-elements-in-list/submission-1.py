class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        freq = [ [] for i in range (len(nums) + 1)]
        res = []

        for num in nums:
            count[num] = count.get(num, 0) + 1 #get the frequency of each number
        
        for num, count in count.items():
            freq[count].append(num) #append the number to the index, the index is used as the count of the num freq
        
        for i in range(len(freq) -1, 0, -1): #loop in descending order to index 1 as 0 isnt needed going down 1 by one
            for num in freq[i]:
                res.append(num)
            if len(res) == k:
                return res

        #this is the O(n) space and time method using a variation of 'bucket sort'

        