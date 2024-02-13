// Submission title: Design Graph With Shortest Path Calculator
// Submission url  : https://leetcode.com/problems/design-graph-with-shortest-path-calculator/description/
// Submission url  : https://leetcode.com/submissions/detail/1096509677/
// Submission json : {"id":1096509677,"status_display":"Accepted","lang":"cpp","question_id":2678,"title_slug":"design-graph-with-shortest-path-calculator","code":"class Graph {\npublic:\n    vector<vector<pair<int, int>>> adjList;\n    Graph(int n, vector<vector<int>>& edges) {\n        adjList.resize(n);\n        for (auto& e: edges)\n            adjList[e[0]].push_back(make_pair(e[1], e[2]));\n    }\n\n    void addEdge(vector<int> edge) {\n        adjList[edge[0]].push_back(make_pair(edge[1], edge[2]));\n    }\n\n    int shortestPath(int node1, int node2) {\n        int n = adjList.size();\n        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;\n        vector<int> costForNode(n, INT_MAX);\n        costForNode[node1] = 0;\n        pq.push({0, node1});\n\n        while (!pq.empty()) {\n            int currCost = pq.top()[0];\n            int currNode = pq.top()[1];\n            pq.pop();\n\n            if (currCost > costForNode[currNode]) {\n                continue;\n            }\n            if (currNode == node2) {\n                return currCost;\n            }\n            for (auto& neighbor : adjList[currNode]) {\n                int neighborNode = neighbor.first;\n                int cost = neighbor.second;\n                int newCost = currCost + cost;\n\n                if (newCost < costForNode[neighborNode]) {\n                    costForNode[neighborNode] = newCost;\n                    pq.push({newCost, neighborNode});\n                }\n            }\n        }\n        return -1;\n    }\n};","title":"Design Graph With Shortest Path Calculator","url":"/submissions/detail/1096509677/","lang_name":"C++","time":"2 months, 3 weeks","timestamp":1699703469,"status":10,"runtime":"344 ms","is_pending":"Not Pending","memory":"113 MB","compare_result":"111111111111111111111111111111111111","has_notes":false,"flag_type":1}

class Graph {
public:
    vector<vector<pair<int, int>>> adjList;
    Graph(int n, vector<vector<int>>& edges) {
        adjList.resize(n);
        for (auto& e: edges)
            adjList[e[0]].push_back(make_pair(e[1], e[2]));
    }

    void addEdge(vector<int> edge) {
        adjList[edge[0]].push_back(make_pair(edge[1], edge[2]));
    }

    int shortestPath(int node1, int node2) {
        int n = adjList.size();
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
        vector<int> costForNode(n, INT_MAX);
        costForNode[node1] = 0;
        pq.push({0, node1});

        while (!pq.empty()) {
            int currCost = pq.top()[0];
            int currNode = pq.top()[1];
            pq.pop();

            if (currCost > costForNode[currNode]) {
                continue;
            }
            if (currNode == node2) {
                return currCost;
            }
            for (auto& neighbor : adjList[currNode]) {
                int neighborNode = neighbor.first;
                int cost = neighbor.second;
                int newCost = currCost + cost;

                if (newCost < costForNode[neighborNode]) {
                    costForNode[neighborNode] = newCost;
                    pq.push({newCost, neighborNode});
                }
            }
        }
        return -1;
    }
};
