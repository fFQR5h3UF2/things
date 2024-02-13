// Submission title: Find the Difference of Two Arrays
// Submission url  : https://leetcode.com/problems/find-the-difference-of-two-arrays/description/
// Submission url  : https://leetcode.com/submissions/detail/1099400651/
// Submission json : {"id":1099400651,"status_display":"Accepted","lang":"cpp","question_id":1392,"title_slug":"find-the-difference-of-two-arrays","code":"class Solution {\npublic:\n    vector<int> getElementsOnlyInFirstList(vector<int>& nums1, vector<int>& nums2) {\n        unordered_set<int> onlyInNums1;\n        for (int num : nums1) {\n            bool existInNums2 = false;\n            for (int x : nums2) {\n                if (x == num) {\n                    existInNums2 = true;\n                    break;\n                }\n            }\n            if (!existInNums2) {\n                onlyInNums1.insert(num);\n            }\n        }\n        return vector<int> (onlyInNums1.begin(), onlyInNums1.end());\n    }\n    \n    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {\n        return {getElementsOnlyInFirstList(nums1, nums2), getElementsOnlyInFirstList(nums2, nums1)};\n    }\n};","title":"Find the Difference of Two Arrays","url":"/submissions/detail/1099400651/","lang_name":"C++","time":"2 months, 3 weeks","timestamp":1700056427,"status":10,"runtime":"102 ms","is_pending":"Not Pending","memory":"30.3 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}

class Solution {
public:
    vector<int> getElementsOnlyInFirstList(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> onlyInNums1;
        for (int num : nums1) {
            bool existInNums2 = false;
            for (int x : nums2) {
                if (x == num) {
                    existInNums2 = true;
                    break;
                }
            }
            if (!existInNums2) {
                onlyInNums1.insert(num);
            }
        }
        return vector<int> (onlyInNums1.begin(), onlyInNums1.end());
    }

    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        return {getElementsOnlyInFirstList(nums1, nums2), getElementsOnlyInFirstList(nums2, nums1)};
    }
};
