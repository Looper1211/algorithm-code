# coding = utf-8
"""
单链表
"""
class ListNode(object):
    """
    结点，包含结点存储的值 val 和指向下一个结点的引用 next
    """
    def __init__(self,val):
        self.val = val
        self.next = None
    
class LinkedList(object):
    def __init__(self):
        # 初始化头结点
        self.head = ListNode(0)
    
    def insert(self,val):
        """
        头插法
        """
        new_node  = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
    
    def append(self,val):
        """
        尾插法
        """
        new_node  = ListNode(val)
        p = self.head
        while p.next:
            p = p.next
        p.next = new_node
    
    def delete(self,val):
        """
        删除链表中值为val的结点
        """
        p = self.head
        while p.next:
            if p.next.val == val:
                break
            p = p.next
        if not p.next:
            return False
        p.next = p.next.next
        return True
    

    def insert_index(self,val,index):
        """
        在链表指定位置插入一个值为val的结点
        """
        p = self.head
        i = 0
        while p.next and i < index-1:
            p = p.next
            i += 1
        new_node = ListNode(val)
        new_node.next = p.next
        p.next = new_node

    def print_list(self):
        p = self.head
        while p.next:
            print(" {} > ".format(p.next.val),end = "")
            p = p.next
        print("None")


def main():
    list1 = LinkedList()
    list1.append(1)
    list1.append(2)
    list1.append(4)
    list1.insert_index(3,3)
    list1.insert_index(5,1)
    list1.delete(4)
    list1.print_list()


if __name__ == '__main__':
    main()