// Submission for Increasing Triplet Subsequence
// Submission url: https://leetcode.com/submissions/detail/1099377583/



class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        auto length{nums.size()};
        for (int i = 0; i < length; ++i) {
            int num1 = nums[i];
            for (int j = i + 1; j < length; ++j) {
                int num2 = nums[j];
                if (num2 <= num1) {
                    continue;
                }
                for (int k = j + 1; k < length; ++k) {
                    if (nums[k] > num2) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
};
