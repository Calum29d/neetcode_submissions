class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # overlap if start1 < end2 and end1 > start2
        intervals.sort()
        res = [intervals[0]]

        for start, end in intervals[1:]:
            if start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start,end])

        return res

