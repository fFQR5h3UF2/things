// Submission title: for Palindrome Linked List
// Submission url  : https://leetcode.com/submissions/detail/1113522285/
// Submission json : {"id": 1113522285, "status_display": "Accepted", "lang": "cpp", "question_id": 234, "title_slug": "palindrome-linked-list", "code": "class Solution {\npublic:\n    bool isPalindrome(ListNode* head) {\n        ListNode* slow {head};\n        ListNode* fast {head};\n        ListNode* next;\n        ListNode* prev {new ListNode()};\n\n        while(fast && fast->next) {\n            slow = slow->next;\n            fast = fast->next->next; \n\n            next = head->next;\n            head->next = prev;\n            prev = head;\n            head = next;\n        }\n    \n        if (fast) {\n            slow = slow->next;\n        }\n        head = prev;\n\n        while (slow) {\n            if (head->val != slow->val) {\n                return false;\n            }\n            head = head->next;\n            slow = slow->next;\n        }\n        return true;\n    }\n};", "title": "Palindrome Linked List", "url": "/submissions/detail/1113522285/", "lang_name": "C++", "time": "2\u00a0months", "timestamp": 1701855940, "status": 10, "runtime": "137 ms", "is_pending": "Not Pending", "memory": "110.7 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}



class Solution {
public:
    bool isPalindrome(ListNode* head) {
        ListNode* slow {head};
        ListNode* fast {head};
        ListNode* next;
        ListNode* prev {new ListNode()};

        while(fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;

            next = head->next;
            head->next = prev;
            prev = head;
            head = next;
        }

        if (fast) {
            slow = slow->next;
        }
        head = prev;

        while (slow) {
            if (head->val != slow->val) {
                return false;
            }
            head = head->next;
            slow = slow->next;
        }
        return true;
    }
};
