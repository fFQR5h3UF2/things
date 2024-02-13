// Submission title: Find a Corresponding Node of a Binary Tree in a Clone of That Tree
// Submission url  : https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/description/
// Submission url  : https://leetcode.com/submissions/detail/701177667/
// Submission json : {"id":701177667,"status_display":"Accepted","lang":"java","question_id":1498,"title_slug":"find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree","code":"class Solution {\nTreeNode ans;\n\npublic void inorder(TreeNode c,TreeNode target) {\nif (c != null) {\ninorder(c.left, target);\nif (c.val == target.val) {\nans = c;\n}\ninorder(c.right, target);\n}\n}\n\npublic final TreeNode getTargetCopy(final TreeNode original, final TreeNode cloned, final TreeNode target)\n{\ninorder(cloned,target);\nreturn ans;\n}\n}","title":"Find a Corresponding Node of a Binary Tree in a Clone of That Tree","url":"/submissions/detail/701177667/","lang_name":"Java","time":"1 year, 8 months","timestamp":1652763542,"status":10,"runtime":"2 ms","is_pending":"Not Pending","memory":"101.5 MB","compare_result":"11111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
com.shishifubing.dotfiles.submissions
class Solution {
TreeNode ans;

public void inorder(TreeNode c,TreeNode target) {
if (c != null) {
inorder(c.left, target);
if (c.val == target.val) {
ans = c;
}
inorder(c.right, target);
}
}

public final TreeNode getTargetCopy(final TreeNode original, final TreeNode cloned, final TreeNode target)
{
inorder(cloned,target);
return ans;
}
}
