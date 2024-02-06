# Submission title: for Pascal's Triangle
# Submission url  : https://leetcode.com/submissions/detail/1043821324/
# Submission json : {"id": 1043821324, "status_display": "Accepted", "lang": "python3", "question_id": 118, "title_slug": "pascals-triangle", "code": "class Solution:\n    def generate(self, numRows: int) -> List[List[int]]:\n        answer = [[1]]\n        numRows -= 1\n\n        while numRows > 0:\n            cur, prev = [1], answer[-1]\n            for i in range(len(prev) - 1):\n                cur.append(prev[i] + prev[i+1])\n            cur.append(1)\n            answer.append(cur)\n            numRows -= 1\n        \n        return answer", "title": "Pascal's Triangle", "url": "/submissions/detail/1043821324/", "lang_name": "Python3", "time": "4\u00a0months, 4\u00a0weeks", "timestamp": 1694169669, "status": 10, "runtime": "41 ms", "is_pending": "Not Pending", "memory": "16.2 MB", "compare_result": "111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = [[1]]
        numRows -= 1

        while numRows > 0:
            cur, prev = [1], answer[-1]
            for i in range(len(prev) - 1):
                cur.append(prev[i] + prev[i + 1])
            cur.append(1)
            answer.append(cur)
            numRows -= 1

        return answer
