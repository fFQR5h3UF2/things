// Submission title: Find Unique Binary String
// Submission url  : https://leetcode.com/problems/find-unique-binary-string/description/
// Submission url  : https://leetcode.com/submissions/detail/1099952562/
// Submission json : {"id":1099952562,"status_display":"Accepted","lang":"cpp","question_id":2107,"title_slug":"find-unique-binary-string","code":"class Solution {\npublic:\n    string findDifferentBinaryString(vector<string>& nums) {\n        unordered_set<int> integers;\n        for (string num : nums) {\n            integers.insert(stoi(num, 0, 2));\n        }\n\n        int n = nums.size();\n        string ans;\n        for (int num = 0; num <= n; num++) {\n            if (integers.find(num) == integers.end()) {\n                ans = bitset<16>(num).to_string();\n                break;\n            }\n        }\n        return ans.substr(16 - n);\n    }\n};","title":"Find Unique Binary String","url":"/submissions/detail/1099952562/","lang_name":"C++","time":"2 months, 2 weeks","timestamp":1700122957,"status":10,"runtime":"2 ms","is_pending":"Not Pending","memory":"10.7 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}

class Solution {
public:
    string findDifferentBinaryString(vector<string>& nums) {
        unordered_set<int> integers;
        for (string num : nums) {
            integers.insert(stoi(num, 0, 2));
        }

        int n = nums.size();
        string ans;
        for (int num = 0; num <= n; num++) {
            if (integers.find(num) == integers.end()) {
                ans = bitset<16>(num).to_string();
                break;
            }
        }
        return ans.substr(16 - n);
    }
};
