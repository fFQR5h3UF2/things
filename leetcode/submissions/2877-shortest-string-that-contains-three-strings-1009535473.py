# Submission for Shortest String That Contains Three Strings
# Submission url: https://leetcode.com/submissions/detail/1009535473/


class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        strings = sorted((a, b, c))
        result = strings[0]

        for string in strings[1:]:
            length = len(result)
            length_new = len(string)
            overlap_max = min(length_new, length)

            for j in range(0, overlap_max):
                overlap = overlap_max - j
                if result[-overlap:] == string[:overlap]:
                    result += string[overlap:]
                    break
            else:
                result += string

        return result
