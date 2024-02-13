# Submission title: Reverse Bits
# Submission url  : https://leetcode.com/problems/reverse-bits/description/
# Submission url  : https://leetcode.com/submissions/detail/1057806200/
# Submission json : {"id":1057806200,"status_display":"Accepted","lang":"python3","question_id":190,"title_slug":"reverse-bits","code":"class Solution:\n    def reverseBits(self, n: int) -> int:\n        # Initialize the reversed number to 0\n        reversed_num = 0\n        \n        # Iterate over all 32 bits of the given number\n        for i in range(32):\n            # Left shift the reversed number by 1 and add the last bit of the given number to it\n            reversed_num = (reversed_num << 1) | (n & 1)\n            # remove the last bit from the original number\n            n >>= 1\n        \n        # Return the reversed number\n        return reversed_num\n","title":"Reverse Bits","url":"/submissions/detail/1057806200/","lang_name":"Python3","time":"4 months, 1 week","timestamp":1695549052,"status":10,"runtime":"44 ms","is_pending":"Not Pending","memory":"16.1 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def reverseBits(self, n: int) -> int:
        # Initialize the reversed number to 0
        reversed_num = 0

        # Iterate over all 32 bits of the given number
        for i in range(32):
            # Left shift the reversed number by 1 and add the last bit of the given number to it
            reversed_num = (reversed_num << 1) | (n & 1)
            # remove the last bit from the original number
            n >>= 1

        # Return the reversed number
        return reversed_num
