// Submission for Merge Strings Alternately
// Submission url: https://leetcode.com/submissions/detail/1096031957/



class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int l1 = word1.size(), l2 = word2.size();
        string result = "";
        int i = 0, j = 0;

        while (i < m || j < n) {
            if (i < m) {
                result.push_back(word1[i++]);
            }
            if (j < n) {
                result.push_back(word2[j++]);
            }
        }

        return result;
    }
};
