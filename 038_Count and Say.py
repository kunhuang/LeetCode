import pdb
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        string = '1'
        for i in range(n-1):
            last = string[0]
            k = 0
            new_string = ''
            for j in range(len(string)):
                # pdb.set_trace()
                if string[j] == last:
                    k += 1
                else:
                    new_string += str(k)+str(last)
                    last = string[j]
                    k = 1
            new_string += str(k)+str(last)        
            string = new_string

        return string

for i in range(10):
    print Solution().countAndSay(i)