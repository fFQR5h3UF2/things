# Submission title: Number of Employees Who Met the Target
# Submission url  : https://leetcode.com/problems/number-of-employees-who-met-the-target/description/
# Submission url  : https://leetcode.com/submissions/detail/1009461517/
# Submission json : {"id":1009461517,"status_display":"Accepted","lang":"python3","question_id":2876,"title_slug":"number-of-employees-who-met-the-target","code":"class Solution:\n    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:\n        count = 0\n        for hour in hours:\n            if hour < target:\n                continue\n            count += 1\n        \n        return count","title":"Number of Employees Who Met the Target","url":"/submissions/detail/1009461517/","lang_name":"Python3","time":"6 months, 1 week","timestamp":1690901535,"status":10,"runtime":"58 ms","is_pending":"Not Pending","memory":"16.2 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0
        for hour in hours:
            if hour < target:
                continue
            count += 1

        return count
