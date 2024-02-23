# Submission title: Two Sum II - Input Array Is Sorted
# Submission url  : https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
# Submission url  : https://leetcode.com/submissions/detail/997606579/"


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers_map: Dict[str, int] = {}

        for i, number in enumerate(numbers):
            diff = target - number
            if diff in numbers_map:
                return [numbers_map[diff] + 1, i + 1]
            numbers_map[number] = i

        return []
