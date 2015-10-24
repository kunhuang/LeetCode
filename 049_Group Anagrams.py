import pdb
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = []
        hash_ = {}
        for string in strs:
            # pdb.set_trace()
            sorted_string = tuple(sorted(string))
            if sorted_string in hash_:
                hash_[sorted_string].append(string)
            else:
                hash_[sorted_string] = [string]

        for key, value in hash_.iteritems():
            result.append(sorted(value))

        return result

print Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        