class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #O(nlogn) time and O(1) space
        #first sort the intervals by start time
        intervals.sort(key = lambda interval: interval[0])

        removed = 0
        prevEnd = intervals[0][1]


        for start, end in intervals[1:]:
            #if the intervals dont overlap then update the previous end to the current
            if start >= prevEnd:
                prevEnd = end

            #otherwise there is an overlap so you 'remove' the overlap by updating the previous end to the interval with
            #the smaller end time, as if we take the smallest then that reduces the chances of other overlaps
            else:
                removed += 1
                prevEnd = min(prevEnd, end)
            
        return removed




        