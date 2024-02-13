# Submission title: Candy
# Submission url  : https://leetcode.com/problems/candy/description/
# Submission url  : https://leetcode.com/submissions/detail/1057811172/
# Submission json : {"id":1057811172,"status_display":"Accepted","lang":"python3","question_id":135,"title_slug":"candy","code":"class Solution:\n    def candy(self, ratings: List[int]) -> int:\n        child_count = len(ratings)\n        candies = [1] * child_count \n\n        for i in range(1, child_count):\n            if ratings[i] > ratings[i-1]:\n                candies[i] = candies[i-1] + 1\n\n        for i in reversed(range(child_count - 1)):\n            if ratings[i] > ratings[i+1]:\n                candies[i] = max(candies[i], candies[i+1] + 1)\n        \n        return sum(candies)","title":"Candy","url":"/submissions/detail/1057811172/","lang_name":"Python3","time":"4 months, 1 week","timestamp":1695549610,"status":10,"runtime":"136 ms","is_pending":"Not Pending","memory":"19.2 MB","compare_result":"111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def candy(self, ratings: List[int]) -> int:
        child_count = len(ratings)
        candies = [1] * child_count

        for i in range(1, child_count):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in reversed(range(child_count - 1)):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)
