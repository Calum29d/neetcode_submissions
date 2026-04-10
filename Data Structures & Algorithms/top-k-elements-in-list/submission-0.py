class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #this is going to be pretty brute force, cant think of a more efficent methods off the top of my head

        noFreq = {} #stores the frequency of each numbers in the list
        res = [0] * k #stores the k most frequent elements

        for num in nums:
            noFreq[num] = noFreq.get(num, 0) + 1 # makes 0 the default value for a num, add 1 as well

        sortedDict = sorted(noFreq.items(), key = lambda item: item[1], reverse=True) #sort the items of the hashmap in descending order

        for i in range(k):
            res[i] = sortedDict[i][0]

        return res

            
