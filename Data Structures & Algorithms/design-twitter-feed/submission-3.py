class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = collections.defaultdict(list) # userId -> pair [time,tweetID]
        self.followMap = collections.defaultdict(set) # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                time, tweetId = self.tweetMap[followeeId][index]
                maxHeap.append([time, tweetId, followeeId, index - 1])
        heapq.heapify(maxHeap)

        while maxHeap and len(res) < 10:
            time, tweetId, followee, index = heapq.heappop(maxHeap)
            res.append(tweetId)
            
            if index >= 0:
                time, tweetId = self.tweetMap[followee][index]
                heapq.heappush(maxHeap, [time, tweetId, followee, index - 1])
            
        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
