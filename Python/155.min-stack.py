#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#
# https://leetcode.com/problems/min-stack/description/
#
# algorithms
# Easy (40.06%)
# Likes:    2435
# Dislikes: 255
# Total Accepted:    390.2K
# Total Submissions: 970.1K
# Testcase Example:
#   '["MinStack","push","push","push","getMin","pop","top","getMin"]\n'
#   '[[],[-2],[0],[-3],[],[],[],[]]'
#
# Design a stack that supports push, pop, top, and retrieving the minimum
# element in constant time.
#
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
#
#
#
#
# Example:
#
#
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.
#
#
#
#
#

# @lc code=start


class MinStack:

    def __init__(self):
        # self.curr_stack = StackMinStack()
        self.curr_stack = LLMinStack()

    def push(self, x: int) -> None:
        self.curr_stack.push(x)

    def pop(self) -> None:
        self.curr_stack.pop()

    def top(self) -> int:
        return self.curr_stack.top()

    def getMin(self) -> int:
        return self.curr_stack.getMin()


class StackMinStack:
    """
    Use two stack to keep track of both the stack and the min
    only append min_stack if value is smaller than the curr min in min_stack
    """

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.min_stack) == 0 or x <= self.getMin():
            self.min_stack.append(x)

    def pop(self) -> None:
        if self.stack[-1] == self.getMin():
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


class Node:
    val: int
    min_val: int
    next: 'Node'

    def __init__(self, val, min_val):
        self.val = val
        self.min_val = min_val
        self.next = None


class LLMinStack:
    """
    Use Linked List to keep track of stack and min
    """

    def __init__(self):
        self.head = None

    def push(self, x: int) -> None:
        if self.head is None:
            self.head = Node(x, x)
        else:
            temp = Node(x, min(self.head.min_val, x))
            temp.next = self.head
            self.head = temp

    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.min_val

# @lc code=end


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin(), -3)
    minStack.pop()
    print(minStack.top(), 0)
    print(minStack.getMin(), -2)
