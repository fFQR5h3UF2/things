# Submission title: for Minimize the Maximum Difference of Pairs
# Submission url  : https://leetcode.com/submissions/detail/1016434342/
# Submission json : {"id": 1016434342, "status_display": "Accepted", "lang": "python3", "question_id": 2720, "title_slug": "minimize-the-maximum-difference-of-pairs", "code": "class Solution:\n    def minimizeMax(self, nums: List[int], p: int) -> int:\n        nums.sort()\n        nums_count = len(nums)\n        \n        # Find the number of valid pairs by greedy approach\n        def countValidPairs(threshold: int) -> int:\n            index, count = 0, 0\n            while index < nums_count - 1:\n                # If a valid pair is found, skip both numbers.\n                if nums[index + 1] - nums[index] <= threshold:\n                    count += 1\n                    index += 1\n                index += 1\n            return count\n        \n        left, right = 0, nums[-1] - nums[0]\n        while left < right:\n            mid = left + (right - left) // 2\n\n            # If there are enough pairs, look for a smaller threshold.\n            # Otherwise, look for a larger threshold.\n            if countValidPairs(mid) >= p:\n                right = mid\n            else:\n                left = mid + 1\n\n        return left       ", "title": "Minimize the Maximum Difference of Pairs", "url": "/submissions/detail/1016434342/", "lang_name": "Python3", "time": "5\u00a0months, 4\u00a0weeks", "timestamp": 1691571946, "status": 10, "runtime": "943 ms", "is_pending": "Not Pending", "memory": "30.9 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        nums_count = len(nums)

        # Find the number of valid pairs by greedy approach
        def countValidPairs(threshold: int) -> int:
            index, count = 0, 0
            while index < nums_count - 1:
                # If a valid pair is found, skip both numbers.
                if nums[index + 1] - nums[index] <= threshold:
                    count += 1
                    index += 1
                index += 1
            return count

        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = left + (right - left) // 2

            # If there are enough pairs, look for a smaller threshold.
            # Otherwise, look for a larger threshold.
            if countValidPairs(mid) >= p:
                right = mid
            else:
                left = mid + 1

        return left
