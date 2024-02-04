# Submission for Tweet Counts Per Frequency
# Submission url: https://leetcode.com/submissions/detail/1047626357/


class TweetCounts:

    def __init__(self):
        self._tweets = defaultdict(list)
        self._chunk_ranges = {"minute": 59, "hour": 3599, "day": 86399}

    def recordTweet(self, tweetName: str, time: int) -> None:
        self._tweets[tweetName].append(time)

    def getTweetCountsPerFrequency(
        self, freq: str, tweetName: str, startTime: int, endTime: int
    ) -> List[int]:
        chunk_range = self._chunk_ranges[freq]
        chunks = [0] * ceil((endTime - startTime) / chunk_range)

        for tweet in self._tweets[tweetName]:
            if not startTime <= tweet <= endTime:
                continue
            chunks[(tweet - startTime) // chunk_range] += 1

        return chunks


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
