# Submission title: Longest Common Subsequence
# Submission url  : https://leetcode.com/problems/longest-common-subsequence/description/
# Submission url  : https://leetcode.com/submissions/detail/1156538677/
# Submission json : {"id":1156538677,"status_display":"Accepted","lang":"python3","question_id":1250,"title_slug":"longest-common-subsequence","code":"class Solution:\n    def longestCommonSubsequence(self, text1: str, text2: str) -> int:\n        # Get the lengths of both input strings\n        len_text1, len_text2 = len(text1), len(text2)\n      \n        # Initialize a 2D array (list of lists) with zeros for dynamic programming\n        # The array has (len_text1 + 1) rows and (len_text2 + 1) columns\n        dp_matrix = [[0] * (len_text2 + 1) for _ in range(len_text1 + 1)]\n      \n        # Loop through each character index of text1 and text2\n        for i in range(1, len_text1 + 1):\n            for j in range(1, len_text2 + 1):\n                # If the characters match, take the diagonal value and add 1\n                if text1[i - 1] == text2[j - 1]:\n                    dp_matrix[i][j] = dp_matrix[i - 1][j - 1] + 1\n                else:\n                    # If the characters do not match, take the maximum of the value from the left and above\n                    dp_matrix[i][j] = max(dp_matrix[i - 1][j], dp_matrix[i][j - 1])\n      \n        # The bottom-right value in the matrix contains the length of the longest common subsequence\n        return dp_matrix[len_text1][len_text2]","title":"Longest Common Subsequence","url":"/submissions/detail/1156538677/","lang_name":"Python3","time":"1 week, 3 days","timestamp":1706193082,"status":10,"runtime":"479 ms","is_pending":"Not Pending","memory":"41.9 MB","compare_result":"11111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Get the lengths of both input strings
        len_text1, len_text2 = len(text1), len(text2)

        # Initialize a 2D array (list of lists) with zeros for dynamic programming
        # The array has (len_text1 + 1) rows and (len_text2 + 1) columns
        dp_matrix = [[0] * (len_text2 + 1) for _ in range(len_text1 + 1)]

        # Loop through each character index of text1 and text2
        for i in range(1, len_text1 + 1):
            for j in range(1, len_text2 + 1):
                # If the characters match, take the diagonal value and add 1
                if text1[i - 1] == text2[j - 1]:
                    dp_matrix[i][j] = dp_matrix[i - 1][j - 1] + 1
                else:
                    # If the characters do not match, take the maximum of the value from the left and above
                    dp_matrix[i][j] = max(dp_matrix[i - 1][j], dp_matrix[i][j - 1])

        # The bottom-right value in the matrix contains the length of the longest common subsequence
        return dp_matrix[len_text1][len_text2]
