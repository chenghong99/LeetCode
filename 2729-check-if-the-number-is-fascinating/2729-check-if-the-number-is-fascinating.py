class Solution:
    def isFascinating(self, n: int) -> bool:
        target = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        new_num = str(n) + str(2*n) + str(3*n)
        new_num = sorted(new_num)
        return new_num == target    