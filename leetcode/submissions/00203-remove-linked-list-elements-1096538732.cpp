// Submission title: Remove Linked List Elements
// Submission url  : https://leetcode.com/problems/remove-linked-list-elements/description/
// Submission url  : https://leetcode.com/submissions/detail/1096538732/
// Submission json : {"id":1096538732,"status_display":"Accepted","lang":"cpp","question_id":203,"title_slug":"remove-linked-list-elements","code":"/**\n * Definition for singly-linked list.\n * struct ListNode {\n *     int val;\n *     ListNode *next;\n *     ListNode() : val(0), next(nullptr) {}\n *     ListNode(int x) : val(x), next(nullptr) {}\n *     ListNode(int x, ListNode *next) : val(x), next(next) {}\n * };\n */\nclass Solution {\npublic:\n    ListNode* removeElements(ListNode* head, int val) {\n        head = new ListNode(-1, head);\n        auto ans = head;\n        while (head) {\n            auto next = head->next;\n            if (next && next->val == val) {\n                head->next = next->next;\n            } else {\n                head = head->next;\n            }\n        }\n        return ans->next;\n    }\n};","title":"Remove Linked List Elements","url":"/submissions/detail/1096538732/","lang_name":"C++","time":"2 months, 3 weeks","timestamp":1699707971,"status":10,"runtime":"16 ms","is_pending":"Not Pending","memory":"15.2 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}

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
        head = new ListNode(-1, head);
        auto ans = head;
        while (head) {
            auto next = head->next;
            if (next && next->val == val) {
                head->next = next->next;
            } else {
                head = head->next;
            }
        }
        return ans->next;
    }
};
