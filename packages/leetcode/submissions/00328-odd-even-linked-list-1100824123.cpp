// Submission title: for Odd Even Linked List
// Submission url  : https://leetcode.com/submissions/detail/1100824123/
// Submission json : {"id": 1100824123, "status_display": "Accepted", "lang": "cpp", "question_id": 328, "title_slug": "odd-even-linked-list", "code": "/**\n * Definition for singly-linked list.\n * struct ListNode {\n *     int val;\n *     ListNode *next;\n *     ListNode() : val(0), next(nullptr) {}\n *     ListNode(int x) : val(x), next(nullptr) {}\n *     ListNode(int x, ListNode *next) : val(x), next(next) {}\n * };\n */\nclass Solution {\npublic:\n    ListNode* oddEvenList(ListNode* head) {\n        if(!head || !head->next || !head->next->next) {\n            return head;\n        } \n        \n        ListNode* odd {head};\n        ListNode* even {head->next};\n        ListNode* even_start {head->next};\n        \n        while(odd->next && even->next) {\n            ListNode* next {even->next}; \n            odd->next = next;\n            even->next = next->next;\n            odd = odd->next;\n            even = even->next;\n        }\n        odd->next = even_start;\n        return head; \n    }\n};", "title": "Odd Even Linked List", "url": "/submissions/detail/1100824123/", "lang_name": "C++", "time": "2\u00a0months, 2\u00a0weeks", "timestamp": 1700231121, "status": 10, "runtime": "8 ms", "is_pending": "Not Pending", "memory": "10.9 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}



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
