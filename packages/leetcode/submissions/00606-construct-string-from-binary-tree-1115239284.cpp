// Submission title: for Construct String from Binary Tree
// Submission url  : https://leetcode.com/submissions/detail/1115239284/
// Submission json : {"id": 1115239284, "status_display": "Accepted", "lang": "cpp", "question_id": 606, "title_slug": "construct-string-from-binary-tree", "code": "class Solution {\npublic:\n    string tree2str(TreeNode* root) {\n        string str = \"\";\n         check(root, str);\n         return str;\n    }\n    void check(TreeNode* root, string &str) {\n        if (root == NULL) {\n            return;\n        }\n        str += to_string(root->val);\n        if (root->left || root->right) {\n            str += '(';\n            check(root->left, str);\n            str += ')';\n        }\n        if (root->right) {\n            str += '(';\n            check(root->right, str);\n            str += ')';\n        }\n        \n    }\n    \n};", "title": "Construct String from Binary Tree", "url": "/submissions/detail/1115239284/", "lang_name": "C++", "time": "1\u00a0month, 3\u00a0weeks", "timestamp": 1702058637, "status": 10, "runtime": "7 ms", "is_pending": "Not Pending", "memory": "23.7 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}



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
