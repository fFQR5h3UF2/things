# Submission title: for Convert an Array Into a 2D Array With Conditions
# Submission url  : https://leetcode.com/submissions/detail/1134598784/
# Submission json : {"id": 1134598784, "status_display": "Accepted", "lang": "python3", "question_id": 2724, "title_slug": "convert-an-array-into-a-2d-array-with-conditions", "code": "class Solution:\n    def findMatrix(self, v: List[int]) -> List[List[int]]:\n        um = {}\n        for i in v:\n            um[i] = um.get(i, 0) + 1\n        \n        ans = []\n        while um:\n            temp = []\n            to_erase = []\n            for f, s in um.items():\n                temp.append(f)\n                s -= 1\n                if s == 0:\n                    to_erase.append(f)\n                um[f] = s\n            ans.append(temp)\n            for i in to_erase:\n                del um[i]\n        return ans\n", "title": "Convert an Array Into a 2D Array With Conditions", "url": "/submissions/detail/1134598784/", "lang_name": "Python3", "time": "1\u00a0month", "timestamp": 1704198018, "status": 10, "runtime": "66 ms", "is_pending": "Not Pending", "memory": "17.4 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def findMatrix(self, v: List[int]) -> List[List[int]]:
        um = {}
        for i in v:
            um[i] = um.get(i, 0) + 1

        ans = []
        while um:
            temp = []
            to_erase = []
            for f, s in um.items():
                temp.append(f)
                s -= 1
                if s == 0:
                    to_erase.append(f)
                um[f] = s
            ans.append(temp)
            for i in to_erase:
                del um[i]
        return ans
