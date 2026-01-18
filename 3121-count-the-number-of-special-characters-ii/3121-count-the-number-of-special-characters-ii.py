class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ## record first and last place of each char 
        last_map = {}
        output = 0

        for i, x in enumerate(word):
            if x.islower():
                last_map[x] = i
                
        visited = set()
        for i, x in enumerate(word):
            if x.isupper() and x not in visited and last_map.get(x.lower()) != None:
                if i > last_map.get(x.lower()):
                    output += 1
            visited.add(x)
        return output

        