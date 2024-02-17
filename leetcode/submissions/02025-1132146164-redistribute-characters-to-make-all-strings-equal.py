# Submission title: Redistribute Characters to Make All Strings Equal
# Submission url  : https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/description/"
# Submission url  : https://leetcode.com/submissions/detail/1132146164/"


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counts = defaultdict(int)
        for word in words:
            for c in word:
                counts[c] += 1

        n = len(words)
        for val in counts.values():
            if val % n != 0:
                return False

        return True
