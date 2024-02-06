// Submission title: for Dota2 Senate
// Submission url  : https://leetcode.com/submissions/detail/1100801416/
// Submission json : {"id": 1100801416, "status_display": "Accepted", "lang": "cpp", "question_id": 649, "title_slug": "dota2-senate", "code": "class Solution {\npublic:\n    string predictPartyVictory(string senate) {\n        std::queue<int> rad, dir;\n        unsigned long length {senate.size()};\n        for (int i = 0; i < length; ++i){\n            if (senate[i] == 'R'){\n                rad.push(i);\n            } else {\n                dir.push(i);\n            }\n        }\n        while (!rad.empty() && !dir.empty()) {\n            if (rad.front() < dir.front()) {\n                rad.push(length);\n            } else {\n                dir.push(length);\n            }\n            ++length;\n            rad.pop();\n            dir.pop();\n        }\n        return rad.empty() ? \"Dire\" : \"Radiant\";\n    }\n};", "title": "Dota2 Senate", "url": "/submissions/detail/1100801416/", "lang_name": "C++", "time": "2\u00a0months, 2\u00a0weeks", "timestamp": 1700228496, "status": 10, "runtime": "6 ms", "is_pending": "Not Pending", "memory": "8.4 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}



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
