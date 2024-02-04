# Submission for Unique Number of Occurrences
# Submission url: https://leetcode.com/submissions/detail/1148942931/


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = defaultdict(int)
        for num in arr:
            counts[num] += 1

        viewed = set()
        for _, count in counts.items():
            if count in viewed:
                return False
            viewed.add(count)
        return True
