// Submission title: Implement Stack using Queues
// Submission url  : https://leetcode.com/problems/implement-stack-using-queues/description/
// Submission url  : https://leetcode.com/submissions/detail/1095927384/"

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
