class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        counter = 1
        curr_char = chars[0]
        moving = 1
        pos = 1
        len_chars = len(chars)
        
        while moving < len_chars:
            if chars[pos] == curr_char:
                counter += 1
                chars.pop(pos)
            elif counter == 1:
                curr_char = chars[pos]
                pos += 1
            else:
                counter_to_string = str(counter)
                counter = 1
                for i in counter_to_string:
                    chars.insert(pos, i)
                    pos += 1
                curr_char = chars[pos]
                pos += 1
            moving += 1
            
        if counter != 1:
            counter_to_string = str(counter)
            for i in counter_to_string:
                chars.insert(pos, i)
                pos += 1
            
        return len(chars)
            
            
        