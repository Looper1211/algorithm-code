# coding = utf-8
"""
队列 顺序队列和链式队列
"""

class Node(object):
    """
    结点，包含结点存储的值 val 和指向下一个结点的引用 next
    """
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue(object):
    def __init__(self):
        self.head = None
        self.rear = None
        self.length = 0
    
    def is_empty(self):
        """
        判断队列是否为空
        """
        return self.length == 0

    def push(self,val):
        """
        进队列
        """
        new_node = Node(val)
        if self.is_empty():
            self.head = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.length += 1

    def pop(self):
        """
        出队列
        """
        if self.is_empty():
            return None
        val = self.head.val
        self.head = self.head.next
        self.length -= 1
        return val


# class Queue(object):
#     def __init__(self):
#         self.data = []

#     def is_empty(self):
#         return len(self.data) == 0
    
#     def push(self,val):
#         self.data.append(val)

#     def pop(self):
#         if self.is_empty():
#             return None
#         return self.data.pop(0)

    
def main():
    queue = Queue()
    queue.push(3)
    queue.push(4)
    queue.push(5)
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())


if __name__ == '__main__':
    main()