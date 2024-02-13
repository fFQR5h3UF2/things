// Submission title: Subrectangle Queries
// Submission url  : https://leetcode.com/problems/subrectangle-queries/description/
// Submission url  : https://leetcode.com/submissions/detail/1096014225/
// Submission json : {"id":1096014225,"status_display":"Accepted","lang":"cpp","question_id":1572,"title_slug":"subrectangle-queries","code":"class SubrectangleQueries {\npublic:\n    std::vector<std::vector<int>> rectangle;\n    std::vector<std::array<int, 5>> updates;\n    SubrectangleQueries(vector<vector<int>>& rectangle) {\n        this->rectangle = rectangle;\n    }\n    \n    void updateSubrectangle(int row1, int col1, int row2, int col2, int newValue) {\n        this->updates.push_back({row1, col1, row2, col2, newValue});\n    }\n    \n    int getValue(int row, int col) {\n        int length = this->updates.size();\n        for (int i = length - 1; i >= 0; --i) {\n            auto const [row1, col1, row2, col2, newValue] = this->updates[i];\n            if (row < row1 || row > row2 || col < col1 || col > col2) {\n                continue;\n            }\n            return newValue;\n        }\n        return this->rectangle[row][col];\n    }\n};\n\n/**\n * Your SubrectangleQueries object will be instantiated and called as such:\n * SubrectangleQueries* obj = new SubrectangleQueries(rectangle);\n * obj->updateSubrectangle(row1,col1,row2,col2,newValue);\n * int param_2 = obj->getValue(row,col);\n */","title":"Subrectangle Queries","url":"/submissions/detail/1096014225/","lang_name":"C++","time":"2 months, 3 weeks","timestamp":1699633107,"status":10,"runtime":"35 ms","is_pending":"Not Pending","memory":"19.1 MB","compare_result":"1111111111111111111111111111111111111111111111111111","has_notes":true,"flag_type":1}

class SubrectangleQueries {
public:
    std::vector<std::vector<int>> rectangle;
    std::vector<std::array<int, 5>> updates;
    SubrectangleQueries(vector<vector<int>>& rectangle) {
        this->rectangle = rectangle;
    }

    void updateSubrectangle(int row1, int col1, int row2, int col2, int newValue) {
        this->updates.push_back({row1, col1, row2, col2, newValue});
    }

    int getValue(int row, int col) {
        int length = this->updates.size();
        for (int i = length - 1; i >= 0; --i) {
            auto const [row1, col1, row2, col2, newValue] = this->updates[i];
            if (row < row1 || row > row2 || col < col1 || col > col2) {
                continue;
            }
            return newValue;
        }
        return this->rectangle[row][col];
    }
};

/**
 * Your SubrectangleQueries object will be instantiated and called as such:
 * SubrectangleQueries* obj = new SubrectangleQueries(rectangle);
 * obj->updateSubrectangle(row1,col1,row2,col2,newValue);
 * int param_2 = obj->getValue(row,col);
 */
