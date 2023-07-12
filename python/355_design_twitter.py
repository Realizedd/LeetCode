import heapq
from collections import defaultdict
from typing import List


class Twitter:

    def __init__(self):
        self.followMap = defaultdict(list)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((tweetId, self.time))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        followTweets = {k: self.tweets[k].copy() for k in self.followMap[userId]}
        followTweets[userId] = self.tweets[userId].copy()
        maxHeap, feed = [], []

        for followId in followTweets:
            if followTweets[followId]:
                tweet = followTweets[followId].pop()
                heapq.heappush(maxHeap, (-tweet[1], tweet[0], followId))

        while maxHeap and len(feed) < 10:
            res = heapq.heappop(maxHeap)
            feed.append(res[1])

            if followTweets[res[1]]:
                tweet = followTweets[res[1]].pop()
                heapq.heappush(maxHeap, (-tweet[1], tweet[0], res[1]))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)