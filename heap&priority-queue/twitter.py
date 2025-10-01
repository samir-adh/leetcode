from typing import DefaultDict, List
from _heapq import heapify, heappop, heappush


class Twitter:
    def __init__(self):
        self.tweets = DefaultDict(list)
        self.followees = DefaultDict(set)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        for followeeId in self.followees[userId].union(set([userId])):
            if not self.tweets[followeeId]:
                continue
            count, tweetId = self.tweets[followeeId][-1]
            index = len(self.tweets[followeeId]) - 1
            minHeap.append((count, tweetId, followeeId, index))
        heapify(minHeap)
        feed = []
        while len(feed) < 10 and minHeap:
            count, tweetId, followeeId, index = heappop(minHeap)
            feed.append(tweetId)
            if index - 1 >= 0:
                count, tweetId = self.tweets[followeeId][index - 1]
                heappush(minHeap, (count, tweetId, followeeId, index - 1))
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
def test_case1():
    args = zip(
        [
            "postTweet",
            "getNewsFeed",
            "follow",
            "postTweet",
            "getNewsFeed",
            "unfollow",
            "getNewsFeed",
        ],
        [[1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]],
    )

    t = Twitter()
    for command, arg in args:
        out = None
        if command == "postTweet":
            out = t.postTweet(arg[0], arg[1])
        if command == "getNewsFeed":
            out = t.getNewsFeed(arg[0])
        if command == "follow":
            out = t.follow(arg[0], arg[1])
        if command == "unfollow":
            out = t.unfollow(arg[0], arg[1])
        print(f"{t.count} : {out}")


test_case1()
