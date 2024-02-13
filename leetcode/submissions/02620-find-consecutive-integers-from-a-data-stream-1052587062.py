# Submission title: Find Consecutive Integers from a Data Stream
# Submission url  : https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/description/
# Submission url  : https://leetcode.com/submissions/detail/1052587062/
# Submission json : {"id":1052587062,"status_display":"Accepted","lang":"python3","question_id":2620,"title_slug":"find-consecutive-integers-from-a-data-stream","code":"class DataStream:\n\n    def __init__(self, value: int, k: int):\n        self.required, self.value, self.value_count = k, value, 0\n        \n\n    def consec(self, num: int) -> bool:\n        if num != self.value:\n            self.value_count = 0\n            return False\n        \n        self.value_count += 1\n        return self.value_count >= self.required\n\n\n# Your DataStream object will be instantiated and called as such:\n# obj = DataStream(value, k)\n# param_1 = obj.consec(num)","title":"Find Consecutive Integers from a Data Stream","url":"/submissions/detail/1052587062/","lang_name":"Python3","time":"4 months, 2 weeks","timestamp":1695039127,"status":10,"runtime":"412 ms","is_pending":"Not Pending","memory":"42.2 MB","compare_result":"11111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class DataStream:

    def __init__(self, value: int, k: int):
        self.required, self.value, self.value_count = k, value, 0

    def consec(self, num: int) -> bool:
        if num != self.value:
            self.value_count = 0
            return False

        self.value_count += 1
        return self.value_count >= self.required


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
