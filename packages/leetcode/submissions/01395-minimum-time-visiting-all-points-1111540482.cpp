// Submission title: for Minimum Time Visiting All Points
// Submission url  : https://leetcode.com/submissions/detail/1111540482/
// Submission json : {"id": 1111540482, "status_display": "Accepted", "lang": "cpp", "question_id": 1395, "title_slug": "minimum-time-visiting-all-points", "code": "class Solution {\npublic:\n    int minTimeToVisitAllPoints(vector<vector<int>>& points) {\n        int ans = 0;\n        for (int i = 0; i < points.size() - 1; i++) {\n            int currX = points[i][0];\n            int currY = points[i][1];\n            int targetX = points[i + 1][0];\n            int targetY = points[i + 1][1];\n            ans += max(abs(targetX - currX), abs(targetY - currY));\n        }\n        \n        return ans;\n    }\n};", "title": "Minimum Time Visiting All Points", "url": "/submissions/detail/1111540482/", "lang_name": "C++", "time": "2\u00a0months", "timestamp": 1701615193, "status": 10, "runtime": "3 ms", "is_pending": "Not Pending", "memory": "10.7 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}



class Solution {
public:
    int minTimeToVisitAllPoints(vector<vector<int>>& points) {
        int ans = 0;
        for (int i = 0; i < points.size() - 1; i++) {
            int currX = points[i][0];
            int currY = points[i][1];
            int targetX = points[i + 1][0];
            int targetY = points[i + 1][1];
            ans += max(abs(targetX - currX), abs(targetY - currY));
        }

        return ans;
    }
};
