// Submission title: for Binary Tree Preorder Traversal
// Submission url  : https://leetcode.com/submissions/detail/1102668286/
// Submission json : {"id": 1102668286, "status_display": "Accepted", "lang": "cpp", "question_id": 144, "title_slug": "binary-tree-preorder-traversal", "code": "/**\n * Definition for a binary tree node.\n * struct TreeNode {\n *     int val;\n *     TreeNode *left;\n *     TreeNode *right;\n *     TreeNode() : val(0), left(nullptr), right(nullptr) {}\n *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}\n *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}\n * };\n */\nclass Solution {\npublic:\n    vector<int> preorderTraversal(TreeNode* root) {\n        std::vector<int> ans{};\n        std::deque<TreeNode*> q{root};\n        while (q.size() != 0) {\n            auto node = q.front();\n            q.pop_front();\n            if (node == nullptr) {\n                continue;\n            }\n            ans.push_back(node->val);\n            q.push_front(node->right);\n            q.push_front(node->left);\n        }\n        return ans;\n    }\n};", "title": "Binary Tree Preorder Traversal", "url": "/submissions/detail/1102668286/", "lang_name": "C++", "time": "2\u00a0months, 2\u00a0weeks", "timestamp": 1700479632, "status": 10, "runtime": "5 ms", "is_pending": "Not Pending", "memory": "9.1 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}



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
        std::vector<int> ans{};
        std::deque<TreeNode*> q{root};
        while (q.size() != 0) {
            auto node = q.front();
            q.pop_front();
            if (node == nullptr) {
                continue;
            }
            ans.push_back(node->val);
            q.push_front(node->right);
            q.push_front(node->left);
        }
        return ans;
    }
};
