from typing import Deque, List


class Twitter:
    def __init__(self):
        self.tweets: dict[int, Deque[tuple[int, int]]] = {}
        self.followees: dict[int, set[int]] = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweets = self.tweets.get(userId, Deque([]))
        tweets.appendleft((self.time, tweetId))
        if len(tweets) > 10:
            tweets.pop()
        self.tweets[userId] = tweets
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        toSort = [
            self.tweets.get(followee, Deque([])).copy()
            for followee in self.followees.get(userId, set([])).union([userId])
        ]
        # print(toSort)
        tweets_count = sum([len(u) for u in toSort])
        feed = []
        while len(feed) < 10 and tweets_count > 0:
            maxIdx = -1
            for i in range(len(toSort)):
                user = toSort[i]
                if len(user) > 0 and user[0][0] > maxIdx:
                    maxIdx = i
            if maxIdx != -1:
                feed.append(toSort[maxIdx].popleft()[1])
                tweets_count -= 1
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followees:
            self.followees[followerId].add(followeeId)
        else:
            self.followees[followerId] = set([followeeId])

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followees:
            self.followees[followerId].remove(followeeId)


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
        print(f"{t.time} : {out}")
