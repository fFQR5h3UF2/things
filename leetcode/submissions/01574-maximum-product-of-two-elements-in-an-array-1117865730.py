# Submission title: Maximum Product of Two Elements in an Array
# Submission url  : https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/description/
# Submission url  : https://leetcode.com/submissions/detail/1117865730/
# Submission json : {"id":1117865730,"status_display":"Accepted","lang":"python3","question_id":1574,"title_slug":"maximum-product-of-two-elements-in-an-array","code":"class Solution:\n    def maxProduct(self, nums: List[int]) -> int:\n        biggest = 0\n        second_biggest = 0\n        for num in nums:\n            if num > biggest:\n                second_biggest = biggest\n                biggest = num\n            else:\n                second_biggest = max(second_biggest, num)\n        \n        return (biggest - 1) * (second_biggest - 1)","title":"Maximum Product of Two Elements in an Array","url":"/submissions/detail/1117865730/","lang_name":"Python3","time":"1 month, 3 weeks","timestamp":1702366785,"status":10,"runtime":"59 ms","is_pending":"Not Pending","memory":"16.4 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        biggest = 0
        second_biggest = 0
        for num in nums:
            if num > biggest:
                second_biggest = biggest
                biggest = num
            else:
                second_biggest = max(second_biggest, num)

        return (biggest - 1) * (second_biggest - 1)
