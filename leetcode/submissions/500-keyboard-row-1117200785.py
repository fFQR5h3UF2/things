# Submission for 'Keyboard Row'
# Submission url: https://leetcode.com/submissions/detail/1117200785/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        rows = [
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm")
        ]
        for word in words:
            for row in rows:
                if len(row.union(word.lower())) == len(row):
                    ans.append(word)
                    break
        return ans
