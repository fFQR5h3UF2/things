// Submission title: Kth Largest Element in an Array
// Submission url  : https://leetcode.com/problems/kth-largest-element-in-an-array/description/"
// Submission url  : https://leetcode.com/submissions/detail/1100039261/"

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end(), std::greater<int>());
        return nums[k-1];
    }
};
