# Submission for Maximum Length of a Concatenated String with Unique Characters
# Submission url: https://leetcode.com/submissions/detail/1154367641/


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        cur = []
        cur_chars = set()
        cur_length = 0
        length = len(arr)
        max_length = 0

        def backtrack(start: int) -> None:
            nonlocal max_length
            nonlocal cur_length
            if start == length:
                max_length = max(max_length, cur_length)
                return

            for i in range(start, length):
                subs = arr[i]
                if cur_chars.intersection(subs):
                    continue
                cur.append(subs)
                cur_chars.update(subs)
                cur_length += len(subs)
                backtrack(i + 1)
                cur_length -= len(subs)
                cur.pop()
                cur_chars.difference_update(subs)

        backtrack(0)

        return max_length
