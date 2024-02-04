# Submission for Evaluate Division
# Submission url: https://leetcode.com/submissions/detail/1037062866/


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        equations_count = len(equations)
        queries_count = len(queries)
        edges = defaultdict(dict)
        # a = 2 b
        # c = 1 / 3 b

        @cache
        def find_value(val1: str, val2: str) -> float:
            if val1 not in edges or val2 not in edges:
                return -1.0
            if val1 == val2:
                return 1.0
            if val2 in edges[val1]:
                return edges[val1][val2]

            common_edges = edges[val1].keys() & edges[val2].keys()
            if not common_edges:
                return -1.0
            edge = common_edges.pop()
            return edges[val1][edge] / edges[val2][edge]

        for i in range(equations_count):
            (val1, val2), res = equations[i], values[i]
            edges[val1][val2], edges[val2][val1] = res, 1 / res

        for i in range(queries_count):
            queries[i] = find_value(*queries[i])

        return queries
