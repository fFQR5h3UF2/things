# Submission for Reorganize String
# Submission url: https://leetcode.com/submissions/detail/1029413306/


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
            return "".join(counter.keys())

        char_order = sorted(counter.keys(), key=lambda key: counter[key])

        result = []
        left, right = char_count - 2, char_count - 1
        right_first = True
        while left >= 0 and right >= 0:
            left_char, right_char = char_order[left], char_order[right]
            left_left, right_left = counter[left_char], counter[right_char]

            if left_left and right_left:
                result.extend(
                    (right_char, left_char) if right_first else (left_char, right_char)
                )
                counter[left_char] -= 1
                counter[right_char] -= 1
                continue

            if not left_left:
                left -= 1
                continue

            if not right_left:
                right = left
                left -= 1
                right_first = not right_first
                continue

        if right >= 0:
            right_char = char_order[right]
            right_left = counter[right_char]
            if right_left > 1:
                return ""

            if right_left == 1 and right_char != result[-1]:
                result.append(right_char)
            elif right_left == 1 and right_char != result[0]:
                result.insert(0, right_char)

        if left >= 0:
            left_char = char_order[left]
            left_left = counter[left_char]
            if left_left > 1:
                return ""
            if left_left == 1 and left_char != result[-1]:
                result.append(right_char)
            elif left_left == 1 and left_char != result[0]:
                result.insert(0, left_char)

        return "".join(result)
