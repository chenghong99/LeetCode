class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        ## sort the 2 array, for the largest capacity, find the largest packets needed to fill up the boxes. 
        capacity.sort(reverse = True)
        num_apples = sum(apple)
        counter = 0
        for i in capacity:
            if num_apples > 0:
                counter += 1
                num_apples -= i
        return counter
