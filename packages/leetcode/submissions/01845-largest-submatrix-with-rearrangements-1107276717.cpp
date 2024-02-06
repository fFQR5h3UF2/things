// Submission title: for Largest Submatrix With Rearrangements
// Submission url  : https://leetcode.com/submissions/detail/1107276717/
// Submission json : {"id": 1107276717, "status_display": "Accepted", "lang": "cpp", "question_id": 1845, "title_slug": "largest-submatrix-with-rearrangements", "code": "class Solution {\npublic:\n    int largestSubmatrix(vector<vector<int>>& matrix) {\n        int m = matrix.size();\n        int n = matrix[0].size();\n        int ans = 0;\n        \n        for (int row = 0; row < m; row++) {\n            for (int col = 0; col < n; col++) {\n                if (matrix[row][col] != 0 && row > 0) {\n                    matrix[row][col] += matrix[row - 1][col];\n                }\n            }\n            \n            vector<int> currRow = matrix[row];\n            sort(currRow.begin(), currRow.end(), greater());\n            for (int i = 0; i < n; i++) {\n                ans = max(ans, currRow[i] * (i + 1));\n            }\n        }\n        \n        return ans;\n    }\n};", "title": "Largest Submatrix With Rearrangements", "url": "/submissions/detail/1107276717/", "lang_name": "C++", "time": "2\u00a0months, 1\u00a0week", "timestamp": 1701070363, "status": 10, "runtime": "172 ms", "is_pending": "Not Pending", "memory": "74.8 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}



class Solution {
public:
    int largestSubmatrix(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        int ans = 0;

        for (int row = 0; row < m; row++) {
            for (int col = 0; col < n; col++) {
                if (matrix[row][col] != 0 && row > 0) {
                    matrix[row][col] += matrix[row - 1][col];
                }
            }

            vector<int> currRow = matrix[row];
            sort(currRow.begin(), currRow.end(), greater());
            for (int i = 0; i < n; i++) {
                ans = max(ans, currRow[i] * (i + 1));
            }
        }

        return ans;
    }
};
