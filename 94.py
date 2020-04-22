
#94. Binary Tree Inorder Traversal
"""
递归方法注意在递归函数前加self。迭代方法思路为令root的left child node一直入栈，并令left child node作为新的root。
当root为空时，说明遍历到最左节点，此时出栈一个node，加入output，令node.right作为新的root继续遍历。
注意if not stack ...不能加载if not root后，否则可能会在最初的根结点提前结束循环。
"""


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
