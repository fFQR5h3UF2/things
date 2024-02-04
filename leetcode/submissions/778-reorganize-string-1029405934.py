# Submission for Reorganize String
# Submission url: https://leetcode.com/submissions/detail/1029405934/


class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = defaultdict(int)
        length = len(s)
        max_count = 0
        for char in s:
            counter[char] += 1
            if counter[char] > max_count:
                max_count = counter[char]

        char_count = len(counter)

        if char_count == 1:
            return ""
        if max_count == 1:
            return counter.keys()

        char_order = sorted(counter.keys(), key=lambda key: counter[key])

        result = []
        left, right = char_count - 2, char_count - 1
        while left >= 0 and right >= 0:
            left_char, right_char = char_order[left], char_order[right]
            left_left, right_left = counter[left_char], counter[right_char]

            if left_left and right_left:
                result.extend((right_char, left_char))
                counter[left_char] -= 1
                counter[right_char] -= 1
                continue

            if not left_left:
                left -= 1
                continue

            if not right_left:
                right = left
                left -= 1
                continue

        if right >= 0:
            right_char = char_order[right]
            right_left = counter[right_char]
            if right_left > 1:
                return ""
            if right_left == 1:
                result.append(right_char)
        if left >= 0:
            left_char = char_order[left]
            left_left = counter[left_char]
            if left_left > 1:
                return ""
            if left_left == 1:
                result.append(left_char)

        return "".join(result)
