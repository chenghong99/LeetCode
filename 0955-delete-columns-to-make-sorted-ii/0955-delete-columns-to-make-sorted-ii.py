class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        ## to note: just need to make sure the first character in the string is in lexicographic order. just need to delete from first character onwards. 
        ## a confirmed case is when the first string first char is > and not >=, for tie breakers like >= more iterations have to be done

        del_counter = 0 
        confirmed_strings = [False for i in range(len(strs)-1)]
        for i in range(len(strs[0])):
            remove_flag = False
            
            for j in range(len(strs) - 1):
                if not confirmed_strings[j] and strs[j][i] > strs[j+1][i]:
                    remove_flag = True 
                    break

            if remove_flag:
                del_counter += 1
                continue

            for j in range(len(strs) - 1):
                if not confirmed_strings[j] and strs[j][i] < strs[j+1][i]:
                    confirmed_strings[j] = True

            if all(confirmed_strings):
                break
        return del_counter




        