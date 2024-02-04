# Submission for Buddy Strings
# Submission url: https://leetcode.com/submissions/detail/1010075791/


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        length_1, length_2 = len(s), len(goal)

        if length_1 != length_2:
            return False

        swap_candidate = None
        swapped = False
        char_count = defaultdict(int)

        for i in range(length_1):
            char_1, char_2 = s[i], goal[i]
            char_count[char_1] += 1

            if char_1 == char_2:
                continue

            if swapped:
                return False

            if swap_candidate is None:
                swap_candidate = i
                continue

            if char_1 == goal[swap_candidate] and s[swap_candidate] == char_2:
                swapped = True
            else:
                return False

        return swapped or any(count > 1 for count in char_count.values())
