// Submission title: Unique Number of Occurrences
// Submission url  : https://leetcode.com/problems/unique-number-of-occurrences/description/
// Submission url  : https://leetcode.com/submissions/detail/1100099074/"

class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        std::unordered_map<int, int> counts;
        std::unordered_set<int> encountered;
        for (int num : arr) {
            counts[num] += 1;
        }
        for (const auto [num, count] : counts) {
            if (encountered.find(count) == encountered.end()) {
                encountered.insert(count);
            } else {
                return false;
            }
        }
        return true;
    }
};
