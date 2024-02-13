// Submission title: Subrectangle Queries
// Submission url  : https://leetcode.com/problems/subrectangle-queries/description/
// Submission url  : https://leetcode.com/submissions/detail/1096023462/
// Submission json : {"id":1096023462,"status_display":"Accepted","lang":"cpp","question_id":1572,"title_slug":"subrectangle-queries","code":"class SubrectangleQueries {\n    vector<vector<int>> res;\npublic:\n    SubrectangleQueries(vector<vector<int>>& rectangle) {\n        res=rectangle;\n    }\n    \n    void updateSubrectangle(int row1, int col1, int row2, int col2, int newValue) {\n        for(int i = row1; i <= row2; ++i) {\n            for(int j= col1; j <= col2; ++j) {\n                res[i][j] = newValue;\n            }\n        }\n    }\n    \n    int getValue(int row, int col) {\n        return res[row][col];\n    }\n};\n\n/**\n * Your SubrectangleQueries object will be instantiated and called as such:\n * SubrectangleQueries* obj = new SubrectangleQueries(rectangle);\n * obj->updateSubrectangle(row1,col1,row2,col2,newValue);\n * int param_2 = obj->getValue(row,col);\n */","title":"Subrectangle Queries","url":"/submissions/detail/1096023462/","lang_name":"C++","time":"2 months, 3 weeks","timestamp":1699634090,"status":10,"runtime":"35 ms","is_pending":"Not Pending","memory":"18.8 MB","compare_result":"1111111111111111111111111111111111111111111111111111","has_notes":true,"flag_type":1}

class SubrectangleQueries {
    vector<vector<int>> res;
public:
    SubrectangleQueries(vector<vector<int>>& rectangle) {
        res=rectangle;
    }

    void updateSubrectangle(int row1, int col1, int row2, int col2, int newValue) {
        for(int i = row1; i <= row2; ++i) {
            for(int j= col1; j <= col2; ++j) {
                res[i][j] = newValue;
            }
        }
    }

    int getValue(int row, int col) {
        return res[row][col];
    }
};

/**
 * Your SubrectangleQueries object will be instantiated and called as such:
 * SubrectangleQueries* obj = new SubrectangleQueries(rectangle);
 * obj->updateSubrectangle(row1,col1,row2,col2,newValue);
 * int param_2 = obj->getValue(row,col);
 */
