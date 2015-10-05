class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        mapping = {
            "0": " ",
            "1": [],
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        last_result = ['']
        result = []
        for digit in digits:
            for letter in mapping[digit]:
                for single_result in last_result:
                    result.append(single_result+letter)
            last_result = result
            result = []

        return last_result
print Solution().letterCombinations("203")