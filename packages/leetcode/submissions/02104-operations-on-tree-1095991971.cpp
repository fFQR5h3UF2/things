// Submission title: for Operations on Tree
// Submission url  : https://leetcode.com/submissions/detail/1095991971/
// Submission json : {"id": 1095991971, "status_display": "Accepted", "lang": "cpp", "question_id": 2104, "title_slug": "operations-on-tree", "code": "class LockingTree {\npublic:\n    std::vector<int> parents, locked;\n    std::vector<std::vector<int>> children;\n    LockingTree(vector<int>& parent) {\n        int length = parent.size();\n        this->children.resize(length);\n        this->locked.resize(length, -1);\n        this->parents = parent;\n        for (int i = 1; i < length; ++i) {\n            this->children[this->parents[i]].push_back(i);\n        }\n    }\n    \n    bool lock(int num, int user) {\n        if (this->locked[num] != -1) {\n            return false;\n        }\n        this->locked[num] = user;\n        return true;\n    }\n    \n    bool unlock(int num, int user) {\n        if (this->locked[num] != user) {\n            return false;\n        }\n        this->locked[num] = -1;\n        return true;\n    }\n\n    bool upgrade(int num, int user) {\n        if (this->locked[num] != -1) {\n            return false;\n        }\n        int parent = this->parents[num];\n        while (parent != -1) {\n            if (this->locked[parent] != -1) {\n                return false;\n            }\n            parent = this->parents[parent];\n        }\n        if (!this->unlockDesc(num)) {\n            return false;\n        }\n        this->locked[num] = user;\n        return true;\n    }\n\n    bool unlockDesc(int parent) {\n        bool hasLocked = false;\n        for (auto const& child : this->children[parent]) {\n            if (this->locked[child] != -1) {\n                this->locked[child] = -1;\n                hasLocked = true;\n            }\n            bool descHasLocked = unlockDesc(child);\n            if (descHasLocked) {\n                hasLocked = true;\n            }\n        }\n        return hasLocked;\n    }\n};\n\n/**\n * Your LockingTree object will be instantiated and called as such:\n * LockingTree* obj = new LockingTree(parent);\n * bool param_1 = obj->lock(num,user);\n * bool param_2 = obj->unlock(num,user);\n * bool param_3 = obj->upgrade(num,user);\n */", "title": "Operations on Tree", "url": "/submissions/detail/1095991971/", "lang_name": "C++", "time": "2\u00a0months, 3\u00a0weeks", "timestamp": 1699630679, "status": 10, "runtime": "291 ms", "is_pending": "Not Pending", "memory": "123.5 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}



class LockingTree {
public:
    std::vector<int> parents, locked;
    std::vector<std::vector<int>> children;
    LockingTree(vector<int>& parent) {
        int length = parent.size();
        this->children.resize(length);
        this->locked.resize(length, -1);
        this->parents = parent;
        for (int i = 1; i < length; ++i) {
            this->children[this->parents[i]].push_back(i);
        }
    }

    bool lock(int num, int user) {
        if (this->locked[num] != -1) {
            return false;
        }
        this->locked[num] = user;
        return true;
    }

    bool unlock(int num, int user) {
        if (this->locked[num] != user) {
            return false;
        }
        this->locked[num] = -1;
        return true;
    }

    bool upgrade(int num, int user) {
        if (this->locked[num] != -1) {
            return false;
        }
        int parent = this->parents[num];
        while (parent != -1) {
            if (this->locked[parent] != -1) {
                return false;
            }
            parent = this->parents[parent];
        }
        if (!this->unlockDesc(num)) {
            return false;
        }
        this->locked[num] = user;
        return true;
    }

    bool unlockDesc(int parent) {
        bool hasLocked = false;
        for (auto const& child : this->children[parent]) {
            if (this->locked[child] != -1) {
                this->locked[child] = -1;
                hasLocked = true;
            }
            bool descHasLocked = unlockDesc(child);
            if (descHasLocked) {
                hasLocked = true;
            }
        }
        return hasLocked;
    }
};

/**
 * Your LockingTree object will be instantiated and called as such:
 * LockingTree* obj = new LockingTree(parent);
 * bool param_1 = obj->lock(num,user);
 * bool param_2 = obj->unlock(num,user);
 * bool param_3 = obj->upgrade(num,user);
 */
