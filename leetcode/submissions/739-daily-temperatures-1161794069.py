# Submission for Daily Temperatures
# Submission url: https://leetcode.com/submissions/detail/1161794069/


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps_left = {}
        to_pop = []
        length = len(temperatures)
        ans = [0] * length
        for i in range(length):
            temp = temperatures[i]
            for temp_left, idx in temps_left.items():
                if temp > temp_left:
                    ans[idx] = i - idx
                    to_pop.append(temp_left)
            temps_left[temp] = i
            for temp in to_pop:
                temps_left.pop(temp)
            to_pop.clear()

        return ans
