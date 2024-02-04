# Submission for Group the People Given the Group Size They Belong To
# Submission url: https://leetcode.com/submissions/detail/1046482817/


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        answer = []
        cur_groups = defaultdict(list)

        for i in range(len(groupSizes)):
            size = groupSizes[i]
            group = cur_groups[size]
            group.append(i)
            if len(group) == size:
                answer.append(group)
                del cur_groups[size]

        return answer
