// Submission title: Odd Even Linked List
// Submission url  : https://leetcode.com/problems/odd-even-linked-list/description/"
// Submission url  : https://leetcode.com/submissions/detail/1100824123/"

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
    ListNode* oddEvenList(ListNode* head) {
        if(!head || !head->next || !head->next->next) {
            return head;
        }

        ListNode* odd {head};
        ListNode* even {head->next};
        ListNode* even_start {head->next};

        while(odd->next && even->next) {
            ListNode* next {even->next};
            odd->next = next;
            even->next = next->next;
            odd = odd->next;
            even = even->next;
        }
        odd->next = even_start;
        return head;
    }
};
