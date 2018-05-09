"""
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Input: 3    "III"
Input: 4     "IV"
Input: 9     "IX"
Input: 58   "LVIII"
    Explanation: C = 100, L = 50, XXX = 30 and III = 3.
Input: 1994  "MCMXCIV"
    Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

1000 + 

1994 / 1000 = 1 ~ 994           M
994 / 1000 = 0 ~ 994    next

994 / 500 = 1 ~ 494             D
494 / 500 = 0 ~ 494     next

494 / 100 = 4 ~ 94              CCCC
94 / 100 = 0 ~ 94   next

94 / 50 = 1 ~ 44                L
44 / 50 = 0 ~ 44    next

44 / 10 = 4 ~ 4                 XXXX
4 / 10 = 0 ~ 4      next

4 / 5 = 0 ~ 4   next            NO

4 / 1 = 4 ~ 0                   IIII
0 / 1 = 0 ~ 0

M DCCCC LXXXX IIII
M  CM    XC     IV   
M  CM    XC     IV
出现四个重复的时候，需要进位
[1000, 500, 400, 50, 40, 4]
['M', 'D', 'CCCC', 'L', 'XXXX', 'IIII']


58 / 50 = 1 ~ 8         L
8 / 50 = 0 ~ 8  next
8 / 10 = 0 ~ 8  next
8 / 5 = 1 ~ 3           V
3 / 5 = 0 ~ 3   next
3 / 1 = 3 ~ 0           III
0 / 1 = 0 ~ 0

L V III
L V III

"""

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if  num < 1 or num >  3999:return ''

        relation = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M',4:'IV',9:'IX',40:'XL',90:'XC',400:'CD',900:'CM'}
        ls = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        rs = ''
        for item in ls:
            while True:
                s = int(num / item)
                r = int(num % item)     
                if s <= 0:break
                if s == 1:
                    rs += relation[item]
                else:
                    rs += relation[item]*s
                num = r
        return rs

so = Solution()
num = 3458
print(so.intToRoman(num))


test_case = {}