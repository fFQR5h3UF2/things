// Submission title: for Calculate Money in Leetcode Bank
// Submission url  : https://leetcode.com/submissions/detail/1113427537/
// Submission json : {"id": 1113427537, "status_display": "Accepted", "lang": "cpp", "question_id": 1817, "title_slug": "calculate-money-in-leetcode-bank", "code": "class Solution {\npublic:\n    int totalMoney(int n) {\n        int ans {0};\n        int monday {1};\n        \n        while (n > 0) {\n            for (int day {0}; day < min(n, 7); ++day) {\n                ans += monday + day;\n            }\n            n -= 7;\n            ++monday;\n        }\n        \n        return ans;\n    }\n};", "title": "Calculate Money in Leetcode Bank", "url": "/submissions/detail/1113427537/", "lang_name": "C++", "time": "2\u00a0months", "timestamp": 1701844984, "status": 10, "runtime": "0 ms", "is_pending": "Not Pending", "memory": "6.4 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}



class Solution {
public:
    int totalMoney(int n) {
        int ans {0};
        int monday {1};

        while (n > 0) {
            for (int day {0}; day < min(n, 7); ++day) {
                ans += monday + day;
            }
            n -= 7;
            ++monday;
        }

        return ans;
    }
};
