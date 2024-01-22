class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in s:
            if i != '*':
                stack.append(i)
                
            else:
                stack.pop(-1)
                
        ans = ''
        for i in stack:
            ans += i
            
        return ans
        