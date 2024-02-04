// Submission for Dota2 Senate
// Submission url: https://leetcode.com/submissions/detail/1100797824/



class Solution {
public:
    string predictPartyVictory(string senate) {
        unsigned long length {senate.size()};
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
            bool isD {!isR};
            if (isR && banR == 0) {
                ++banD;
                --countD;
            } else if (isR) {
                --banR;
            } else if (isD && banD == 0) {
                ++banR;
                --countR;
            } else if (isD) {
                --banD;
            }
            if (countR == 0 || countD == 0) {
                break;
            }
        }
        if (countR > countD) {
            return "Radiant";
        }
        return "Dire";
    }
};
