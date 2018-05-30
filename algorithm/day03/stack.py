# coding = utf-8
"""
顺序栈与链式栈
"""

class Node(object):
    """
    结点，包含结点存储的值 val 和指向下一个结点的引用 next
    """
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack(object):
    """
    链式栈
    """
    def __init__(self):
        self.top = None
        self.length = 0

    def push(self, val):
        """
        指定元素创建结点并进栈
        """
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node
        self.length += 1

    def pop(self):
        """
        栈顶元素出栈，并返回栈顶结点对应的val，返回None代表栈为空
        """
        val = None
        if self.is_empty():
            val = self.top.val
            self.top = self.top.next
            self.length -= 1
        return val

    def is_empty(self):
        """
        判断栈是否为空 
        """
        # return self.length == 0
        return self.top == None

    def get_top(self):
        """
        返回栈顶元素的值
        """
        if not self.is_empty():
            return self.top.val
    

# class Stack(object):
#     def __init__(self):
#         self.data = []
    
#     def push(self,val):
#         self.data.append(val)
    
#     def pop(self):
#         if len(self.data): 
#             return self.data.pop()
#         else:
#             return None


def main():
    stack = Stack()
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())


if __name__ == '__main__':
    main()
