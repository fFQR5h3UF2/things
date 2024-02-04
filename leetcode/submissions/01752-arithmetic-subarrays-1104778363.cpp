// Submission title: for Arithmetic Subarrays
// Submission url  : https://leetcode.com/submissions/detail/1104778363/
// Submission json : {"id": 1104778363, "status_display": "Accepted", "lang": "cpp", "question_id": 1752, "title_slug": "arithmetic-subarrays", "code": "class Solution {\npublic:\n    bool check(vector<int>& arr) {\n        sort(arr.begin(), arr.end());\n        int diff = arr[1] - arr[0];\n        \n        for (int i = 2; i < arr.size(); i++) {\n            if (arr[i] - arr[i - 1] != diff) {\n                return false;\n            }\n        }\n        \n        return true;\n    }\n    \n    vector<bool> checkArithmeticSubarrays(vector<int>& nums, vector<int>& l, vector<int>& r) {\n        vector<bool> ans;\n        for (int i = 0; i < l.size(); i++) {\n            vector<int> arr(begin(nums) + l[i], begin(nums) + r[i] + 1);\n            ans.push_back(check(arr));\n        }\n        \n        return ans;\n    }\n};", "title": "Arithmetic Subarrays", "url": "/submissions/detail/1104778363/", "lang_name": "C++", "time": "2\u00a0months, 1\u00a0week", "timestamp": 1700736084, "status": 10, "runtime": "41 ms", "is_pending": "Not Pending", "memory": "26.4 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}



class Solution {
public:
    bool check(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        int diff = arr[1] - arr[0];

        for (int i = 2; i < arr.size(); i++) {
            if (arr[i] - arr[i - 1] != diff) {
                return false;
            }
        }

        return true;
    }

    vector<bool> checkArithmeticSubarrays(vector<int>& nums, vector<int>& l, vector<int>& r) {
        vector<bool> ans;
        for (int i = 0; i < l.size(); i++) {
            vector<int> arr(begin(nums) + l[i], begin(nums) + r[i] + 1);
            ans.push_back(check(arr));
        }

        return ans;
    }
};
