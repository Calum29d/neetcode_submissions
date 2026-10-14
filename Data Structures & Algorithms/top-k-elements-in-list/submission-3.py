class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = {}
        freqBuckets = [[] for _ in range(len(nums) + 1)] # index = freq -> [list of ints with that freq]

        for num in nums: # initalise freq
            freq[num] = freq.get(num, 0) + 1
        
        for num, count in freq.items():
            freqBuckets[count].append(num)
        
        for i in range(len(nums), -1, -1):
            for j in range(len(freqBuckets[i])):
                if len(res) == k:
                    return res
                res.append(freqBuckets[i][j])

        return res

        
        