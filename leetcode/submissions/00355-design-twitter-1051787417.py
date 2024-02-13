# Submission title: Design Twitter
# Submission url  : https://leetcode.com/problems/design-twitter/description/
# Submission url  : https://leetcode.com/submissions/detail/1051787417/
# Submission json : {"id":1051787417,"status_display":"Accepted","lang":"python3","question_id":355,"title_slug":"design-twitter","code":"class Twitter:\n\n    def __init__(self):\n        self.tweets = []\n        self.following = defaultdict(set)\n\n    def postTweet(self, userId: int, tweetId: int) -> None:\n        self.tweets.append((userId, tweetId))\n\n    def getNewsFeed(self, userId: int) -> List[int]:\n        tweets, following = [], self.following[userId]\n        for poster, tweet in reversed(self.tweets):\n            if poster != userId and poster not in following:\n                continue\n            tweets.append(tweet)\n            if len(tweets) == 10:\n                break\n            \n        return tweets\n\n    def follow(self, followerId: int, followeeId: int) -> None:\n        self.following[followerId].add(followeeId)\n\n    def unfollow(self, followerId: int, followeeId: int) -> None:\n        self.following[followerId].discard(followeeId)\n\n# Your Twitter object will be instantiated and called as such:\n# obj = Twitter()\n# obj.postTweet(userId,tweetId)\n# param_2 = obj.getNewsFeed(userId)\n# obj.follow(followerId,followeeId)\n# obj.unfollow(followerId,followeeId)","title":"Design Twitter","url":"/submissions/detail/1051787417/","lang_name":"Python3","time":"4 months, 2 weeks","timestamp":1694956091,"status":10,"runtime":"38 ms","is_pending":"Not Pending","memory":"16.3 MB","compare_result":"1111111111111111","has_notes":false,"flag_type":1}


class Twitter:

    def __init__(self):
        self.tweets = []
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets, following = [], self.following[userId]
        for poster, tweet in reversed(self.tweets):
            if poster != userId and poster not in following:
                continue
            tweets.append(tweet)
            if len(tweets) == 10:
                break

        return tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
