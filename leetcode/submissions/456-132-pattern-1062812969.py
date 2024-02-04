# Submission for 132 Pattern
# Submission url: https://leetcode.com/submissions/detail/1062812969/


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        nums_ids = defaultdict(list)
        for i, num in enumerate(nums):
            nums_ids[num].append(i)

        for i_num, i_ids in nums_ids.items():
            for k_num, k_ids in nums_ids.items():
                for j_num, j_ids in nums_ids.items():
                    if not i_num < k_num < j_num:
                        continue
                    for i_id in i_ids:
                        for k_id in reversed(k_ids):
                            if i_id > k_id:
                                break
                            for j_id in j_ids:
                                if i_id < j_id < k_id:
                                    return True
        return False
