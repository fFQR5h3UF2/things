# Submission title: Majority Element
# Submission url  : https://leetcode.com/problems/majority-element/description/"
# Submission url  : https://leetcode.com/submissions/detail/1173047408/"


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        half = len(nums) // 2
        for num in nums:
            counter[num] += 1
            if counter[num] > half:
                return num
        raise Exception()
