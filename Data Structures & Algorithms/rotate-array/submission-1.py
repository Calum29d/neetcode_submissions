class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k):
            endNum = nums.pop()
            nums.insert(0, endNum)

        # O(n^2) time and space

        