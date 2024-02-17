// Submission title: Construct String from Binary Tree
// Submission url  : https://leetcode.com/problems/construct-string-from-binary-tree/description/"
// Submission url  : https://leetcode.com/submissions/detail/1115239284/"

class Solution {
public:
    string tree2str(TreeNode* root) {
        string str = "";
         check(root, str);
         return str;
    }
    void check(TreeNode* root, string &str) {
        if (root == NULL) {
            return;
        }
        str += to_string(root->val);
        if (root->left || root->right) {
            str += '(';
            check(root->left, str);
            str += ')';
        }
        if (root->right) {
            str += '(';
            check(root->right, str);
            str += ')';
        }

    }

};
