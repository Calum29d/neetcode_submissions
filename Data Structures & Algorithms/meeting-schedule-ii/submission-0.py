"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        endTimeHeap = [] #min heap to keep track of the earliest ending meeting

        intervals.sort(key = lambda interval: interval.start)

        for meeting in intervals:

            #room becomes available if the meeting with the earliest start time is less than the current meetings start because
            #the 2 meetings dont run at the same time
            if endTimeHeap and endTimeHeap[0] <= meeting.start:
                heapq.heappop(endTimeHeap)
            
            #since no room can be reused we add another room
            heapq.heappush(endTimeHeap, meeting.end)

        return len(endTimeHeap)



        