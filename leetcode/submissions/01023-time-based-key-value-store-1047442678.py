# Submission title: Time Based Key-Value Store
# Submission url  : https://leetcode.com/problems/time-based-key-value-store/description/
# Submission url  : https://leetcode.com/submissions/detail/1047442678/
# Submission json : {"id":1047442678,"status_display":"Accepted","lang":"python3","question_id":1023,"title_slug":"time-based-key-value-store","code":"class TimeMap:\n\n    def __init__(self):\n        self._cache = defaultdict(list)\n        \n\n    def set(self, key: str, value: str, timestamp: int) -> None:\n        self._cache[key].append((timestamp, value))\n\n    def get(self, key: str, timestamp: int) -> str:\n        for cur_timestamp, value in reversed(self._cache[key]):\n            if cur_timestamp > timestamp:\n                continue\n            return value\n\n        return \"\"\n\n# Your TimeMap object will be instantiated and called as such:\n# obj = TimeMap()\n# obj.set(key,value,timestamp)\n# param_2 = obj.get(key,timestamp)","title":"Time Based Key-Value Store","url":"/submissions/detail/1047442678/","lang_name":"Python3","time":"4 months, 3 weeks","timestamp":1694522555,"status":10,"runtime":"583 ms","is_pending":"Not Pending","memory":"73.9 MB","compare_result":"11111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class TimeMap:

    def __init__(self):
        self._cache = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._cache[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        for cur_timestamp, value in reversed(self._cache[key]):
            if cur_timestamp > timestamp:
                continue
            return value

        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
