// Submission for Dota2 Senate
// Submission url: https://leetcode.com/submissions/detail/1100791276/



class Solution {
public:
    string predictPartyVictory(string senate) {
        unsigned long length {senate.size()};
        int queue {0};
        for (char c : senate) {
            if (c == 'R') {
                ++queue;
            } else {
                --queue;
            }
        }
        if (queue >= 0) {
            return "Radiant";
        }
        return "Dire";
    }
};
