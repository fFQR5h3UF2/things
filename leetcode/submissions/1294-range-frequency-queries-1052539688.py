# Submission for Range Frequency Queries
# Submission url: https://leetcode.com/submissions/detail/1052539688/


class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.freq = {num: [0] for num in arr}
        self.freq[arr[0]][0] = 1
        for arr_val in arr[1:]:
            for num, cur_freq in self.freq.items():
                cur_freq.append(cur_freq[-1] + (1 if arr_val == num else 0))

    def query(self, left: int, right: int, value: int) -> int:
        freqs = self.freq[value]
        print(left, right, value, self.freq[value])
        return freqs[right] - (freqs[left - 1] if left > 0 else 0)


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
