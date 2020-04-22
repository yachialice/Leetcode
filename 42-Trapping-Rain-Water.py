"""
42.Trapping Rain Water

栈中存放潜在left border， 若当前值小于栈顶元素，不能形成容器，则入栈；若当前值大于栈顶元素时，
可能构成容器，出栈匹配left border，计算water。
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        water = 0
        for i, value in enumerate(height):
            #there might be an right border
            while stack and value >stack[-1][1]:
                _, popped = stack.pop()
                #is there and left border to form an container?
                if stack:
                    j, left_border = stack[-1]
                    water += min(left_border-popped, value-popped) * (i-j-1)
            stack.append((i,value))

        return water
