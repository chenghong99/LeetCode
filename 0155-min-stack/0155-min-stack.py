class MinStack(object):

    def __init__(self):
        self.stack = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if len(self.stack) == 0:
            self.stack.append((val, val))
        else:
            prev_min = self.stack[-1][1]
            if val > prev_min:
                self.stack.append((val, prev_min))
            else:
                self.stack.append((val, val))

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop(-1)
        

    def top(self):
        """
        :rtype: int
        """
        top_val = self.stack[-1][0]
        return top_val
        

    def getMin(self):
        """
        :rtype: int
        """
        min_val = self.stack[-1][1]
        return min_val
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()