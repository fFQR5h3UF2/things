// Submission title: Reverse Linked List
// Submission url  : https://leetcode.com/problems/reverse-linked-list/description/
// Submission url  : https://leetcode.com/submissions/detail/1096520085/
// Submission json : {"id":1096520085,"status_display":"Accepted","lang":"cpp","question_id":206,"title_slug":"reverse-linked-list","code":"\nclass Solution {\npublic:\n    ListNode* reverseList(ListNode* head) {\n        ListNode* prev = NULL;\n        ListNode* curr = head;\n        while(curr != NULL){\n            ListNode* next = curr->next;\n            curr->next = prev;\n            prev = curr;\n            curr = next;\n        }\n        return prev;\n    }\n};","title":"Reverse Linked List","url":"/submissions/detail/1096520085/","lang_name":"C++","time":"2 months, 3 weeks","timestamp":1699705119,"status":10,"runtime":"4 ms","is_pending":"Not Pending","memory":"8.8 MB","compare_result":"1111111111111111111111111111","has_notes":false,"flag_type":1}


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
