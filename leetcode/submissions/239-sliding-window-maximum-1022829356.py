# Submission for Sliding Window Maximum
# Submission url: https://leetcode.com/submissions/detail/1022829356/


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        nums_count = len(nums)
        if nums_count <= k:
            return [sum(nums)]

        result = [max(nums[:k])]
        counter = defaultdict(int)

        for num in nums[:k]:
            counter[num] += 1

        for i in range(k, nums_count):
            new_num = nums[i]
            remove_num = nums[i - k]
            remove_num_count = counter[remove_num]
            counter[remove_num] = 0 if remove_num_count < 1 else remove_num_count - 1
            counter[new_num] += 1
            result.append(max(counter.keys()))

        return result
