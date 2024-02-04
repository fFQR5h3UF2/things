// Submission title: for Binary Tree Postorder Traversal
// Submission url  : https://leetcode.com/submissions/detail/1102672996/
// Submission json : {"id": 1102672996, "status_display": "Accepted", "lang": "cpp", "question_id": 145, "title_slug": "binary-tree-postorder-traversal", "code": "/**\n * Definition for a binary tree node.\n * struct TreeNode {\n *     int val;\n *     TreeNode *left;\n *     TreeNode *right;\n *     TreeNode() : val(0), left(nullptr), right(nullptr) {}\n *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}\n *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}\n * };\n */\nclass Solution {\npublic:\n    vector<int> postorderTraversal(TreeNode* root) {\n        if (root == nullptr) {\n            return {};\n        }\n        std::vector<int> ans{};\n        addNodes(root, ans);\n        return ans;\n    }\n\n    void addNodes(TreeNode* node, std::vector<int>& ans) {\n        auto left{node->left}, right{node->right};\n        if (left != nullptr) {\n            addNodes(left, ans);\n        }\n        if (right != nullptr) {\n            addNodes(right, ans);\n        }\n        ans.push_back(node->val);\n    }\n};", "title": "Binary Tree Postorder Traversal", "url": "/submissions/detail/1102672996/", "lang_name": "C++", "time": "2\u00a0months, 2\u00a0weeks", "timestamp": 1700480320, "status": 10, "runtime": "2 ms", "is_pending": "Not Pending", "memory": "8.9 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}



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
    vector<int> postorderTraversal(TreeNode* root) {
        if (root == nullptr) {
            return {};
        }
        std::vector<int> ans{};
        addNodes(root, ans);
        return ans;
    }

    void addNodes(TreeNode* node, std::vector<int>& ans) {
        auto left{node->left}, right{node->right};
        if (left != nullptr) {
            addNodes(left, ans);
        }
        if (right != nullptr) {
            addNodes(right, ans);
        }
        ans.push_back(node->val);
    }
};
