import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # each task takes 1 unit of time
        # and we want the min time to complete all tasks

        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque() # pair of [-cnt, when we can process this task]
        
        # while there are still tasks to process
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap) # add 1 to process the task
                if cnt:
                    q.append([cnt, time + n]) # calculate when we can process the task again
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time

        #O(m) time and O(1) space as only using A-Z at max O(26) space so constant m is size of input array

        