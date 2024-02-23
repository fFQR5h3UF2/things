// Submission title: Transpose Matrix
// Submission url  : https://leetcode.com/problems/transpose-matrix/description/
// Submission url  : https://leetcode.com/submissions/detail/1116406430/"

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
