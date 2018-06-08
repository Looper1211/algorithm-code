"""
BST-二叉搜索树，又称为二叉排序树，每个结点的值大于它的左儿子结点的值，小于它的右儿子结点的值
"""


class TreeNode(object):
    """
    结点，包含结点存储的值 val 和 左边儿子结点的引用、右边儿子结点的引用
    """

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST(object):
    def __init__(self):
        self.root = None

    def insert_tree(self, node, val):
        """
        插入一个值到二叉树中
        """
        if not node:
            node = TreeNode(val)
            return node

        if val < node.val:
            node.left = self.insert_tree(node.left, val)
        else:
            node.right = self.insert_tree(node.right, val)
        return node

    def query(self, node, val):
        """
        
        """
        if not node:
            return False
        if node.val == val:
            return True
        if node.val > val:
            return self.query(node.left, val)
        else:
            return self.query(node.right, val)

    def pre_traverse(self, node):
        """
        前序遍历
        """
        if node:
            print(node.val+" ", end="")
            self.pre_traverse(node.left)
            self.pre_traverse(node.right)

    def mid_traverse(self, node):
        """
        中序遍历
        """
        if node:
            self.mid_traverse(node.left)
            print(str(node.val)+" ", end="")
            self.mid_traverse(node.right)

    def post_traverse(self, node):
        """
        后序遍历
        """
        if node:
            self.post_traverse(node.left)
            self.post_traverse(node.right)
            print(node.val+" ", end="")

    def level_traverse(self, root):
        """
        层序遍历
        """
        if root:
            queue = []
            queue.append(root)
            while len(queue):
                node = queue.pop(0)
                print(node.val+" ", end="")
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)


def main():
    bst = BST()
    bst.root = bst.insert_tree(bst.root, 10)
    bst.root = bst.insert_tree(bst.root, 5)
    bst.root = bst.insert_tree(bst.root, 7)
    bst.root = bst.insert_tree(bst.root, 9)
    bst.root = bst.insert_tree(bst.root, 8)
    bst.mid_traverse(bst.root)


if __name__ == '__main__':
    main()
