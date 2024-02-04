# Submission for 'Faulty Keyboard'
# Submission url: https://leetcode.com/submissions/detail/1013920579/

class Solution:
    def finalString(self, s: str) -> str:
        result = []
        for char in s:
            if char == "i":
                result.reverse()
            else:
                result.append(char)

        return "".join(result)
