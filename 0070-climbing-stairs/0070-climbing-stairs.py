class Solution(object):
    def climbStairs(self, n):
        dic = dict()
        def climb(n):
          if n < 0:
            return 0
          elif n == 0:
            return 1
          elif dic.get(n) != None:
            return dic.get(n)
          else:
            val = climb(n - 1) + climb(n - 2)
            dic[n] = val
            return val
        return climb(n)