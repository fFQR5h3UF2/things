// Submission title: for Search in a Binary Search Tree
// Submission url  : https://leetcode.com/submissions/detail/1100032935/
// Submission json : {"id": 1100032935, "status_display": "Accepted", "lang": "cpp", "question_id": 783, "title_slug": "search-in-a-binary-search-tree", "code": "/**\n * Definition for a binary tree node.\n * struct TreeNode {\n *     int val;\n *     TreeNode *left;\n *     TreeNode *right;\n *     TreeNode() : val(0), left(nullptr), right(nullptr) {}\n *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}\n *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}\n * };\n */\nclass Solution {\npublic:\n    TreeNode* searchBST(TreeNode* root, int val) {\n        if (root == nullptr || root->val == val) {\n            return root;\n        }\n        if (val > root->val) {\n            return searchBST(root->right, val);\n        }\n        return searchBST(root->left, val);\n    }\n};", "title": "Search in a Binary Search Tree", "url": "/submissions/detail/1100032935/", "lang_name": "C++", "time": "2\u00a0months, 2\u00a0weeks", "timestamp": 1700133358, "status": 10, "runtime": "24 ms", "is_pending": "Not Pending", "memory": "35.2 MB", "compare_result": "111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}



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
    TreeNode* searchBST(TreeNode* root, int val) {
        if (root == nullptr || root->val == val) {
            return root;
        }
        if (val > root->val) {
            return searchBST(root->right, val);
        }
        return searchBST(root->left, val);
    }
};
