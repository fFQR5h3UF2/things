# Submission title: Find the Duplicate Number
# Submission url  : https://leetcode.com/problems/find-the-duplicate-number/description/
# Submission url  : https://leetcode.com/submissions/detail/1053766402/
# Submission json : {"id":1053766402,"status_display":"Accepted","lang":"python3","question_id":287,"title_slug":"find-the-duplicate-number","code":"class Solution:\n    def findDuplicate(self, nums: List[int]) -> int:\n        freqs = [0] * (10**5 + 1)\n        for num in nums:\n            freqs[num] += 1\n            if freqs[num] > 1:\n                return num\n\n        raise Exception()","title":"Find the Duplicate Number","url":"/submissions/detail/1053766402/","lang_name":"Python3","time":"4 months, 2 weeks","timestamp":1695142716,"status":10,"runtime":"486 ms","is_pending":"Not Pending","memory":"30.8 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freqs = [0] * (10**5 + 1)
        for num in nums:
            freqs[num] += 1
            if freqs[num] > 1:
                return num

        raise Exception()
