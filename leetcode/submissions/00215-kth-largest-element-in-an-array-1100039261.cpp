// Submission title: Kth Largest Element in an Array
// Submission url  : https://leetcode.com/problems/kth-largest-element-in-an-array/description/
// Submission url  : https://leetcode.com/submissions/detail/1100039261/
// Submission json : {"id":1100039261,"status_display":"Accepted","lang":"cpp","question_id":215,"title_slug":"kth-largest-element-in-an-array","code":"class Solution {\npublic:\n    int findKthLargest(vector<int>& nums, int k) {\n        std::sort(nums.begin(), nums.end(), std::greater<int>());\n        return nums[k-1];\n    }\n};","title":"Kth Largest Element in an Array","url":"/submissions/detail/1100039261/","lang_name":"C++","time":"2 months, 2 weeks","timestamp":1700134246,"status":10,"runtime":"85 ms","is_pending":"Not Pending","memory":"55.5 MB","compare_result":"11111111111111111111111111111111111111111","has_notes":false,"flag_type":1}

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end(), std::greater<int>());
        return nums[k-1];
    }
};
