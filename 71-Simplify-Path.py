"""
71.Simplify Path
判断两个’/’之间的字符串：字母串-> 入栈；.. -> 出栈；. -> 不作处理。最后将栈中的元素组合得到结果。

"""
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        i = 0
        output = []
        
        while i<len(path):
            while i<len(path) and path[i] == '/':
                i+=1
            start = i
            while i<len(path) and path[i] != '/':
                i+=1
            strr = path[start:i]
            if strr == '..':
                if output:
                    output.pop()
            elif strr == '.':
                continue
            elif strr:
                output.append(strr)
        if not output:
            return '/'
        return ''.join('/'+value for value in output )
