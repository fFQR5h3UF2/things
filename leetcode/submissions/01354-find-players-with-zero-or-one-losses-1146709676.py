# Submission title: Find Players With Zero or One Losses
# Submission url  : https://leetcode.com/problems/find-players-with-zero-or-one-losses/description/
# Submission url  : https://leetcode.com/submissions/detail/1146709676/
# Submission json : {"id":1146709676,"status_display":"Accepted","lang":"python3","question_id":1354,"title_slug":"find-players-with-zero-or-one-losses","code":"class Solution:\n    def findWinners(self, matches):\n        losses = [0] * 100001\n\n        for winner, loser in matches:\n            if losses[winner] == 0:\n                losses[winner] = -1\n\n            if losses[loser] == -1:\n                losses[loser] = 1\n            else:\n                losses[loser] += 1\n\n        zero_loss = [i for i in range(1, 100001) if losses[i] == -1]\n        one_loss = [i for i in range(1, 100001) if losses[i] == 1]\n\n        return [zero_loss, one_loss]","title":"Find Players With Zero or One Losses","url":"/submissions/detail/1146709676/","lang_name":"Python3","time":"2 weeks, 6 days","timestamp":1705308312,"status":10,"runtime":"1779 ms","is_pending":"Not Pending","memory":"73.9 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def findWinners(self, matches):
        losses = [0] * 100001

        for winner, loser in matches:
            if losses[winner] == 0:
                losses[winner] = -1

            if losses[loser] == -1:
                losses[loser] = 1
            else:
                losses[loser] += 1

        zero_loss = [i for i in range(1, 100001) if losses[i] == -1]
        one_loss = [i for i in range(1, 100001) if losses[i] == 1]

        return [zero_loss, one_loss]
