# Submission title: Keyboard Row
# Submission url  : https://leetcode.com/problems/keyboard-row/description/
# Submission url  : https://leetcode.com/submissions/detail/1117200785/
# Submission json : {"id":1117200785,"status_display":"Accepted","lang":"python3","question_id":500,"title_slug":"keyboard-row","code":"class Solution:\n    def findWords(self, words: List[str]) -> List[str]:\n        ans = []\n        rows = [\n            set(\"qwertyuiop\"),\n            set(\"asdfghjkl\"), \n            set(\"zxcvbnm\")\n        ]\n        for word in words:\n            for row in rows:\n                if len(row.union(word.lower())) == len(row):\n                    ans.append(word)\n                    break\n        return ans\n","title":"Keyboard Row","url":"/submissions/detail/1117200785/","lang_name":"Python3","time":"1 month, 3 weeks","timestamp":1702297835,"status":10,"runtime":"39 ms","is_pending":"Not Pending","memory":"16.3 MB","compare_result":"11111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        rows = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        for word in words:
            for row in rows:
                if len(row.union(word.lower())) == len(row):
                    ans.append(word)
                    break
        return ans
