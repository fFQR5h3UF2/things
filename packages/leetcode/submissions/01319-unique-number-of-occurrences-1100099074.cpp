// Submission title: for Unique Number of Occurrences
// Submission url  : https://leetcode.com/submissions/detail/1100099074/
// Submission json : {"id": 1100099074, "status_display": "Accepted", "lang": "cpp", "question_id": 1319, "title_slug": "unique-number-of-occurrences", "code": "class Solution {\npublic:\n    bool uniqueOccurrences(vector<int>& arr) {\n        std::unordered_map<int, int> counts;\n        std::unordered_set<int> encountered;\n        for (int num : arr) {\n            counts[num] += 1;\n        }\n        for (const auto [num, count] : counts) {\n            if (encountered.find(count) == encountered.end()) {\n                encountered.insert(count);\n            } else {\n                return false;\n            }\n        }\n        return true;\n    }\n};", "title": "Unique Number of Occurrences", "url": "/submissions/detail/1100099074/", "lang_name": "C++", "time": "2\u00a0months, 2\u00a0weeks", "timestamp": 1700142179, "status": 10, "runtime": "5 ms", "is_pending": "Not Pending", "memory": "8.7 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}



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
