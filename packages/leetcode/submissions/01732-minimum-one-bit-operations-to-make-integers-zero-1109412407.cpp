// Submission title: for Minimum One Bit Operations to Make Integers Zero
// Submission url  : https://leetcode.com/submissions/detail/1109412407/
// Submission json : {"id": 1109412407, "status_display": "Accepted", "lang": "cpp", "question_id": 1732, "title_slug": "minimum-one-bit-operations-to-make-integers-zero", "code": "class Solution {\npublic:\n    int minimumOneBitOperations(int n) {\n        if (n == 0) {\n            return 0;\n        }\n        \n        int k = 0;\n        int curr = 1;\n        while (curr * 2 <= n) {\n            curr *= 2;\n            k++;\n        }\n        \n        return (1 << (k + 1)) - 1 - minimumOneBitOperations(n ^ curr);\n    }\n};", "title": "Minimum One Bit Operations to Make Integers Zero", "url": "/submissions/detail/1109412407/", "lang_name": "C++", "time": "2\u00a0months", "timestamp": 1701330611, "status": 10, "runtime": "0 ms", "is_pending": "Not Pending", "memory": "6.1 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}



class Solution {
public:
    int minimumOneBitOperations(int n) {
        if (n == 0) {
            return 0;
        }

        int k = 0;
        int curr = 1;
        while (curr * 2 <= n) {
            curr *= 2;
            k++;
        }

        return (1 << (k + 1)) - 1 - minimumOneBitOperations(n ^ curr);
    }
};
