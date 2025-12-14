class Solution(object):
    def countCollisions(self, directions):
        """
        :type directions: str
        :rtype: int
        """

        stack = []
        count = 0 

        for curr in directions:
            if len(stack) == 0:
                stack.append(curr)
            elif curr == 'L' and stack[-1] == 'R':
                count += 2
                stack.pop()
                while len(stack) > 0 and stack[-1] == 'R':
                    count += 1
                    stack.pop()
                stack.append('S')
            elif curr == 'L' and stack[-1] == 'S':
                count += 1
                stack.append('S')
            elif curr == 'S' and stack[-1] == 'R':
                while len(stack) > 0 and stack[-1] == 'R':
                    count += 1
                    stack.pop()
                stack.append('S')
            else:
                stack.append(curr)
        return count


        