# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode.com/problems/validate-binary-search-tree/

# Method 1 : O(N) time and O(N) space
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

# O(N) time but O(1) space
class Solution1:
	lastSeen = -1
	def inOrder(self,root):
		if(root is None):
			return True
		
		if(not self.inOrder(self.inOrder(root.left))):
			return False
		
		if(self.lastSeen != -1 and self.lastSeen >= root.val):
			return False
		self.lastSeen = root.val

		if(not self.inOrder(self.inOrder(root.right))):
			return False

		return True
    
	def isValidBST(self, root: TreeNode) -> bool:
		return self.inOrder(root)