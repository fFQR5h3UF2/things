# Submission title: Design an Ordered Stream
# Submission url  : https://leetcode.com/problems/design-an-ordered-stream/description/
# Submission url  : https://leetcode.com/submissions/detail/1051124372/
# Submission json : {"id":1051124372,"status_display":"Accepted","lang":"python3","question_id":1775,"title_slug":"design-an-ordered-stream","code":"class OrderedStream:\n\n    def __init__(self, n: int):\n        self.values = [None] * n\n        self.length = n\n        self.cur = 0\n\n    def insert(self, idKey: int, value: str) -> List[str]:\n        self.values[idKey - 1] = value\n        for i in range(self.cur, self.length):\n            if self.values[i] is not None:\n                continue\n            \n            self.cur, answer = i, self.values[self.cur:i]\n            return answer\n\n        return self.values[self.cur:]\n\n\n\n# Your OrderedStream object will be instantiated and called as such:\n# obj = OrderedStream(n)\n# param_1 = obj.insert(idKey,value)","title":"Design an Ordered Stream","url":"/submissions/detail/1051124372/","lang_name":"Python3","time":"4 months, 2 weeks","timestamp":1694884699,"status":10,"runtime":"251 ms","is_pending":"Not Pending","memory":"17 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class OrderedStream:

    def __init__(self, n: int):
        self.values = [None] * n
        self.length = n
        self.cur = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.values[idKey - 1] = value
        for i in range(self.cur, self.length):
            if self.values[i] is not None:
                continue

            self.cur, answer = i, self.values[self.cur : i]
            return answer

        return self.values[self.cur :]


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
