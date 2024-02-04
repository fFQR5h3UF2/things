# Submission for Fizz Buzz
# Submission url: https://leetcode.com/submissions/detail/1000092409/


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []

        for i in range(n):
            div_by_3 = i > 3 and i % 3 == 0
            div_by_5 = i > 5 and i % 5 == 0
            value = None

            if div_by_3 and div_by_5:
                value = "FizzBuzz"
            elif div_by_3:
                value = "Fizz"
            elif div_by_5:
                value = "Buzz"
            else:
                value = str(i)

            result.append(value)

        return result
