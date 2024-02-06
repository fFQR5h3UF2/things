// Submission title: for Count Nice Pairs in an Array
// Submission url  : https://leetcode.com/submissions/detail/1103345965/
// Submission json : {"id": 1103345965, "status_display": "Accepted", "lang": "cpp", "question_id": 1925, "title_slug": "count-nice-pairs-in-an-array", "code": "class Solution {\npublic:\n    int countNicePairs(vector<int>& nums) {\n        std::unordered_map<int, int> diffs{};\n        for (const int& num : nums) {\n            int revNum{};\n            int tempNum{num};\n            while(tempNum) {\n                revNum = (revNum * 10) + (tempNum % 10);\n                tempNum /= 10;\n            }\n            ++diffs[num - revNum];\n        }\n        int ans{};\n        double mod{std::pow(10, 9) + 7};\n        for (const auto& [num, count] : diffs) {\n            long pairs{(1L * count * count - count) / 2};\n            ans = std::fmod(ans + pairs, mod);\n        }\n        return ans;\n    }\n\n};", "title": "Count Nice Pairs in an Array", "url": "/submissions/detail/1103345965/", "lang_name": "C++", "time": "2\u00a0months, 2\u00a0weeks", "timestamp": 1700559192, "status": 10, "runtime": "91 ms", "is_pending": "Not Pending", "memory": "57.3 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}



class Solution {
public:
    int countNicePairs(vector<int>& nums) {
        std::unordered_map<int, int> diffs{};
        for (const int& num : nums) {
            int revNum{};
            int tempNum{num};
            while(tempNum) {
                revNum = (revNum * 10) + (tempNum % 10);
                tempNum /= 10;
            }
            ++diffs[num - revNum];
        }
        int ans{};
        double mod{std::pow(10, 9) + 7};
        for (const auto& [num, count] : diffs) {
            long pairs{(1L * count * count - count) / 2};
            ans = std::fmod(ans + pairs, mod);
        }
        return ans;
    }

};
