# Submission for H-Index
# Submission url: https://leetcode.com/submissions/detail/998365043/


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations)
        length = len(citations)
        h = 0
        for i in reversed(range(length)):
            citations_count = citations[i]
            published_count = length - i
            if published_count >= citations_count and citations_count >= h:
                h = citations_count

        return h
