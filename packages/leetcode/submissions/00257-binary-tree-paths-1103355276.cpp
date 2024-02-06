// Submission title: for Binary Tree Paths
// Submission url  : https://leetcode.com/submissions/detail/1103355276/
// Submission json : {"id": 1103355276, "status_display": "Accepted", "lang": "cpp", "question_id": 257, "title_slug": "binary-tree-paths", "code": "/**\n * Definition for a binary tree node.\n * struct TreeNode {\n *     int val;\n *     TreeNode *left;\n *     TreeNode *right;\n *     TreeNode() : val(0), left(nullptr), right(nullptr) {}\n *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}\n *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}\n * };\n */\nclass Solution {\npublic:\n    vector<string> binaryTreePaths(TreeNode* root) {\n        vector<string> ans;\n        dfs(*root, ans, \"\");\n        return ans;\n    }\n\n    void dfs(TreeNode& root, vector<string> &ans, string path){\n        path += (path.size() ? \"->\" : \"\") + std::to_string(root.val);\n        if(!root.left && !root.right) {\n            ans.push_back(path);\n            return;\n        }\n        if(root.left) {\n            dfs(*root.left, ans, path);\n        }\n        if(root.right) {\n            dfs(*root.right, ans, path);\n        }\n    }\n};", "title": "Binary Tree Paths", "url": "/submissions/detail/1103355276/", "lang_name": "C++", "time": "2\u00a0months, 2\u00a0weeks", "timestamp": 1700560280, "status": 10, "runtime": "0 ms", "is_pending": "Not Pending", "memory": "13.9 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}



/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> ans;
        dfs(*root, ans, "");
        return ans;
    }

    void dfs(TreeNode& root, vector<string> &ans, string path){
        path += (path.size() ? "->" : "") + std::to_string(root.val);
        if(!root.left && !root.right) {
            ans.push_back(path);
            return;
        }
        if(root.left) {
            dfs(*root.left, ans, path);
        }
        if(root.right) {
            dfs(*root.right, ans, path);
        }
    }
};
