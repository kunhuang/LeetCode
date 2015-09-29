from math import log
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_numeral = ""
        symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M', '', '']
        def symbols_mapping(num, symbol_set):
            if num==0:
                return ''
            elif num==1:
                return symbol_set[0]
            elif num==2:
                return symbol_set[0]+symbol_set[0]
            elif num==3:
                return symbol_set[0]+symbol_set[0]+symbol_set[0]
            elif num==4:
                return symbol_set[0]+symbol_set[1]
            elif num==5:
                return symbol_set[1]
            elif num==6:
                return symbol_set[1]+symbol_set[0]
            elif num==7:
                return symbol_set[1]+symbol_set[0]+symbol_set[0]
            elif num==8:
                return symbol_set[1]+symbol_set[0]+symbol_set[0]+symbol_set[0]
            elif num==9:
                return symbol_set[0]+symbol_set[2]
            raise Exception()
        i = 0
        while num:
            roman_numeral = symbols_mapping(num%10, symbols[2*i:2*i+3])+roman_numeral
            num /= 10
            i += 1
        return roman_numeral
print Solution().intToRoman(1311)