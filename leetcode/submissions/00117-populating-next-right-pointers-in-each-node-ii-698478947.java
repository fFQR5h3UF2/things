// Submission title: Populating Next Right Pointers in Each Node II
// Submission url  : https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/
// Submission url  : https://leetcode.com/submissions/detail/698478947/
// Submission json : {"id":698478947,"status_display":"Accepted","lang":"java","question_id":117,"title_slug":"populating-next-right-pointers-in-each-node-ii","code":"class Solution {\n    public Node connect(Node root) {\n        Node leftMost = root;\n        while (leftMost != null) {\n            Node cur = leftMost;\n            leftMost = null;\n            Node pre = null;\n            while (cur != null) {\n                if (leftMost == null) {\n                    leftMost = cur.left == null ? cur.right: cur.left;\n                }\n                if (pre != null) {\n                    pre.next = cur.left == null ? cur.right : cur.left;\n                }\n                if (cur.left != null && cur.right != null) {\n                    cur.left.next = cur.right;\n                }\n                pre = cur.right == null ? (cur.left == null ? pre : cur.left) : cur.right;\n                cur = cur.next;\n            }\n        }\n        return root;\n    }\n}","title":"Populating Next Right Pointers in Each Node II","url":"/submissions/detail/698478947/","lang_name":"Java","time":"1 year, 8 months","timestamp":1652415464,"status":10,"runtime":"1 ms","is_pending":"Not Pending","memory":"44.4 MB","compare_result":"1111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
com.shishifubing.dotfiles.submissions
class Solution {
    public Node connect(Node root) {
        Node leftMost = root;
        while (leftMost != null) {
            Node cur = leftMost;
            leftMost = null;
            Node pre = null;
            while (cur != null) {
                if (leftMost == null) {
                    leftMost = cur.left == null ? cur.right: cur.left;
                }
                if (pre != null) {
                    pre.next = cur.left == null ? cur.right : cur.left;
                }
                if (cur.left != null && cur.right != null) {
                    cur.left.next = cur.right;
                }
                pre = cur.right == null ? (cur.left == null ? pre : cur.left) : cur.right;
                cur = cur.next;
            }
        }
        return root;
    }
}
