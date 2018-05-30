# coding = utf-8
"""
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

    push(x) -- 将元素 x 推入栈中。
    pop() -- 删除栈顶的元素。
    top() -- 获取栈顶元素。
    getMin() -- 检索栈中的最小元素。
    
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.stack_min = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if (len(self.stack_min) == 0) or (len(self.stack_min) != 0 and self.stack_min[-1] >= x):
            self.stack_min.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack):
            if len(self.stack_min):
                if self.stack[-1] == self.stack_min[-1]:
                    self.stack_min.pop()
            self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack):
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack_min):
            return self.stack_min[-1]



# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(1)
obj.push(2)
print(obj.top())
print(obj.getMin())
obj.pop()
print(obj.getMin())
print(obj.top())
