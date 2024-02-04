# Submission for Reorganize String
# Submission url: https://leetcode.com/submissions/detail/1029304778/


class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = defaultdict(int)
        for char in s:
            counter[char] += 1

        result = []

        for char, count in counter.items():
            if count == 0:
                continue
            if result and result[-1] == char:
                return ""
            result.append(char)
            counter[char] -= 1

        return "".join(result)
