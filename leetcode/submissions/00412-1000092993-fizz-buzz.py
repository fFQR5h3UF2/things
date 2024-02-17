# Submission title: Fizz Buzz
# Submission url  : https://leetcode.com/problems/fizz-buzz/description/"
# Submission url  : https://leetcode.com/submissions/detail/1000092993/"


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []

        for i in range(1, n + 1):
            div_by_3, div_by_5 = i % 3 == 0, i % 5 == 0
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
