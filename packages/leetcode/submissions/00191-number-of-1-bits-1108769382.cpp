// Submission title: for Number of 1 Bits
// Submission url  : https://leetcode.com/submissions/detail/1108769382/
// Submission json : {"id": 1108769382, "status_display": "Accepted", "lang": "cpp", "question_id": 191, "title_slug": "number-of-1-bits", "code": "class Solution {\npublic:\n    int hammingWeight(uint32_t n) {\n        int ans {};\n        while (n) {\n            if (n & 1) {\n                ++ans;\n            }\n            n >>= 1;\n        }\n        return ans;\n    }\n};", "title": "Number of 1 Bits", "url": "/submissions/detail/1108769382/", "lang_name": "C++", "time": "2\u00a0months, 1\u00a0week", "timestamp": 1701248504, "status": 10, "runtime": "0 ms", "is_pending": "Not Pending", "memory": "6.4 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}



class Solution {
public:
    int hammingWeight(uint32_t n) {
        int ans {};
        while (n) {
            if (n & 1) {
                ++ans;
            }
            n >>= 1;
        }
        return ans;
    }
};
