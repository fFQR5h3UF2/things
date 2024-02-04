// Submission for Two Sum
// Submission url: https://leetcode.com/submissions/detail/1096529076/



class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::map<int, int> numToIndex;
        int length = nums.size();
        for (int i = 0; i < length; ++i) {
            int num = nums[i];
            int diff = target - num;
            if (numToIndex.contains(diff)) {
                return std::vector<int>{numToIndex[diff], i}
            }
            numToIndex[num] = i;
        }
    }
};
