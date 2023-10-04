import random

class RandomizedSet(object):

    def __init__(self):
        self.dic = dict()
        self.arr = []
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if self.dic.get(val) == None:
            self.arr.append(val)
            self.dic[val] = len(self.arr) - 1
            return True
        else:
            return False

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if self.dic.get(val) != None:
            self.dic[self.arr[-1]] = self.dic.get(val)
            self.arr[self.dic.get(val)], self.arr[-1] = self.arr[-1], self.arr[self.dic.get(val)]
            self.arr = self.arr[:-1]
            self.dic.pop(val)
            return True
        else:
            return False
            

    def getRandom(self):
        """
        :rtype: int
        """
        num = random.randint(0, len(self.arr) - 1)
        number = self.arr[num]
        # self.arr[num], self.arr[-1] = self.arr[-1], self.arr[num]
        # self.arr = self.arr[:-1]
        # self.dic.pop(number)
        return number
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()