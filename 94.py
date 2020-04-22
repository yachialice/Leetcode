
#94. Binary Tree Inorder Traversal


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    
    #Recursive Method
    def inorderTraversal(self, root):
        #:type root: TreeNode
        #:rtype: List[int]
        output = []
        self.inOrder(root,output)
        return output
            
    def inOrder(self, root,output):
        if root:
            self.inOrder (root.left, output)
            output.append(root.val)
            self.inOrder(root.right, output)   
   #Iterative Method
    def inorderTraversal(self, root):
        
        stack = []
        output=[]
        while True:
            if root:
                stack.append(root)
                root = root.left
            if not stack:
                break            
            if not root:
                a = stack.pop()
                output.append(a.val)
                root = a.right 

        return output