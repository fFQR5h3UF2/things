// Submission for Find a Corresponding Node of a Binary Tree in a Clone of That Tree
// Submission url: https://leetcode.com/submissions/detail/701177667/

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
