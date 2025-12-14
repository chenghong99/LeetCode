class Solution(object):
    def countCoveredBuildings(self, n, buildings):
        """
        :type n: int
        :type buildings: List[List[int]]
        :rtype: int
        """

        ## create 2 dic one for x axis, one for y axis. or each coordinate store the key value pair in each dic. 
        ## for each coordinate x, y find the max and min of the correspinding coordinate, if there exist a smaller and larger coordinate add 1 to output 

        x_dic, y_dic, count = {}, {}, 0

        for c in buildings:
            if x_dic.get(c[0]) == None:
                x_dic[c[0]] = [100000000, -100000000]
                x_dic[c[0]][0] = min(c[1], x_dic[c[0]][0])
                x_dic[c[0]][1] = max(c[1], x_dic[c[0]][1])
            else:
                x_dic[c[0]][0] = min(c[1], x_dic[c[0]][0])
                x_dic[c[0]][1] = max(c[1], x_dic[c[0]][1])
            if y_dic.get(c[1]) == None:
                y_dic[c[1]] = [100000000, -100000000]
                y_dic[c[1]][0] = min(c[0], y_dic[c[1]][0])
                y_dic[c[1]][1] = max(c[0], y_dic[c[1]][1])
            else:
                y_dic[c[1]][0] = min(c[0], y_dic[c[1]][0])
                y_dic[c[1]][1] = max(c[0], y_dic[c[1]][1])
        print(x_dic)
        print(y_dic)
        for c in buildings:
            if y_dic[c[1]][0] < c[0] < y_dic[c[1]][1] and x_dic[c[0]][0] < c[1] < x_dic[c[0]][1]:
                count += 1

        return count