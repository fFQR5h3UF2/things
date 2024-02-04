# Submission for Constrained Subsequence Sum
# Submission url: https://leetcode.com/submissions/detail/1080533312/


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        answer, negatives = [None], deque(maxlen=len(nums))
        max_val = float("-inf")
        for i, num in enumerate(nums):
            max_val = max(max_val, num)

            if num >= 0 and answer[0] is None:
                answer[0] = num
                continue
            elif num >= 0:
                answer[0] += num
                negatives.clear()
                continue

            if answer is None:
                continue

            if len(negatives) < k - 1:
                negatives.append(num)
                continue

            negatives.append(num)
            max_negative, max_negative_idx = negatives[0], 0
            for j in range(1, k):
                negative = negatives[j]
                if negative >= max_negative:
                    max_negative, max_negative_idx = negative, j

            answer.append(max_negative)
            cur = 0
            while cur <= max_negative_idx:
                negatives.popleft()
                cur += 1

        if answer[0] is None:
            return max_val

        last_num = None
        for i in reversed(range(len(answer))):
            num = answer[i]
            if num > 0:
                last_num = i
                break

        return sum(answer[0 : last_num + 1])
