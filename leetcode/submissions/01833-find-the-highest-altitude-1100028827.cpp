// Submission title: Find the Highest Altitude
// Submission url  : https://leetcode.com/problems/find-the-highest-altitude/description/
// Submission url  : https://leetcode.com/submissions/detail/1100028827/
// Submission json : {"id":1100028827,"status_display":"Accepted","lang":"cpp","question_id":1833,"title_slug":"find-the-highest-altitude","code":"class Solution {\npublic:\n    int largestAltitude(vector<int>& gain) {\n        int att {0}, maxAtt {0};\n        for (int num : gain) {\n            att += num;\n            maxAtt = max(maxAtt, att);\n        }\n        return maxAtt;\n    }\n};","title":"Find the Highest Altitude","url":"/submissions/detail/1100028827/","lang_name":"C++","time":"2 months, 2 weeks","timestamp":1700132790,"status":10,"runtime":"0 ms","is_pending":"Not Pending","memory":"8.4 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}

class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int att {0}, maxAtt {0};
        for (int num : gain) {
            att += num;
            maxAtt = max(maxAtt, att);
        }
        return maxAtt;
    }
};
