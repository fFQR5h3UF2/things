// Submission title: Dota2 Senate
// Submission url  : https://leetcode.com/problems/dota2-senate/description/
// Submission url  : https://leetcode.com/submissions/detail/1100801416/"

class Solution {
public:
    string predictPartyVictory(string senate) {
        std::queue<int> rad, dir;
        unsigned long length {senate.size()};
        for (int i = 0; i < length; ++i){
            if (senate[i] == 'R'){
                rad.push(i);
            } else {
                dir.push(i);
            }
        }
        while (!rad.empty() && !dir.empty()) {
            if (rad.front() < dir.front()) {
                rad.push(length);
            } else {
                dir.push(length);
            }
            ++length;
            rad.pop();
            dir.pop();
        }
        return rad.empty() ? "Dire" : "Radiant";
    }
};
