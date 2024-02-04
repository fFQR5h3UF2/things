// Submission for Move Zeroes
// Submission url: https://leetcode.com/submissions/detail/1096516231/



class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int length = nums.size();
        int lastNonZeroFoundAt = 0;
        for (int i = 0; cur < length; ++cur) {
            if (nums[cur] != 0) {
                swap(nums[i], nums[cur]);
                lastNonZeroFoundAt += 1;
            }
        }
    }
};
