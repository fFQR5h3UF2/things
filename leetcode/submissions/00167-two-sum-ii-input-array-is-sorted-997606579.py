# Submission title: Two Sum II - Input Array Is Sorted
# Submission url  : https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
# Submission url  : https://leetcode.com/submissions/detail/997606579/
# Submission json : {"id":997606579,"status_display":"Accepted","lang":"python3","question_id":167,"title_slug":"two-sum-ii-input-array-is-sorted","code":"class Solution:\n    def twoSum(self, numbers: List[int], target: int) -> List[int]:\n        numbers_map: Dict[str, int] = {}\n\n        for i, number in enumerate(numbers):\n            diff = target - number\n            if diff in numbers_map:\n                return [numbers_map[diff] + 1, i + 1]\n            numbers_map[number] = i\n        \n        return []\n","title":"Two Sum II - Input Array Is Sorted","url":"/submissions/detail/997606579/","lang_name":"Python3","time":"6 months, 3 weeks","timestamp":1689688529,"status":10,"runtime":"136 ms","is_pending":"Not Pending","memory":"17.3 MB","compare_result":"11111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers_map: Dict[str, int] = {}

        for i, number in enumerate(numbers):
            diff = target - number
            if diff in numbers_map:
                return [numbers_map[diff] + 1, i + 1]
            numbers_map[number] = i

        return []
