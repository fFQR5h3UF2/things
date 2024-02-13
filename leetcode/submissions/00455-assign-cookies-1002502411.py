# Submission title: Assign Cookies
# Submission url  : https://leetcode.com/problems/assign-cookies/description/
# Submission url  : https://leetcode.com/submissions/detail/1002502411/
# Submission json : {"id":1002502411,"status_display":"Accepted","lang":"python3","question_id":455,"title_slug":"assign-cookies","code":"class Solution:\n    def findContentChildren(self, g: List[int], s: List[int]) -> int:\n        greed = 0\n        g.sort(reverse=True)\n        s.sort(reverse=True)\n        children_count = len(g)\n        count = 0\n        for cookie_size in s:\n            while greed < children_count and g[greed] > cookie_size:\n                greed += 1\n            \n            if greed >= children_count:\n                break\n\n            count += 1\n            greed += 1\n            \n        return count","title":"Assign Cookies","url":"/submissions/detail/1002502411/","lang_name":"Python3","time":"6 months, 2 weeks","timestamp":1690191603,"status":10,"runtime":"173 ms","is_pending":"Not Pending","memory":"18.2 MB","compare_result":"111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        greed = 0
        g.sort(reverse=True)
        s.sort(reverse=True)
        children_count = len(g)
        count = 0
        for cookie_size in s:
            while greed < children_count and g[greed] > cookie_size:
                greed += 1

            if greed >= children_count:
                break

            count += 1
            greed += 1

        return count
