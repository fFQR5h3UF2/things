# Submission for Sliding Window Maximum
# Submission url: https://leetcode.com/submissions/detail/1022833447/


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        nums_count = len(nums)
        if nums_count <= k:
            return [sum(nums)]

        result = [max(nums[:k])]
        counter = {}

        for num in nums[:k]:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1

        for i in range(k, nums_count):
            new_num = nums[i]
            remove_num = nums[i - k]

            if counter[remove_num] > 1:
                counter[remove_num] -= 1
            else:
                counter.pop(remove_num)

            if new_num in counter:
                counter[new_num] += 1
            else:
                counter[new_num] = 1

            result.append(max(counter.keys()))

        return result
