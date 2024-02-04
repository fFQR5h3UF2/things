# Submission for Fair Distribution of Cookies
# Submission url: https://leetcode.com/submissions/detail/1005171031/


class Solution:
    # cookies = [8,8,10,15,20], [20,15], k = 2 -> 31
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        length = len(cookies)

        if length == k:
            return max(cookies)

        if k == 1:
            return sum(cookies)

        cookies = sorted(cookies)

        distributed_start = length - k
        to_distribute_start = length - (2 * k)
        if to_distribute_start < 0:
            to_distribute_start = 0

        for bag_to_add in range(0, to_distribute_start):
            smallest_bag = to_distribute_start

            for bag in range(to_distribute_start + 1, distributed_start):
                if cookies[bag] >= cookies[smallest_bag]:
                    continue

                smallest_bag = bag

            cookies[smallest_bag] += bag_to_add

        return cookies[-1] + min(cookies[bags_extra_end:bags_left_end])
