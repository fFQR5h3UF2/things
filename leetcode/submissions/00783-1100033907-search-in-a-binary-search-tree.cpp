// Submission title: Search in a Binary Search Tree
// Submission url  : https://leetcode.com/problems/search-in-a-binary-search-tree/description/"
// Submission url  : https://leetcode.com/submissions/detail/1100033907/"

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
