# Submission title: Sliding Window Maximum
# Submission url  : https://leetcode.com/problems/sliding-window-maximum/description/
# Submission url  : https://leetcode.com/submissions/detail/1022947511/
# Submission json : {"id":1022947511,"status_display":"Accepted","lang":"python3","question_id":239,"title_slug":"sliding-window-maximum","code":"import sortedcontainers\n\nclass Solution:\n    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:\n        nums_count = len(nums)\n        if nums_count <= k:\n            return [max(nums)]\n\n        counter = defaultdict(int)\n        elems = sortedcontainers.SortedSet()\n        \n        for num in nums[:k]:\n            counter[num] += 1\n            elems.add(num)\n        \n        result = [elems[-1]]\n        \n        for i in range(k, nums_count):\n            new_num = nums[i]\n            remove_num = nums[i-k]\n\n            counter[new_num] += 1\n            elems.add(new_num)\n\n            counter[remove_num] -= 1\n            if counter[remove_num] == 0:\n                elems.discard(remove_num)\n\n            result.append(elems[-1])\n\n        return result","title":"Sliding Window Maximum","url":"/submissions/detail/1022947511/","lang_name":"Python3","time":"5 months, 3 weeks","timestamp":1692185780,"status":10,"runtime":"2438 ms","is_pending":"Not Pending","memory":"32.9 MB","compare_result":"111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}

import sortedcontainers


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        nums_count = len(nums)
        if nums_count <= k:
            return [max(nums)]

        counter = defaultdict(int)
        elems = sortedcontainers.SortedSet()

        for num in nums[:k]:
            counter[num] += 1
            elems.add(num)

        result = [elems[-1]]

        for i in range(k, nums_count):
            new_num = nums[i]
            remove_num = nums[i - k]

            counter[new_num] += 1
            elems.add(new_num)

            counter[remove_num] -= 1
            if counter[remove_num] == 0:
                elems.discard(remove_num)

            result.append(elems[-1])

        return result
