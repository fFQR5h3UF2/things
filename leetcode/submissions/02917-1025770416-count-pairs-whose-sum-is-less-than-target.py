# Submission title: Count Pairs Whose Sum is Less than Target
# Submission url  : https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description/"
# Submission url  : https://leetcode.com/submissions/detail/1025770416/"


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        pairs_count = 0
        nums_count = len(nums)
        for i in range(nums_count):
            num1 = nums[i]
            for j in range(i + 1, nums_count):
                if num1 + nums[j] < target:
                    pairs_count += 1

        return pairs_count
