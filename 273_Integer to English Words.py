class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        string = ""
        base = {
            0: "",
            1: " Thousand",
            2: " Million",
            3: " Billion",
            4: " Trillion"
        }
        current_base = 0
        while num > 0:
            chunk = num%1000
            current_string = self.convert(chunk)
            if current_string:
                string = current_string + base[current_base] + (' ' + string if string else '')
            current_base += 1
            num /= 1000

        return string

    def convert(self, num):
        string = ""
        num_2 = num%100
        tranlate_1 = {
            0: "",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten"
        }
        tranlate_2 = {
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen"
        }
        tranlate_3 = {
            2: "Twenty",
            3: "Thirty",
            4: "Forty",
            5: "Fifty",
            6: "Sixty",
            7: "Seventy",
            8: "Eighty",
            9: "Ninety"
        }
        if 0 < num_2 <= 10:
            string = tranlate_1[num_2]
        elif 10 < num_2 <= 19:
            string = tranlate_2[num_2]
        elif num_2 > 19:
            if num_2%10:
                string = tranlate_3[num_2/10] + " " + tranlate_1[num_2%10]
            else:
                string = tranlate_3[num_2/10]
        num_1 = num/100
        if num_1 > 0:
            string = tranlate_1[num_1] + " Hundred" + (" " + string if string else "")

        return string

print Solution().numberToWords(123000)

