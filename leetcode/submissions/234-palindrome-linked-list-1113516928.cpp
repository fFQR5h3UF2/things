// Submission for Palindrome Linked List
// Submission url: https://leetcode.com/submissions/detail/1113516928/



class Solution {
public:
    bool isPalindrome(ListNode* head) {
        if(head == nullptr || head->next == nullptr){
            return false;
        }
        ListNode *r_head = nullptr;
        ListNode *ptr = head;
        while(ptr != nullptr){
            ListNode *temp = new ListNode(ptr->val);
            temp->next = r_head;
            r_head = temp;
            ptr = ptr->next;
        }
        while(head && r_head){
            if(head->val != r_head->val){
                return false;
            }
            head = head->next;
            r_head = r_head->next;
        }
        return true;
    }
};
