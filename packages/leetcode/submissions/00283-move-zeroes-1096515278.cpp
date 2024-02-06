// Submission title: for Move Zeroes
// Submission url  : https://leetcode.com/submissions/detail/1096515278/
// Submission json : {"id": 1096515278, "status_display": "Accepted", "lang": "cpp", "question_id": 283, "title_slug": "move-zeroes", "code": "class Solution {\npublic:\n    void moveZeroes(vector<int>& nums) {\n    int lastNonZeroFoundAt = 0;\n    int length = nums.size();\n    for (int i = 0; i < length; ++i) {\n        int num = nums[i];\n        if (num == 0) {\n            continue;\n        }\n        if (i != lastNonZeroFoundAt) {\n            nums[lastNonZeroFoundAt] = num;\n        }\n        lastNonZeroFoundAt += 1;\n    }\n \tfor (int i = lastNonZeroFoundAt; i < length; i++) {\n        nums[i] = 0;\n    }\n}\n};", "title": "Move Zeroes", "url": "/submissions/detail/1096515278/", "lang_name": "C++", "time": "2\u00a0months, 3\u00a0weeks", "timestamp": 1699704365, "status": 10, "runtime": "16 ms", "is_pending": "Not Pending", "memory": "19.5 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}



class Solution {
public:
    void moveZeroes(vector<int>& nums) {
    int lastNonZeroFoundAt = 0;
    int length = nums.size();
    for (int i = 0; i < length; ++i) {
        int num = nums[i];
        if (num == 0) {
            continue;
        }
        if (i != lastNonZeroFoundAt) {
            nums[lastNonZeroFoundAt] = num;
        }
        lastNonZeroFoundAt += 1;
    }
 	for (int i = lastNonZeroFoundAt; i < length; i++) {
        nums[i] = 0;
    }
}
};
