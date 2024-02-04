# Submission title: for Evaluate Division
# Submission url  : https://leetcode.com/submissions/detail/1037088395/
# Submission json : {"id": 1037088395, "status_display": "Accepted", "lang": "python3", "question_id": 399, "title_slug": "evaluate-division", "code": "class Solution:\n    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:\n        equations_count = len(equations)\n        queries_count = len(queries) \n        edges = defaultdict(dict)\n        seen_nodes = set()\n        invalid = -1.0\n\n        def dfs(val1: str, val2: str) -> float:\n            if val1 == val2:\n                return 1.0\n\n            if val2 in edges[val1]:\n                return edges[val1][val2]\n\n            if val1 in seen_nodes:\n                return invalid\n\n            seen_nodes.add(val1)\n\n            for connected_node in edges[val1]:\n                new_edge_res = dfs(connected_node, val2)\n                if new_edge_res == invalid:\n                    continue\n                new_edge_res *= edges[val1][connected_node]\n                edges[val1][val2] = new_edge_res\n                return new_edge_res\n            \n            return invalid\n\n        for i in range(equations_count):\n            (val1, val2), res = equations[i], values[i]\n            edges[val1][val2], edges[val2][val1] = res, 1 / res\n        \n        for i in range(queries_count):\n            res, (val1, val2) = -1, queries[i]\n            if val1 in edges and val2 in edges:\n                seen_nodes.clear()\n                res = dfs(val1, val2)\n            queries[i] = res\n\n        return queries", "title": "Evaluate Division", "url": "/submissions/detail/1037088395/", "lang_name": "Python3", "time": "5\u00a0months", "timestamp": 1693509297, "status": 10, "runtime": "39 ms", "is_pending": "Not Pending", "memory": "16.3 MB", "compare_result": "1111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        equations_count = len(equations)
        queries_count = len(queries)
        edges = defaultdict(dict)
        seen_nodes = set()
        invalid = -1.0

        def dfs(val1: str, val2: str) -> float:
            if val1 == val2:
                return 1.0

            if val2 in edges[val1]:
                return edges[val1][val2]

            if val1 in seen_nodes:
                return invalid

            seen_nodes.add(val1)

            for connected_node in edges[val1]:
                new_edge_res = dfs(connected_node, val2)
                if new_edge_res == invalid:
                    continue
                new_edge_res *= edges[val1][connected_node]
                edges[val1][val2] = new_edge_res
                return new_edge_res

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
