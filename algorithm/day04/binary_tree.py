# coding = utf-8
"""
二叉树的创建和遍历
"""


class TreeNode(object):
    """
    结点，包含结点存储的值 val 和 左边儿子结点的引用、右边儿子结点的引用
    """

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Binary_Tree(object):

    def __init__(self,data):
        
        self.data = data
        self.index = 0
        self.root = self.create_tree()

    def create_tree(self):
        """
        创建二叉树
        """
        val = self.data[self.index]
        self.index += 1
        if val == None:
            node = None
        else:
            # 创建一个结点
            node = TreeNode(val)
            # 创建左子树结点
            node.left = self.create_tree()
            # 创建右子树结点
            node.right = self.create_tree()
        return node

    def pre_traverse(self, node):
        """
        前序遍历
        """
        if node:
            print(node.val+" ",end="")
            self.pre_traverse(node.left)
            self.pre_traverse(node.right)

    def mid_traverse(self, node):
        """
        中序遍历
        """
        if node:
            self.mid_traverse(node.left)
            print(node.val+" ",end="")
            self.mid_traverse(node.right)

    def post_traverse(self,node):
        """
        后序遍历
        """
        if node:
            self.post_traverse(node.left)
            self.post_traverse(node.right)
            print(node.val+" ",end="")
    
    def level_traverse(self,root):
        """
        层序遍历
        """
        if root:
            queue = []
            queue.append(root)
            while len(queue):
                node = queue.pop(0)
                print(node.val+" ",end="")
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
                


def main():
    data = ['1','2',None,None,'3',None,None]
    tree = Binary_Tree(data)
    tree.pre_traverse(tree.root)
    print("")
    tree.mid_traverse(tree.root)
    print("")
    tree.post_traverse(tree.root)
    print("")
    tree.level_traverse(tree.root)
    print("")


if __name__ == '__main__':
    main()
