class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = '0'
        for i in range(len(num1)-1,-1,-1):
            m = self.multiply_single(num1[i], num2)
            m = m + '0'*(len(num1)-1-i)
            result = self.sum(result, m)

        for i in range(len(result)):
            if result[i] != '0':
                return result[i:]
        return '0'

    def multiply_single(self, num1, num2):
        result = ""
        num1 = int(num1)
        c = 0
        if num1 == 0:
            return '0'
        for i in range(len(num2)-1,-1,-1):
            m = num1*(int(num2[i]))+c
            if m > 9:
                c = m/10
                m = m%10
            else:
                c = 0
            result = str(m) + result
        if c > 0:
            result = str(c) + result
        return result

    def sum(self, num1, num2):
        c = 0
        result = ''
        for i in range(min(len(num1), len(num2))):
            s = ord(num1[len(num1)-1-i]) - ord('0') + ord(num2[len(num2)-1-i]) - ord('0') + c
            if s > 9:
                s -= 10
                c = 1
            else:
                c = 0
            result = str(s)+result
        if len(num1) == len(num2):
            if c == 1:
                result = '1' + result
        else:
            num_remain = num1[:len(num1)-i-1] if len(num1) > len(num2) else num2[:len(num2)-i-1]
        
            for i in range(len(num_remain)):
                s = ord(num_remain[len(num_remain)-1-i]) - ord('0') + c
                if s > 9:
                    s -= 10
                    c = 1
                else:
                    result = str(s)+result
                    c = 0
                    break
                result = str(s)+result
                
            if c == 1:
                result = '1' + result
            else:
                result = num_remain[:len(num_remain)-i-1] + result
            
        return result

print Solution().multiply('123','19991111')