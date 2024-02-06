// Submission title: for Search in a Binary Search Tree
// Submission url  : https://leetcode.com/submissions/detail/1100033907/
// Submission json : {"id": 1100033907, "status_display": "Accepted", "lang": "cpp", "question_id": 783, "title_slug": "search-in-a-binary-search-tree", "code": "/**\n * Definition for a binary tree node.\n * struct TreeNode {\n *     int val;\n *     TreeNode *left;\n *     TreeNode *right;\n *     TreeNode() : val(0), left(nullptr), right(nullptr) {}\n *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}\n *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}\n * };\n */\nclass Solution {\npublic:\n    TreeNode* searchBST(TreeNode* root, int val) {\n        while (root != nullptr) {\n            if (root->val == val) {\n                return root;\n            }\n            if (root->val > val) {\n                root = root->left;\n            } else {\n                root = root->right;\n            }\n        }\n        return root;\n    }\n};", "title": "Search in a Binary Search Tree", "url": "/submissions/detail/1100033907/", "lang_name": "C++", "time": "2\u00a0months, 2\u00a0weeks", "timestamp": 1700133495, "status": 10, "runtime": "36 ms", "is_pending": "Not Pending", "memory": "35 MB", "compare_result": "111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}



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
        while (root != nullptr) {
            if (root->val == val) {
                return root;
            }
            if (root->val > val) {
                root = root->left;
            } else {
                root = root->right;
            }
        }
        return root;
    }
};
