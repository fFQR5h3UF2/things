# Submission title: for Element Appearing More Than 25% In Sorted Array
# Submission url  : https://leetcode.com/submissions/detail/1117030857/
# Submission json : {"id": 1117030857, "status_display": "Accepted", "lang": "python3", "question_id": 1221, "title_slug": "element-appearing-more-than-25-in-sorted-array", "code": "class Solution:\n    def findSpecialInteger(self, arr: List[int]) -> int:\n        prev, count = arr[0], 1\n        quarter = len(arr) / 4\n        for num in arr[1:]:\n            if num == prev:\n                count += 1\n            else:\n                prev = num\n                count = 1\n            if count > quarter:\n                break\n        return prev", "title": "Element Appearing More Than 25% In Sorted Array", "url": "/submissions/detail/1117030857/", "lang_name": "Python3", "time": "1\u00a0month, 3\u00a0weeks", "timestamp": 1702279615, "status": 10, "runtime": "87 ms", "is_pending": "Not Pending", "memory": "17.6 MB", "compare_result": "1111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        prev, count = arr[0], 1
        quarter = len(arr) / 4
        for num in arr[1:]:
            if num == prev:
                count += 1
            else:
                prev = num
                count = 1
            if count > quarter:
                break
        return prev
