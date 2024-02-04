// Submission for Dota2 Senate
// Submission url: https://leetcode.com/submissions/detail/1100794798/



class Solution {
public:
    string predictPartyVictory(string senate) {
        unsigned long length {senate.size()};
        if (length == 1 && senate[0] == 'D') {
            return "Dire";
        } else if (length == 1) {
            return "Radiant";
        }
        int countR {0}, countD {0};
        int banR {0}, banD {0};
        for (char c : senate) {
            if (c == 'R') {
                ++countR;
            } else {
                ++countD;
            }
        }
        for (char c : senate) {
            bool isR {c == 'R'};
            if (isR && banR == 0) {
                ++banD;
                --countD;
            } else if (isR) {
                --banR;
            } else if (!isR && banD == 0) {
                ++banR;
                --countR;
            } else if (!isR) {
                --banD;
            }
            if (countR == 0 || countD == 0) {
                break;
            }
        }
        if (countD == 0) {
            return "Dire";
        }
        return "Radiant";
    }
};
