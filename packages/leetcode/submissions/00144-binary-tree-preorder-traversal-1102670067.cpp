// Submission title: for Binary Tree Preorder Traversal
// Submission url  : https://leetcode.com/submissions/detail/1102670067/
// Submission json : {"id": 1102670067, "status_display": "Accepted", "lang": "cpp", "question_id": 144, "title_slug": "binary-tree-preorder-traversal", "code": "/**\n * Definition for a binary tree node.\n * struct TreeNode {\n *     int val;\n *     TreeNode *left;\n *     TreeNode *right;\n *     TreeNode() : val(0), left(nullptr), right(nullptr) {}\n *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}\n *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}\n * };\n */\nclass Solution {\npublic:\n    vector<int> preorderTraversal(TreeNode* root) {\n        if (root == nullptr) {\n            return {};\n        }\n        std::vector<int> ans{};\n        std::vector<TreeNode*> q{root};\n        while (q.size() != 0) {\n            auto node = q.back();\n            auto left{node->left}, right{node->right};\n            q.pop_back();\n            ans.push_back(node->val);\n            if (right != nullptr) {\n                q.push_back(right);\n            }\n            if (left != nullptr) {\n                q.push_back(left);\n            }\n        }\n        return ans;\n    }\n};", "title": "Binary Tree Preorder Traversal", "url": "/submissions/detail/1102670067/", "lang_name": "C++", "time": "2\u00a0months, 2\u00a0weeks", "timestamp": 1700479885, "status": 10, "runtime": "0 ms", "is_pending": "Not Pending", "memory": "8.5 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}



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
    vector<int> preorderTraversal(TreeNode* root) {
        if (root == nullptr) {
            return {};
        }
        std::vector<int> ans{};
        std::vector<TreeNode*> q{root};
        while (q.size() != 0) {
            auto node = q.back();
            auto left{node->left}, right{node->right};
            q.pop_back();
            ans.push_back(node->val);
            if (right != nullptr) {
                q.push_back(right);
            }
            if (left != nullptr) {
                q.push_back(left);
            }
        }
        return ans;
    }
};
