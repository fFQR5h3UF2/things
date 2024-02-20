// Submission title: Design Graph With Shortest Path Calculator
// Submission url  : https://leetcode.com/problems/design-graph-with-shortest-path-calculator/description/
// Submission url  : https://leetcode.com/submissions/detail/1096509677/"

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
