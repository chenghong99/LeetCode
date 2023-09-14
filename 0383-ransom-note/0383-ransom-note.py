class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        mag_hm = {}
        
        for letter in magazine:
            if mag_hm.get(letter) != None:
                mag_hm[letter] += 1
            else:
                mag_hm[letter] = 1

        for letter in ransomNote:
            if mag_hm.get(letter) == None:
                return False
            else:
                mag_hm[letter] -= 1
                if mag_hm[letter] == 0:
                    mag_hm.pop(letter)

        return True