// Submission title: Diagonal Traverse II
// Submission url  : https://leetcode.com/problems/diagonal-traverse-ii/description/
// Submission url  : https://leetcode.com/submissions/detail/1104261001/
// Submission json : {"id":1104261001,"status_display":"Accepted","lang":"cpp","question_id":1539,"title_slug":"diagonal-traverse-ii","code":"class Solution {\npublic:\n    vector<int> findDiagonalOrder(vector<vector<int>>& nums) {\n        unordered_map<int, vector<int>> groups;\n        for (int row = nums.size() - 1; row >= 0; row--) {\n            for (int col = 0; col < nums[row].size(); col++) {\n                int diagonal = row + col;\n                groups[diagonal].push_back(nums[row][col]);\n            }\n        }\n        \n        vector<int> ans;\n        int curr = 0;\n        \n        while (groups.find(curr) != groups.end()) {\n            for (int num : groups[curr]) {\n                ans.push_back(num);\n            }\n            \n            curr++;\n        }\n        \n        return ans;\n    }\n};\n","title":"Diagonal Traverse II","url":"/submissions/detail/1104261001/","lang_name":"C++","time":"2 months, 1 week","timestamp":1700668142,"status":10,"runtime":"212 ms","is_pending":"Not Pending","memory":"97.6 MB","compare_result":"11111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}

class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& nums) {
        unordered_map<int, vector<int>> groups;
        for (int row = nums.size() - 1; row >= 0; row--) {
            for (int col = 0; col < nums[row].size(); col++) {
                int diagonal = row + col;
                groups[diagonal].push_back(nums[row][col]);
            }
        }

        vector<int> ans;
        int curr = 0;

        while (groups.find(curr) != groups.end()) {
            for (int num : groups[curr]) {
                ans.push_back(num);
            }

            curr++;
        }

        return ans;
    }
};
