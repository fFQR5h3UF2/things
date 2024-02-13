# Submission title: Majority Element II
# Submission url  : https://leetcode.com/problems/majority-element-ii/description/
# Submission url  : https://leetcode.com/submissions/detail/1067493121/
# Submission json : {"id":1067493121,"status_display":"Accepted","lang":"python3","question_id":229,"title_slug":"majority-element-ii","code":"class Solution:\n    def majorityElement(self, nums: List[int]) -> List[int]:\n        nums.sort()\n        threshold = len(nums) // 3\n        cur_num, cur_count = nums[0], 1\n        answer = []\n        for num in nums[1:]:\n            if num == cur_num:\n                cur_count += 1\n                continue\n            if cur_count > threshold:\n                answer.append(cur_num)\n            cur_num, cur_count = num, 1\n        if cur_count > threshold:\n            answer.append(cur_num)\n        return answer","title":"Majority Element II","url":"/submissions/detail/1067493121/","lang_name":"Python3","time":"4 months","timestamp":1696488396,"status":10,"runtime":"105 ms","is_pending":"Not Pending","memory":"17.8 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


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
