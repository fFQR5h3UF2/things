# Submission title: Count Complete Subarrays in an Array
# Submission url  : https://leetcode.com/problems/count-complete-subarrays-in-an-array/description/
# Submission url  : https://leetcode.com/submissions/detail/1009497441/
# Submission json : {"id":1009497441,"status_display":"Accepted","lang":"python3","question_id":2856,"title_slug":"count-complete-subarrays-in-an-array","code":"class Solution:\n    def countCompleteSubarrays(self, nums: List[int]) -> int:\n        length = len(nums)\n        elems_count = len(set(nums))\n        \n        if elems_count == length:\n            return 1\n        \n        if elems_count == 1:\n            return length + sum(i for i in range(1, length))\n        \n        result, elems, min_j = 0, defaultdict(int), 0\n        for i in range(length):\n            left = nums[i]\n            \n            for j in range(min_j, length):\n                right = nums[j]\n                elems[right] += 1\n                \n                if len(elems) != elems_count:\n                    continue\n                \n                if elems[right] == 1:\n                    elems.pop(right)\n                else:\n                    elems[right] -= 1 \n    \n                result += length - j\n                min_j = j\n                break\n            else:\n                return result\n            \n            if elems[left] == 1:\n                elems.pop(left)\n            else:\n                elems[left] -= 1\n                    \n        return result","title":"Count Complete Subarrays in an Array","url":"/submissions/detail/1009497441/","lang_name":"Python3","time":"6 months","timestamp":1690904342,"status":10,"runtime":"110 ms","is_pending":"Not Pending","memory":"16.5 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        length = len(nums)
        elems_count = len(set(nums))

        if elems_count == length:
            return 1

        if elems_count == 1:
            return length + sum(i for i in range(1, length))

        result, elems, min_j = 0, defaultdict(int), 0
        for i in range(length):
            left = nums[i]

            for j in range(min_j, length):
                right = nums[j]
                elems[right] += 1

                if len(elems) != elems_count:
                    continue

                if elems[right] == 1:
                    elems.pop(right)
                else:
                    elems[right] -= 1

                result += length - j
                min_j = j
                break
            else:
                return result

            if elems[left] == 1:
                elems.pop(left)
            else:
                elems[left] -= 1

        return result
