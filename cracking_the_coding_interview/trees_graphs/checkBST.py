# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode.com/problems/validate-binary-search-tree/

class Solution:
    result = []
    def inOrder(self,root):
        if(root is None):
            return
        self.inOrder(root.left)
        self.result.append(root.val)
        self.inOrder(root.right)
        
    def isValidBST(self, root: TreeNode) -> bool:
        self.result = []
        if(root == None or (root.left == None and root.right == None)):
            return True
        self.inOrder(root)
        # print(self.result)
        for i in range(1,len(self.result)):
            if(self.result[i] <= self.result[i-1]):
                return False
        return True