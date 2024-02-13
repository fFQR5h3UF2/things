// Submission title: Number of Ways to Divide a Long Corridor
// Submission url  : https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/description/
// Submission url  : https://leetcode.com/submissions/detail/1108067184/
// Submission json : {"id":1108067184,"status_display":"Accepted","lang":"cpp","question_id":2251,"title_slug":"number-of-ways-to-divide-a-long-corridor","code":"class Solution {\npublic:\n    // Store 1000000007 in a variable for convenience\n    const int MOD = 1e9 + 7;\n    \n    // Count the number of ways to divide from \"index\" to the last index\n    // with \"seats\" number of \"S\" in the current section\n    int count(int index, int seats, string& corridor, int cache[][3]) {\n        // If we have reached the end of the corridor, then\n        // the current section is valid only if \"seats\" is 2\n        if (index == corridor.length()) {\n            return seats == 2 ? 1 : 0;\n        }\n\n        // If we have already computed the result of this sub-problem,\n        // then return the cached result\n        if (cache[index][seats] != -1) {\n            return cache[index][seats];\n        }\n\n        // Result of the sub-problem\n        int result = 0;\n\n        // If the current section has exactly 2 \"S\"\n        if (seats == 2) {\n            // If the current element is \"S\", then we have to close the\n            // section and start a new section from this index. Next index\n            // will have one \"S\" in the current section\n            if (corridor[index] == 'S') {\n                result = count(index + 1, 1, corridor, cache);\n            } else {\n                // If the current element is \"P\", then we have two options\n                // 1. Close the section and start a new section from this index\n                // 2. Keep growing the section\n                result = (count(index + 1, 0, corridor, cache) + count(index + 1, 2, corridor, cache)) % MOD;  \n            }\n        } else {\n            // Keep growing the section. Increment \"seats\" if present\n            // element is \"S\"\n            if (corridor[index] == 'S') {\n                result = count(index + 1, seats + 1, corridor, cache);\n            } else {\n                result = count(index + 1, seats, corridor, cache);\n            }\n        }\n\n        // Memoize the result, and return it\n        cache[index][seats] = result;\n        return cache[index][seats];\n    }\n\n    int numberOfWays(string corridor) {\n        // Cache the result of each sub-problem\n        int cache[corridor.length()][3];\n        memset(cache, -1, sizeof(cache));\n\n        // Call the count function\n        return count(0, 0, corridor, cache);\n    }\n};","title":"Number of Ways to Divide a Long Corridor","url":"/submissions/detail/1108067184/","lang_name":"C++","time":"2 months, 1 week","timestamp":1701165881,"status":10,"runtime":"177 ms","is_pending":"Not Pending","memory":"40.2 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}

class Solution {
public:
    // Store 1000000007 in a variable for convenience
    const int MOD = 1e9 + 7;

    // Count the number of ways to divide from "index" to the last index
    // with "seats" number of "S" in the current section
    int count(int index, int seats, string& corridor, int cache[][3]) {
        // If we have reached the end of the corridor, then
        // the current section is valid only if "seats" is 2
        if (index == corridor.length()) {
            return seats == 2 ? 1 : 0;
        }

        // If we have already computed the result of this sub-problem,
        // then return the cached result
        if (cache[index][seats] != -1) {
            return cache[index][seats];
        }

        // Result of the sub-problem
        int result = 0;

        // If the current section has exactly 2 "S"
        if (seats == 2) {
            // If the current element is "S", then we have to close the
            // section and start a new section from this index. Next index
            // will have one "S" in the current section
            if (corridor[index] == 'S') {
                result = count(index + 1, 1, corridor, cache);
            } else {
                // If the current element is "P", then we have two options
                // 1. Close the section and start a new section from this index
                // 2. Keep growing the section
                result = (count(index + 1, 0, corridor, cache) + count(index + 1, 2, corridor, cache)) % MOD;
            }
        } else {
            // Keep growing the section. Increment "seats" if present
            // element is "S"
            if (corridor[index] == 'S') {
                result = count(index + 1, seats + 1, corridor, cache);
            } else {
                result = count(index + 1, seats, corridor, cache);
            }
        }

        // Memoize the result, and return it
        cache[index][seats] = result;
        return cache[index][seats];
    }

    int numberOfWays(string corridor) {
        // Cache the result of each sub-problem
        int cache[corridor.length()][3];
        memset(cache, -1, sizeof(cache));

        // Call the count function
        return count(0, 0, corridor, cache);
    }
};
