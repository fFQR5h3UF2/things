# Submission for 'Find Consecutive Integers from a Data Stream'
# Submission url: https://leetcode.com/submissions/detail/1052587062/

class DataStream:

    def __init__(self, value: int, k: int):
        self.required, self.value, self.value_count = k, value, 0


    def consec(self, num: int) -> bool:
        if num != self.value:
            self.value_count = 0
            return False

        self.value_count += 1
        return self.value_count >= self.required


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
