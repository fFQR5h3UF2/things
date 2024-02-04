# Submission for Minimum Deletions to Make Character Frequencies Unique
# Submission url: https://leetcode.com/submissions/detail/1047264287/


class Solution:
    def minDeletions(self, s: str) -> int:
        length = len(s)
        char_count = Counter(s)
        counts = set()
        deleted_chars = 0

        for char, count in char_count.items():
            if count == 0:
                continue
            while count in counts:
                count -= 1
                deleted_chars += 1
            counts.add(count)

        return deleted_chars
