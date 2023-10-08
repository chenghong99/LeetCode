class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        for i in s:
            if i in ['(', '[', '{']:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                else:
                    para = stack.pop(-1)
                    if i == ')' and para != '(':
                        return False
                    elif i == ']' and para != "[":
                        return False
                    elif i == '}' and para != "{":
                        return False
        if len(stack) != 0:
            return False
        return True
        