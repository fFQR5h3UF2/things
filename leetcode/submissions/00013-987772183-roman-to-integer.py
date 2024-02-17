# Submission title: Roman to Integer
# Submission url  : https://leetcode.com/problems/roman-to-integer/description/"
# Submission url  : https://leetcode.com/submissions/detail/987772183/"


class Solution:
    def romanToInt(self, input_numbers: str) -> int:
        result = 0
        previous = None
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        subtractions = set(["IV", "IX", "XL", "XC", "CD", "CM"])

        for number in input_numbers:
            if f"{previous}{number}" in subtractions:
                result = result - values[previous] * 2 + values[number]
            else:
                result += values[number]
            previous = number

        return result
