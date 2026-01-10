class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ## hashmap key = group size, value = position in list 
        ## for each key, value group the people together. 

        hashmap = {}

        for pos, size in enumerate(groupSizes):
            if hashmap.get(size) == None:
                hashmap[size] = []
            hashmap.get(size).append(pos)

        output = []
        for key, value in hashmap.items():
            for i in range(0, len(value), key):
                temp = []
                for j in range(i, i + key):
                    temp.append(value[j])
                output.append(temp)
        return output

        