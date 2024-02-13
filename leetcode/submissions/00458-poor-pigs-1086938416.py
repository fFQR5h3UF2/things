# Submission title: Poor Pigs
# Submission url  : https://leetcode.com/problems/poor-pigs/description/
# Submission url  : https://leetcode.com/submissions/detail/1086938416/
# Submission json : {"id":1086938416,"status_display":"Accepted","lang":"python3","question_id":458,"title_slug":"poor-pigs","code":"class Solution:\n    def poorPigs(self, buckets: int, a: int, b: int) -> int:\n        pigs = 0\n        while (b / a + 1) ** pigs < buckets:\n            pigs += 1\n\n        return pigs ","title":"Poor Pigs","url":"/submissions/detail/1086938416/","lang_name":"Python3","time":"3 months, 1 week","timestamp":1698597392,"status":10,"runtime":"30 ms","is_pending":"Not Pending","memory":"16.3 MB","compare_result":"111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def poorPigs(self, buckets: int, a: int, b: int) -> int:
        pigs = 0
        while (b / a + 1) ** pigs < buckets:
            pigs += 1

        return pigs
