# Submission for Evaluate Division
# Submission url: https://leetcode.com/submissions/detail/1037085765/


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        equations_count = len(equations)
        queries_count = len(queries)
        edges = defaultdict(dict)
        seen_nodes = set()
        invalid = -1.0

        @cache
        def dfs(val1: str, val2: str) -> float:
            if val1 == val2:
                return 1.0

            if val2 in edges[val1]:
                return edges[val1][val2]

            if val1 in seen_nodes:
                return invalid

            seen_nodes.add(val1)

            for edge in edges[val1]:
                found_path = dfs(edge, val2)
                if found_path != invalid:
                    return edges[val1][edge] * found_path

            return invalid

        for i in range(equations_count):
            (val1, val2), res = equations[i], values[i]
            edges[val1][val2], edges[val2][val1] = res, 1 / res

        for i in range(queries_count):
            res, (val1, val2) = -1, queries[i]
            if val1 in edges and val2 in edges:
                seen_nodes.clear()
                res = dfs(val1, val2)
            queries[i] = res

        return queries
