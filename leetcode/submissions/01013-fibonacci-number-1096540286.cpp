// Submission title: Fibonacci Number
// Submission url  : https://leetcode.com/problems/fibonacci-number/description/
// Submission url  : https://leetcode.com/submissions/detail/1096540286/
// Submission json : {"id":1096540286,"status_display":"Accepted","lang":"cpp","question_id":1013,"title_slug":"fibonacci-number","code":"class Solution {\npublic:\n    int fib(int n) {\n        if (n < 2) {\n            return n;\n        }\n        int cur = 1, prev = 0;\n        for (int i = 2; i <= n; ++i) {\n            int newVal = cur + prev;\n            prev = cur;\n            cur = newVal;\n        }\n        return cur;\n    }\n};","title":"Fibonacci Number","url":"/submissions/detail/1096540286/","lang_name":"C++","time":"2 months, 3 weeks","timestamp":1699708200,"status":10,"runtime":"2 ms","is_pending":"Not Pending","memory":"6.2 MB","compare_result":"1111111111111111111111111111111","has_notes":false,"flag_type":1}

class Solution {
public:
    int fib(int n) {
        if (n < 2) {
            return n;
        }
        int cur = 1, prev = 0;
        for (int i = 2; i <= n; ++i) {
            int newVal = cur + prev;
            prev = cur;
            cur = newVal;
        }
        return cur;
    }
};
