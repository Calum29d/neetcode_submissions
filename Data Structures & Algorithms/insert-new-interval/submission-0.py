class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        start, end = 0 , len(intervals) - 1
        
        #binary search to find the position of insertion, left pointer will end up where it needs to be
        while start <= end:
            mid = (start + end) // 2

            if newInterval[0] < intervals[mid][0]:
                end = mid - 1

            else:
                start = mid + 1

        intervals.insert(start, newInterval)

        res = []

        for interval in intervals:
            if not res or res[-1][-1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
            
        return res

    



        