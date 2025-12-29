class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        ## logic for brute force: for each histogram iterate till u find a histogram smaller then it. 
        ## reverse engineer, only pop list when the curr histogram is larger than the prev. 
        ## logic for any histogram curr the largest possible volume is to find the l where l is the furthest and >= to curr and r where r is the furthest away from curr and >= 0. 
        ## 2 iterations. first iteration, for each histogram curr, pop the stack until you cannot find a histogram higher than curr. for each histogram store 2 values, curr height, number of histogram to left. update stack by inserting curr back to stack. continue iteration until end of list. if there is nth larger than curr then leave the stack alone. 
        ## second iteration reverse the list, and use the same algorithm

        stack = []
        tracker = []

        for height in heights:
            curr_depth = 1
            while stack and stack[-1][0] >= height:
                temp = stack.pop()
                curr_depth += temp[1]
            tracker.append([height, curr_depth])
            stack.append([height, curr_depth])

        print(tracker)
        stack_reverse = []
        max_vol = 0

        for i in range(len(heights)-1, -1, -1):
            curr_depth = 1
            height = heights[i]
            while stack_reverse and stack_reverse[-1][0] >= height:
                temp = stack_reverse.pop()
                curr_depth += temp[1]
            max_vol = max(max_vol, ((tracker[i][1] + curr_depth - 1) * height))
            stack_reverse.append([height, curr_depth])
        return max_vol