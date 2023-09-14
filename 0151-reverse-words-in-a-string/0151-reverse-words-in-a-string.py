class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word_bank = []
        pos_front = 0
        pos_back = 0
        pos_back_list = []
        changes = False

        if len(s) == 1:
            return s

        while pos_front < len(s) - 1:
            while s[pos_front] == " " and pos_front < len(s) - 1:
                pos_front += 1
                pos_back += 1

            while (s[pos_front] != " ") and (pos_front < len(s) - 1):
                pos_front += 1
                changes = True
            if pos_front == len(s) - 1:
                if s[pos_front] != " ":
                    pos_front += 1
                    changes = True
            if changes:
                word_bank.append(s[pos_back:pos_front])
                pos_back_list.append(pos_back)
                pos_back = pos_front
                changes = False

        # word_bank.pop()
        # word_bank.append(s[pos_back_list[-1]:pos_front + 1])
        print(word_bank)
        word_bank.reverse()
        return " ".join(word_bank)

