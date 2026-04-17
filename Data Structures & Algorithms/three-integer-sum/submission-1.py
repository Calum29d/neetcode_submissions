class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedArray = sorted(nums)
        ans = []

        for i in range(len(sortedArray)):
            if i > 0 and sortedArray[i] == sortedArray[i-1]: #skips the duplicate i
                continue

            j = i+1
            k=len(sortedArray)-1
            target = -sortedArray[i]
            while j < k:

                if sortedArray[j] + sortedArray[k] < target:
                    j += 1
                elif sortedArray[j] + sortedArray[k] > target:
                    k -= 1
                else:
                    ans.append([sortedArray[i], sortedArray[j], sortedArray[k]])
                    j += 1
                    k -= 1
                    while j < k and sortedArray[j] == sortedArray[j - 1]:
                        j += 1
                    while j < k and sortedArray[k] == sortedArray[k + 1]:
                        k -= 1
        return ans

        #i struggled on this one so much






        