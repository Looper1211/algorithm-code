"""
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1

返回:

[
   [5,4,11,2],
   [5,8,4,5]
]

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        path = []
        self.find(root, sum, res, path)
        return res

    def find(self, root, sum, res, path):
        if not root:
            return
        sum -= root.val
        path.append(root.val)
        if sum == 0 and root.left == None and root.right == None:
            temp = []
            temp.extend(path)
            res.append(temp)
        self.find(root.left, sum, res, path)
        self.find(root.right, sum, res, path)
        path.pop()
