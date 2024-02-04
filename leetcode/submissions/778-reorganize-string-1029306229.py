# Submission for Reorganize String
# Submission url: https://leetcode.com/submissions/detail/1029306229/


class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = defaultdict(int)
        char_count = len(s)
        for char in s:
            counter[char] += 1

        result = []
        while True:
            zero_count = 0
            for char, count in counter.items():
                if count == 0:
                    zero_count += 1
                    continue
                if result and result[-1] == char:
                    return ""
                result.append(char)
                counter[char] -= 1

            if zero_count == char_count:
                break

        return "".join(result)
