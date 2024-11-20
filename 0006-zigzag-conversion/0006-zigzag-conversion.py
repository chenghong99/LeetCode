class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [''] * min(numRows, len(s))
        curRow, goingDown = 0, False

        for c in s:
            rows[curRow] += c
            if curRow == 0 or curRow == numRows - 1:
                goingDown = not goingDown
            if goingDown:
                curRow += 1  
            else:
                curRow -= 1

        return ''.join(rows)