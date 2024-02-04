// Submission title: for Bus Routes
// Submission url  : https://leetcode.com/submissions/detail/1097144778/
// Submission json : {"id": 1097144778, "status_display": "Accepted", "lang": "cpp", "question_id": 833, "title_slug": "bus-routes", "code": "class Solution {\npublic:\n    int numBusesToDestination(vector<vector<int>>& routes, int source, int target) {\n        if (source == target) {\n            return 0;\n        }\n\n        unordered_map<int, vector<int>> adjList;\n        // Create a map from the bus stop to all the routes that include this stop.\n        for (int route = 0; route < routes.size(); route++) {\n            for (auto stop : routes[route]) {\n                // Add all the routes that have this stop.\n                adjList[stop].push_back(route);\n            }\n        }\n\n        queue<int> q;\n        unordered_set<int> vis;\n        // Insert all the routes in the queue that have the source stop.\n        for (auto route : adjList[source]){\n            q.push(route);\n            vis.insert(route);\n        }\n\n        int busCount = 1;\n        while (q.size()) {\n            int size = q.size();\n\n            for (int i = 0; i < size; i++) {\n                int route = q.front(); q.pop();\n\n                // Iterate over the stops in the current route.\n                for (auto stop: routes[route]) {\n                    // Return the current count if the target is found.\n                    if (stop == target) {\n                        return busCount;\n                    }\n\n                    // Iterate over the next possible routes from the current stop.\n                    for (auto nextRoute : adjList[stop]) {\n                        if (!vis.count(nextRoute)) {\n                            vis.insert(nextRoute);\n                            q.push(nextRoute);\n                        }\n                    }\n                }\n            }\n            busCount++;\n        }\n        return -1;\n    }\n};", "title": "Bus Routes", "url": "/submissions/detail/1097144778/", "lang_name": "C++", "time": "2\u00a0months, 3\u00a0weeks", "timestamp": 1699778425, "status": 10, "runtime": "687 ms", "is_pending": "Not Pending", "memory": "55.5 MB", "compare_result": "1111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}



class Solution {
public:
    int numBusesToDestination(vector<vector<int>>& routes, int source, int target) {
        if (source == target) {
            return 0;
        }

        unordered_map<int, vector<int>> adjList;
        // Create a map from the bus stop to all the routes that include this stop.
        for (int route = 0; route < routes.size(); route++) {
            for (auto stop : routes[route]) {
                // Add all the routes that have this stop.
                adjList[stop].push_back(route);
            }
        }

        queue<int> q;
        unordered_set<int> vis;
        // Insert all the routes in the queue that have the source stop.
        for (auto route : adjList[source]){
            q.push(route);
            vis.insert(route);
        }

        int busCount = 1;
        while (q.size()) {
            int size = q.size();

            for (int i = 0; i < size; i++) {
                int route = q.front(); q.pop();

                // Iterate over the stops in the current route.
                for (auto stop: routes[route]) {
                    // Return the current count if the target is found.
                    if (stop == target) {
                        return busCount;
                    }

                    // Iterate over the next possible routes from the current stop.
                    for (auto nextRoute : adjList[stop]) {
                        if (!vis.count(nextRoute)) {
                            vis.insert(nextRoute);
                            q.push(nextRoute);
                        }
                    }
                }
            }
            busCount++;
        }
        return -1;
    }
};
