# Submission title: Maximum Length of a Concatenated String with Unique Characters
# Submission url  : https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description/
# Submission url  : https://leetcode.com/submissions/detail/1154381353/"


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        cur = set()
        length = len(arr)
        max_length = 0

        def backtrack(start: int) -> None:
            nonlocal max_length

            for i in range(start, length):
                new_subs = arr[i]
                new = set(new_subs)
                if len(new_subs) != len(new) or len(cur.intersection(new)) != 0:
                    continue
                cur.update(new)
                backtrack(i + 1)
                cur.difference_update(new)

            max_length = max(max_length, len(cur))

        backtrack(0)

        return max_length
