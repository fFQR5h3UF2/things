// Submission for Kth Largest Element in an Array
// Submission url: https://leetcode.com/submissions/detail/1100038369/



class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        std::make_heap(nums.begin(), nums.end());
        return nums[k-1];
    }
};
