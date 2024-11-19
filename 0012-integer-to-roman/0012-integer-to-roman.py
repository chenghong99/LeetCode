class Solution:
    def intToRoman(self, num: int) -> str:
        ## divide by 1000 first and add M then divide by 900 and add
        str = ''
        str += (num // 1000) * 'M'
        num %= 1000
        str += (num // 900) * 'CM'
        num %= 900
        str += (num // 500) * 'D'
        num %= 500
        str += (num // 400) * 'CD'
        num %= 400
        str += (num // 100) * 'C'
        num %= 100 
        str += (num // 90) * 'XC'
        num %= 90
        str += (num // 50) * 'L'
        num %= 50
        str += (num // 40) * 'XL'
        num %= 40
        str += (num // 10) * 'X'
        num %= 10
        str += (num // 9) * 'IX'
        num %= 9 
        str += (num // 5) * 'V'
        num %= 5
        str += (num // 4) * 'IV'
        num %= 4
        str += (num // 1) * 'I'
        
        return str
        