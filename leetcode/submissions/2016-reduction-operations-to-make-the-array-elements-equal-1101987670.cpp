// Submission for Reduction Operations to Make the Array Elements Equal
// Submission url: https://leetcode.com/submissions/detail/1101987670/



class Solution {
public:
    int reductionOperations(vector<int>& nums) {
        std::map<int, int> counts;
        for (int num : nums) {
            ++counts[num];
        }
        auto length {counts.size()};
        if (length == 1) {
            return 0;
        }
        int cur {0};
        auto last = counts.rend();
        --last;
        for (auto it = counts.rbegin(); it != last ; ++it) {
            cur += cur + it->second;
        }
        return cur;
    }
};
