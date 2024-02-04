// Submission for Remove Linked List Elements
// Submission url: https://leetcode.com/submissions/detail/1096536118/



/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        auto newHead = new ListNode(-1, head);
        auto ans = newHead;
        while (newHead) {
            auto next = head.next;
            if (next && next.val == val) {
                next = head.next.next;
                head.next = next;
            }
            head = next;
        }
        return ans.next;
    }
};
