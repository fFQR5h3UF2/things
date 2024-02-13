// Submission title: Frequency of the Most Frequent Element
// Submission url  : https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/
// Submission url  : https://leetcode.com/submissions/detail/1101503370/
// Submission json : {"id":1101503370,"status_display":"Accepted","lang":"cpp","question_id":1966,"title_slug":"frequency-of-the-most-frequent-element","code":"class Solution {\npublic:\n    int maxFrequency(vector<int>& nums, int k) {\n        sort(nums.begin(), nums.end());\n        int left = 0;\n        int ans = 0;\n        long curr = 0;\n        \n        for (int right = 0; right < nums.size(); right++) {\n            long target = nums[right];\n            curr += target;\n            \n            while ((right - left + 1) * target - curr > k) {\n                curr -= nums[left];\n                left++;\n            }\n            \n            ans = max(ans, right - left + 1);\n        }\n        \n        return ans;\n    }\n};","title":"Frequency of the Most Frequent Element","url":"/submissions/detail/1101503370/","lang_name":"C++","time":"2 months, 2 weeks","timestamp":1700324628,"status":10,"runtime":"161 ms","is_pending":"Not Pending","memory":"99.5 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}

class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int left = 0;
        int ans = 0;
        long curr = 0;

        for (int right = 0; right < nums.size(); right++) {
            long target = nums[right];
            curr += target;

            while ((right - left + 1) * target - curr > k) {
                curr -= nums[left];
                left++;
            }

            ans = max(ans, right - left + 1);
        }

        return ans;
    }
};
