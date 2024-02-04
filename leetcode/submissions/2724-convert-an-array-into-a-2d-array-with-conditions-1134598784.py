# Submission for Convert an Array Into a 2D Array With Conditions
# Submission url: https://leetcode.com/submissions/detail/1134598784/


class Solution:
    def findMatrix(self, v: List[int]) -> List[List[int]]:
        um = {}
        for i in v:
            um[i] = um.get(i, 0) + 1

        ans = []
        while um:
            temp = []
            to_erase = []
            for f, s in um.items():
                temp.append(f)
                s -= 1
                if s == 0:
                    to_erase.append(f)
                um[f] = s
            ans.append(temp)
            for i in to_erase:
                del um[i]
        return ans
