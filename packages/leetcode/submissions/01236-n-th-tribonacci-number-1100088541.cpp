// Submission title: for N-th Tribonacci Number
// Submission url  : https://leetcode.com/submissions/detail/1100088541/
// Submission json : {"id": 1100088541, "status_display": "Accepted", "lang": "cpp", "question_id": 1236, "title_slug": "n-th-tribonacci-number", "code": "class Solution {\npublic:\n    int tribonacci(int n) {\n        if (n == 0) {\n            return 0;\n        }\n        if (n == 1 || n == 2) {\n            return 1;\n        }\n        int num1 {0}, num2 {1}, num3 {1};\n        for (int i = 3; i <= n; ++i) {\n            int newNum3 = num1 + num2 + num3; \n            num1 = num2;\n            num2 = num3;\n            num3 = newNum3;\n        }\n        return num3;\n    }\n};", "title": "N-th Tribonacci Number", "url": "/submissions/detail/1100088541/", "lang_name": "C++", "time": "2\u00a0months, 2\u00a0weeks", "timestamp": 1700140969, "status": 10, "runtime": "2 ms", "is_pending": "Not Pending", "memory": "6.3 MB", "compare_result": "111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}



class Solution {
public:
    int tribonacci(int n) {
        if (n == 0) {
            return 0;
        }
        if (n == 1 || n == 2) {
            return 1;
        }
        int num1 {0}, num2 {1}, num3 {1};
        for (int i = 3; i <= n; ++i) {
            int newNum3 = num1 + num2 + num3;
            num1 = num2;
            num2 = num3;
            num3 = newNum3;
        }
        return num3;
    }
};
