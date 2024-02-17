// Submission title: Move Zeroes
// Submission url  : https://leetcode.com/problems/move-zeroes/description/"
// Submission url  : https://leetcode.com/submissions/detail/1096515278/"

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
