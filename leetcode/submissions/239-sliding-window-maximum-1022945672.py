# Submission for Sliding Window Maximum
# Submission url: https://leetcode.com/submissions/detail/1022945672/


import sortedcontainers


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        nums_count = len(nums)
        if nums_count <= k:
            return [max(nums)]

        counter = defaultdict(int)
        elems = sortedcontainers.SortedSet()

        for num in nums[:k]:
            counter[num] += 1
            elems.add(num)

        result = [elems[-1]]

        for i in range(k, nums_count):
            new_num = nums[i]
            remove_num = nums[i - k]

            if counter[remove_num] > 1:
                counter[remove_num] -= 1
            else:
                elems.discard(remove_num)

            counter[new_num] += 1
            elems.add(new_num)

            result.append(elems[-1])

        return result
