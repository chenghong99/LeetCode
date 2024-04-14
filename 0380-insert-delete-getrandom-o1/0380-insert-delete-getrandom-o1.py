import random

class RandomizedSet(object):

    def __init__(self):
        self.arr = []
        self.map = {}
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if self.map.get(val) != None:
            return False
        
        else:
            self.arr.append(val)
            self.map[val] = len(self.arr) - 1
            return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        
        if self.map.get(val) == None:
            return False
        
        else:
            pos = self.map.get(val)
            tail = self.arr[-1]
            tail_pos = self.map.get(tail)
            self.arr[pos], self.arr[tail_pos] = self.arr[tail_pos], self.arr[pos]
            self.arr.pop()
            self.map[tail] = pos
            self.map.pop(val)
            return True

    def getRandom(self):
        """
        :rtype: int
        """
        
        len_ls = len(self.arr)
        num = random.randint(0, len_ls-1)
        get_num = self.arr[num]
        return get_num
        
    
## if not exist add to array and add inex to dic
## if remove swap with tail and remove tail 
## remove any from arr and pop from dic and arr


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()