# Submission title: Add Binary
# Submission url  : https://leetcode.com/problems/add-binary/description/
# Submission url  : https://leetcode.com/submissions/detail/1057805990/
# Submission json : {"id":1057805990,"status_display":"Accepted","lang":"python3","question_id":67,"title_slug":"add-binary","code":"class Solution:\n    def addBinary(self, a: str, b: str) -> str:\n        answer = []\n        carry = 0\n        for char1, char2 in zip_longest(reversed(a), reversed(b)):\n            num1, num2 = int(char1) if char1 else 0, int(char2) if char2 else 0\n            cur_sum = num1 + num2 + carry\n            carry = 0\n            if cur_sum > 1:\n                cur_sum -= 2\n                carry = 1\n            \n            answer.append(str(cur_sum))\n        \n        if carry:\n            answer.append(\"1\")\n\n        return \"\".join(reversed(answer))","title":"Add Binary","url":"/submissions/detail/1057805990/","lang_name":"Python3","time":"4 months, 1 week","timestamp":1695549032,"status":10,"runtime":"53 ms","is_pending":"Not Pending","memory":"16.3 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        answer = []
        carry = 0
        for char1, char2 in zip_longest(reversed(a), reversed(b)):
            num1, num2 = int(char1) if char1 else 0, int(char2) if char2 else 0
            cur_sum = num1 + num2 + carry
            carry = 0
            if cur_sum > 1:
                cur_sum -= 2
                carry = 1

            answer.append(str(cur_sum))

        if carry:
            answer.append("1")

        return "".join(reversed(answer))
