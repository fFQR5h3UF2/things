// Submission title: Implement Stack using Queues
// Submission url  : https://leetcode.com/problems/implement-stack-using-queues/description/
// Submission url  : https://leetcode.com/submissions/detail/1095927384/
// Submission json : {"id":1095927384,"status_display":"Accepted","lang":"cpp","question_id":225,"title_slug":"implement-stack-using-queues","code":"class MyStack {\npublic:\n    std::vector<int> v;\n\n    MyStack() {\n        this->v = {};\n    }\n    \n    void push(int x) {\n        this->v.push_back(x);\n    }\n    \n    int pop() {\n        int last = this->v.back();\n        this->v.pop_back();\n        return last;\n    }\n    \n    int top() {\n        return this->v.back();\n    }\n    \n    bool empty() {\n        return this->v.empty();\n    }\n};\n\n/**\n * Your MyStack object will be instantiated and called as such:\n * MyStack* obj = new MyStack();\n * obj->push(x);\n * int param_2 = obj->pop();\n * int param_3 = obj->top();\n * bool param_4 = obj->empty();\n */","title":"Implement Stack using Queues","url":"/submissions/detail/1095927384/","lang_name":"C++","time":"2 months, 3 weeks","timestamp":1699623033,"status":10,"runtime":"0 ms","is_pending":"Not Pending","memory":"7.1 MB","compare_result":"111111111111111111","has_notes":false,"flag_type":1}

class MyStack {
public:
    std::vector<int> v;

    MyStack() {
        this->v = {};
    }

    void push(int x) {
        this->v.push_back(x);
    }

    int pop() {
        int last = this->v.back();
        this->v.pop_back();
        return last;
    }

    int top() {
        return this->v.back();
    }

    bool empty() {
        return this->v.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */
