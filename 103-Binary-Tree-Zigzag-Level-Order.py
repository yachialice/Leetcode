"""
103.Binary Tree Zigzag Level Order Traveral
使用队列，每一层node出队后储存在一个list中，再按照node.left，
node.right顺序令子节点入队。再判断len(res)，考虑是否要颠倒此层list的顺序。
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = []
        res = []
        if root:
            queue.append(root)
        else:
            return []
        
        while queue:
            r = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                r.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            
            r = r[::-1] if len(res)%2 else r
            res.append(r)
        return res
