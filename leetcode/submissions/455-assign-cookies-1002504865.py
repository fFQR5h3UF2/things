# Submission for Assign Cookies
# Submission url: https://leetcode.com/submissions/detail/1002504865/


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        count = 0
        cookie_index = 0
        cookie_count = len(s)
        for greed in g:
            if cookie_index < cookie_count and greed > s[cookie_index]:
                continue

            count += 1
            cookie_index += 1

        return count
