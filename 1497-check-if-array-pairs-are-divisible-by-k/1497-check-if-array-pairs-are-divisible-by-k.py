class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        ## save modulo instead of the number, for example k = 5 find find number of modulo 1&4, 2&3, 0 pair, (eg 6, 9)
        ## boolean check hashmap is empty at the end 

        hashmap = {}

        for num in arr:
            mod = (num % k + k) % k
            hashmap[mod] = hashmap.get(mod, 0) + 1 ## fill in the number of each modulo occurence

        for key in list(hashmap.keys()): ## for each key find the inverse ie 5 % 10 find 5
            inverse = (k - key) % k

            if inverse == key: ## ie looking for the same key, make sure that key is even
                if hashmap.get(key) % 2 == 0:
                    hashmap.pop(key)

            elif hashmap.get(inverse) and hashmap.get(inverse) == hashmap.get(key):
                hashmap.pop(inverse)
                hashmap.pop(key)

        return len(hashmap) == 0