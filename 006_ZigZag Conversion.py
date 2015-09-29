import pdb
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        result = ""
        n_arrays = len(s)/(2*numRows-2)
        n_last_array = len(s)%(2*numRows-2)

        for j in range(n_arrays):
            result += s[j*(2*numRows-2)]
        result += s[n_arrays*(2*numRows-2)] if n_last_array > 0 else ""
        for i in range(1, numRows-1):
            for j in range(n_arrays):
                result += (s[j*(2*numRows-2)+i]+s[(j+1)*(2*numRows-2)-i])
            result += s[n_arrays*(2*numRows-2)+i] if n_last_array > i else ""
            result += s[(n_arrays+1)*(2*numRows-2)-i] if n_last_array > 2*numRows-2-i else ""
        for j in range(n_arrays):
            result += s[j*(2*numRows-2)-1+numRows]
        result += s[n_arrays*(2*numRows-2)-1+numRows] if n_last_array > numRows-1 else ""

        return result

print Solution().convert("PAYPALISHIRING", 3)        
# PAHN APLSIIG YIR
# PAHN APLSIIG PSI