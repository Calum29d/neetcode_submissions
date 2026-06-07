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


        for start, end in intervals:
            #if res is empty then append the interval, or if the intervals dont overlap, the end of the most recent interval is less than the start of the current interval
            if not res or res[-1][1] < start:
                res.append([start,end])
            
            #otherwise the intervals overlap so make the most recent intervals end = to the greater end time
            else:
                res[-1][1] = max(res[-1][1], end)
        
        return res



        