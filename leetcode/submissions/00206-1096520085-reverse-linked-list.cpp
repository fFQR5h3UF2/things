// Submission title: Reverse Linked List
// Submission url  : https://leetcode.com/problems/reverse-linked-list/description/"
// Submission url  : https://leetcode.com/submissions/detail/1096520085/"


class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = NULL;
        ListNode* curr = head;
        while(curr != NULL){
            ListNode* next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }
};
