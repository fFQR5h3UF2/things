// Submission title: for Minimum Amount of Time to Collect Garbage
// Submission url  : https://leetcode.com/submissions/detail/1102661782/
// Submission json : {"id": 1102661782, "status_display": "Accepted", "lang": "cpp", "question_id": 2471, "title_slug": "minimum-amount-of-time-to-collect-garbage", "code": "class Solution {\npublic:\n    int garbageCollection(vector<string>& garbage, vector<int>& travel) {\n        vector<int> prefixSum(travel.size() + 1, 0);\n        prefixSum[1] = travel[0];\n        for (int i = 1; i < travel.size(); i++) {\n            prefixSum[i + 1] = prefixSum[i] + travel[i];\n        }\n        unordered_map<char, int> garbageLastPos;\n        unordered_map<char, int> garbageCount;\n        for (int i = 0; i < garbage.size(); i++) {\n            for (char c : garbage[i]) {\n                garbageLastPos[c] = i;\n                garbageCount[c]++;\n            }\n        }\n        char garbageTypes[3] = {'M', 'P', 'G'};\n        int ans = 0;\n        for (char c : garbageTypes) {\n            if (garbageCount[c]) {\n                ans += prefixSum[garbageLastPos[c]] + garbageCount[c];\n            }\n        }\n        return ans;\n    }\n};", "title": "Minimum Amount of Time to Collect Garbage", "url": "/submissions/detail/1102661782/", "lang_name": "C++", "time": "2\u00a0months, 2\u00a0weeks", "timestamp": 1700478707, "status": 10, "runtime": "214 ms", "is_pending": "Not Pending", "memory": "104.2 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}



class Solution {
public:
    int garbageCollection(vector<string>& garbage, vector<int>& travel) {
        vector<int> prefixSum(travel.size() + 1, 0);
        prefixSum[1] = travel[0];
        for (int i = 1; i < travel.size(); i++) {
            prefixSum[i + 1] = prefixSum[i] + travel[i];
        }
        unordered_map<char, int> garbageLastPos;
        unordered_map<char, int> garbageCount;
        for (int i = 0; i < garbage.size(); i++) {
            for (char c : garbage[i]) {
                garbageLastPos[c] = i;
                garbageCount[c]++;
            }
        }
        char garbageTypes[3] = {'M', 'P', 'G'};
        int ans = 0;
        for (char c : garbageTypes) {
            if (garbageCount[c]) {
                ans += prefixSum[garbageLastPos[c]] + garbageCount[c];
            }
        }
        return ans;
    }
};
