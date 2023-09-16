class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        ans = [0 for i in range(len(temperatures))]
        
        stack = []
        
        for i in range(len(temperatures)):
            if len(stack) == 0:
                stack.append((i, temperatures[i]))
            elif stack[-1][1] < temperatures[i]:
                while len(stack) > 0:
                    if stack[-1][1] < temperatures[i]:
                        prev_day = stack.pop(-1)
                        ans[prev_day[0]] = i - prev_day[0]
                    else:
                        break
                stack.append((i, temperatures[i]))
            else:
                stack.append((i, temperatures[i]))
        return ans
                
        