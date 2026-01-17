class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        ## pair min of both top right - max of both bottom left for x axis 
        ## like wise for y axis by using the y axis coordinates 

        max_len = 0

        for pos in range(len(bottomLeft)): ## iterate from second pos onwards, compre against prev
            for pos_2 in range(len(bottomLeft)):
                if pos_2 == pos:
                    continue
                curr_x_right_min = min(topRight[pos_2][0], topRight[pos][0])
                curr_x_left_max = max(bottomLeft[pos_2][0], bottomLeft[pos][0])
                curr_y_right_min = min(topRight[pos_2][1], topRight[pos][1])
                curr_y_left_max = max(bottomLeft[pos_2][1], bottomLeft[pos][1])

                max_len = max(max_len, min(curr_x_right_min - curr_x_left_max, curr_y_right_min - curr_y_left_max))

        return max_len ** 2


        