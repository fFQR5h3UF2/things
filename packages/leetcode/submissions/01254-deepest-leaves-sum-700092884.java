// Submission title: for Deepest Leaves Sum
// Submission url  : https://leetcode.com/submissions/detail/700092884/
// Submission json : {"id": 700092884, "status_display": "Accepted", "lang": "java", "question_id": 1254, "title_slug": "deepest-leaves-sum", "code": "/**\n * Definition for a binary tree node.\n * public class TreeNode {\n *     int val;\n *     TreeNode left;\n *     TreeNode right;\n *     TreeNode() {}\n *     TreeNode(int val) { this.val = val; }\n *     TreeNode(int val, TreeNode left, TreeNode right) {\n *         this.val = val;\n *         this.left = left;\n *         this.right = right;\n *     }\n * }\n */\nclass Solution {\n    public int deepestLeavesSum(TreeNode root) {\n        MaxDepthInfo maxDepthInfo = new MaxDepthInfo(0 ,0);\n        sumAtLevel(root, 0, maxDepthInfo);\n        return maxDepthInfo.getSumAtMaxDepth();\n    }\n\n    public void sumAtLevel(TreeNode root, int currentDepth, MaxDepthInfo maxDepthInfo) {\n        if (root == null) return;\n\n        if (currentDepth > maxDepthInfo.getMaxDepth()) {\n            maxDepthInfo.setMaxDepth(currentDepth);\n            maxDepthInfo.setSumAtMaxDepth(root.val);\n        }\n\n        else if (currentDepth == maxDepthInfo.getMaxDepth())\n            maxDepthInfo.setSumAtMaxDepth(maxDepthInfo.getSumAtMaxDepth() + root.val);\n\n        sumAtLevel(root.left, currentDepth + 1, maxDepthInfo);\n        sumAtLevel(root.right, currentDepth + 1, maxDepthInfo);\n    }\n\n    public static class MaxDepthInfo {\n        private int maxDepth;\n        private int sumAtMaxDepth;\n\n        public MaxDepthInfo(int maxDepth, int sumAtMaxDepth) {\n            this.maxDepth = maxDepth;\n            this.sumAtMaxDepth = sumAtMaxDepth;\n        }\n\n        public int getMaxDepth() { return maxDepth;}\n\n        public void setMaxDepth(int maxDepth) { this.maxDepth = maxDepth;}\n\n        public int getSumAtMaxDepth() { return sumAtMaxDepth;}\n\n        public void setSumAtMaxDepth(int sumAtMaxDepth) { this.sumAtMaxDepth = sumAtMaxDepth;}\n    }\n}", "title": "Deepest Leaves Sum", "url": "/submissions/detail/700092884/", "lang_name": "Java", "time": "1\u00a0year, 8\u00a0months", "timestamp": 1652629473, "status": 10, "runtime": "1 ms", "is_pending": "Not Pending", "memory": "44.6 MB", "compare_result": "11111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

com.shishifubing.dotfiles.submissions

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int deepestLeavesSum(TreeNode root) {
        MaxDepthInfo maxDepthInfo = new MaxDepthInfo(0 ,0);
        sumAtLevel(root, 0, maxDepthInfo);
        return maxDepthInfo.getSumAtMaxDepth();
    }

    public void sumAtLevel(TreeNode root, int currentDepth, MaxDepthInfo maxDepthInfo) {
        if (root == null) return;

        if (currentDepth > maxDepthInfo.getMaxDepth()) {
            maxDepthInfo.setMaxDepth(currentDepth);
            maxDepthInfo.setSumAtMaxDepth(root.val);
        }

        else if (currentDepth == maxDepthInfo.getMaxDepth())
            maxDepthInfo.setSumAtMaxDepth(maxDepthInfo.getSumAtMaxDepth() + root.val);

        sumAtLevel(root.left, currentDepth + 1, maxDepthInfo);
        sumAtLevel(root.right, currentDepth + 1, maxDepthInfo);
    }

    public static class MaxDepthInfo {
        private int maxDepth;
        private int sumAtMaxDepth;

        public MaxDepthInfo(int maxDepth, int sumAtMaxDepth) {
            this.maxDepth = maxDepth;
            this.sumAtMaxDepth = sumAtMaxDepth;
        }

        public int getMaxDepth() { return maxDepth;}

        public void setMaxDepth(int maxDepth) { this.maxDepth = maxDepth;}

        public int getSumAtMaxDepth() { return sumAtMaxDepth;}

        public void setSumAtMaxDepth(int sumAtMaxDepth) { this.sumAtMaxDepth = sumAtMaxDepth;}
    }
}
