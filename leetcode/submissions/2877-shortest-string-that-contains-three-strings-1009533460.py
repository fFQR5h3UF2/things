# Submission for Shortest String That Contains Three Strings
# Submission url: https://leetcode.com/submissions/detail/1009533460/


class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        strings = sorted((a, b, c))
        result = strings[0]

        for string in strings[1:]:
            length = len(result)
            length_new = len(string)

            for j in range(0, min(length_new, length)):
                string_chars = length_new - j
                if result[-string_chars:] == string[:string_chars]:
                    result += string[string_chars:]
                    break
            else:
                result += string

        return result
