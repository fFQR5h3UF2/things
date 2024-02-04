# Submission title: for Tweet Counts Per Frequency
# Submission url  : https://leetcode.com/submissions/detail/1047631211/
# Submission json : {"id": 1047631211, "status_display": "Accepted", "lang": "python3", "question_id": 1470, "title_slug": "tweet-counts-per-frequency", "code": "class TweetCounts:\n\n    def __init__(self):\n        self._tweets = defaultdict(list)\n        self._chunk_ranges = {\n            \"minute\": 60, \n            \"hour\": 3600, \n            \"day\": 86400\n        }\n\n    def recordTweet(self, tweetName: str, time: int) -> None:\n        self._tweets[tweetName].append(time)\n\n    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:\n        chunk_range = self._chunk_ranges[freq]\n        chunks = [0] * (1 + (endTime - startTime) // chunk_range)\n\n        for tweet in self._tweets[tweetName]:\n            if not startTime <= tweet <= endTime:\n                continue\n            chunks[(tweet - startTime) // chunk_range] += 1\n        \n        return chunks\n\n\n\n\n# Your TweetCounts object will be instantiated and called as such:\n# obj = TweetCounts()\n# obj.recordTweet(tweetName,time)\n# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)", "title": "Tweet Counts Per Frequency", "url": "/submissions/detail/1047631211/", "lang_name": "Python3", "time": "4\u00a0months, 3\u00a0weeks", "timestamp": 1694536595, "status": 10, "runtime": "318 ms", "is_pending": "Not Pending", "memory": "22.2 MB", "compare_result": "1111111111111111111111", "has_notes": false, "flag_type": 1}


class TweetCounts:

    def __init__(self):
        self._tweets = defaultdict(list)
        self._chunk_ranges = {"minute": 60, "hour": 3600, "day": 86400}

    def recordTweet(self, tweetName: str, time: int) -> None:
        self._tweets[tweetName].append(time)

    def getTweetCountsPerFrequency(
        self, freq: str, tweetName: str, startTime: int, endTime: int
    ) -> List[int]:
        chunk_range = self._chunk_ranges[freq]
        chunks = [0] * (1 + (endTime - startTime) // chunk_range)

        for tweet in self._tweets[tweetName]:
            if not startTime <= tweet <= endTime:
                continue
            chunks[(tweet - startTime) // chunk_range] += 1

        return chunks


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
