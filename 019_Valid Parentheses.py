class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        try:        
            for char in s:
                if char == '(' or char == '[' or char == '{':
                    stack.append(char)
                elif char == ')':
                    if '(' != stack.pop():
                        return False
                elif char == ']':
                    if '[' != stack.pop():
                        return False
                elif char == '}':
                    if '{' != stack.pop():
                        return False
        except:
            return False
        if len(stack) > 0:
            return False
        return True

print Solution().isValid("]")