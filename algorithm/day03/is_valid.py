# coding = utf-8
"""
leetcode 20
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
"""
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict1 = {"(":")","{":"}","[":"]"}
        stack = []
        for item in s:
            if item in dict1.keys():
                stack.append(item)
            else:
                if len(stack)==0:
                    return False
                if dict1[stack.pop()] != item:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
