# Submission title: Majority Element II
# Submission url  : https://leetcode.com/problems/majority-element-ii/description/"
# Submission url  : https://leetcode.com/submissions/detail/1067493121/"


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        threshold = len(nums) // 3
        cur_num, cur_count = nums[0], 1
        answer = []
        for num in nums[1:]:
            if num == cur_num:
                cur_count += 1
                continue
            if cur_count > threshold:
                answer.append(cur_num)
            cur_num, cur_count = num, 1
        if cur_count > threshold:
            answer.append(cur_num)
        return answer
