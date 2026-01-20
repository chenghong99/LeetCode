class Solution:
    def sumAndMultiply(self, n: int) -> int:
        sum_x = sum(int(i) for i in str(n))
        total_x = [i for i in str(n) if i != "0"]
        x_num = "".join(total_x)
        if x_num == "":
            return 0
        return sum_x*int(x_num)