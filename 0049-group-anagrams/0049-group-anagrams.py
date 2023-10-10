class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        dic = dict()
        
        for i in range(len(strs)):
            split_string = tuple(sorted(list(strs[i])))
            if dic.get(split_string) == None:
                dic[split_string] = [strs[i]]
                
            else:
                dic.get(split_string).append(strs[i])
                
        return list(dic.values())
            
        