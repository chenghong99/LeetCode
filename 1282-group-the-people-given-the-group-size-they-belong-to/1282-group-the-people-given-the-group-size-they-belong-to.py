class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ## hashmap key = group size, value = position in list 
        ## for each key, value group the people together. 

        hashmap = {}
        output = []

        for pos, size in enumerate(groupSizes):
            if hashmap.get(size) == None:
                hashmap[size] = []
            hashmap[size].append(pos)

            if len(hashmap[size]) == size:
                output.append(hashmap[size])
                hashmap[size] = []
       
        return output

        