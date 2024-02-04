# Submission for Reorganize String
# Submission url: https://leetcode.com/submissions/detail/1029310653/


class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = defaultdict(int)
        char_count = len(s)
        for char in s:
            counter[char] += 1

        result = []
        remove_chars = set()

        while counter:
            for char, count in counter.items():
                if char in remove_chars:
                    continue
                if result and result[-1] == char:
                    return ""

                result.append(char)
                if count == 1:
                    remove_chars.add(char)
                else:
                    counter[char] -= 1

            for char in remove_chars:
                counter.pop(char)

            remove_chars.clear()

        return "".join(result)
