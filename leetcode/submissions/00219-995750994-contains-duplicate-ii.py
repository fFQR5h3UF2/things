# Submission title: Contains Duplicate II
# Submission url  : https://leetcode.com/problems/contains-duplicate-ii/description/"
# Submission url  : https://leetcode.com/submissions/detail/995750994/"


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indexes = {}
        for i, number in enumerate(nums):
            if number in indexes and abs(i - indexes[number]) <= k:
                return True
            indexes[number] = i
        return False
