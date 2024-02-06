// Submission title: for Transpose Matrix
// Submission url  : https://leetcode.com/submissions/detail/1116406430/
// Submission json : {"id": 1116406430, "status_display": "Accepted", "lang": "cpp", "question_id": 898, "title_slug": "transpose-matrix", "code": "class Solution {\npublic:\n    vector<vector<int>> transpose(vector<vector<int>>& matrix) {\n        int row = matrix.size();\n        int col = matrix[0].size();\n        vector<vector<int>> result(col, vector<int>(row, 0));\n        \n        for (int i = 0; i < col; ++i) {\n            for (int j = 0; j < row; ++j) {\n                result[i][j] = matrix[j][i];\n            }\n        }\n        \n        return result;\n    }\n};", "title": "Transpose Matrix", "url": "/submissions/detail/1116406430/", "lang_name": "C++", "time": "1\u00a0month, 3\u00a0weeks", "timestamp": 1702205145, "status": 10, "runtime": "7 ms", "is_pending": "Not Pending", "memory": "10.9 MB", "compare_result": "111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}



class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& matrix) {
        int row = matrix.size();
        int col = matrix[0].size();
        vector<vector<int>> result(col, vector<int>(row, 0));

        for (int i = 0; i < col; ++i) {
            for (int j = 0; j < row; ++j) {
                result[i][j] = matrix[j][i];
            }
        }

        return result;
    }
};
