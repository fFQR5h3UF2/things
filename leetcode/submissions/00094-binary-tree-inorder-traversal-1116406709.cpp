// Submission title: Binary Tree Inorder Traversal
// Submission url  : https://leetcode.com/problems/binary-tree-inorder-traversal/description/
// Submission url  : https://leetcode.com/submissions/detail/1116406709/
// Submission json : {"id":1116406709,"status_display":"Accepted","lang":"cpp","question_id":94,"title_slug":"binary-tree-inorder-traversal","code":"/**\n * Definition for a binary tree node.\n * struct TreeNode {\n *     int val;\n *     TreeNode *left;\n *     TreeNode *right;\n *     TreeNode() : val(0), left(nullptr), right(nullptr) {}\n *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}\n *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}\n * };\n */\nclass Solution {\npublic:\n    vector<int> inorderTraversal(TreeNode* root) {\n        vector<int> result;\n        helper(root, result);\n        return result;\n    }\n\n    void helper(TreeNode* root, vector<int>& result) {\n        if (root != nullptr) {\n            helper(root->left, result);\n            result.push_back(root->val);\n            helper(root->right, result);\n        }\n    }\n};","title":"Binary Tree Inorder Traversal","url":"/submissions/detail/1116406709/","lang_name":"C++","time":"1 month, 3 weeks","timestamp":1702205182,"status":10,"runtime":"4 ms","is_pending":"Not Pending","memory":"8.7 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}

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
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        helper(root, result);
        return result;
    }

    void helper(TreeNode* root, vector<int>& result) {
        if (root != nullptr) {
            helper(root->left, result);
            result.push_back(root->val);
            helper(root->right, result);
        }
    }
};
