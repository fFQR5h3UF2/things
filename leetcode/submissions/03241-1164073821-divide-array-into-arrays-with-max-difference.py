# Submission title: Divide Array Into Arrays With Max Difference
# Submission url  : https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/description/"
# Submission url  : https://leetcode.com/submissions/detail/1164073821/"


class Solution:
    def divideArray(self, nums, k):
        size = len(nums)
        if size % 3 != 0:
            return []

        nums.sort()

        result = []
        group_index = 0
        for i in range(0, size, 3):
            if i + 2 < size and nums[i + 2] - nums[i] <= k:
                result.append([nums[i], nums[i + 1], nums[i + 2]])
                group_index += 1
            else:
                return []
        return result