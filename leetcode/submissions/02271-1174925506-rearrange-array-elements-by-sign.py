# Submission title: Rearrange Array Elements by Sign
# Submission url  : https://leetcode.com/problems/rearrange-array-elements-by-sign/description/"
# Submission url  : https://leetcode.com/submissions/detail/1174925506/"


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = []
        pos, neg = [], []
        length = len(nums)
        for i in range(length):
            num = nums[i]
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)
        pos.reverse()
        neg.reverse()
        while pos and neg:
            res.extend((pos.pop(), neg.pop()))
        return res
