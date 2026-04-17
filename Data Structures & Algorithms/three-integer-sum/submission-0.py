class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedArray = sorted(nums)
        ans = []

        for i in range(len(sortedArray)):
            j = i+1
            k=len(sortedArray)-1
            target = -sortedArray[i]
            while j < k:
                if sortedArray[j] + sortedArray[k] < target:
                    j += 1
                elif sortedArray[j] + sortedArray[k] > target:
                    k -= 1
                else:
                    if [sortedArray[i], sortedArray[j], sortedArray[k]] in ans:
                        j += 1
                        k -= 1
                        continue
                    else:
                        ans.append([sortedArray[i], sortedArray[j], sortedArray[k]])
                        j += 1
                        k -= 1
        return ans






        