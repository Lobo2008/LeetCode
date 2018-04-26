"""


Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
s numerals are usually written largest to smallest from left to right. 
    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.
Input: "III"    "IV"    "IX"    "LVIII"     "MCMXCIV"
Output: 3         4      9         58          1994

Input: "LVIII"
Output: 58
Explanation: C = 100, L = 50, XXX = 30 and III = 3.

Input: "M CM XC IV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

"D C XX I"
621

从左往右加，如果右边比左边的下标大，则组成一组进行加减

0  123  456
9  446  124
"""
class Solution(object):
    def sToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        relation ={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000,'G':-100000}
        s += 'G' 
        sum = start = 0
        for index in range(len(s)-1):
            if  relation[s[index]] > relation[s[index+1]]: #当前值大于前面的值，则分组
                oneGroup = s[start:index+1]
                if len(oneGroup) == 1:
                    tmpsum = relation[oneGroup[0]]
                    sum += relation[oneGroup[0]]
                elif oneGroup[0] == oneGroup[1]:#如果后两个相等，则如果存在第三个，第三个也必定相等
                        tmpsum = relation[oneGroup[0]] * len(oneGroup)
                        sum += relation[oneGroup[0]] * len(oneGroup)
                else:
                    tmpsum = relation[oneGroup[1]] - relation[oneGroup[0]]
                    sum += relation[oneGroup[1]] - relation[oneGroup[0]]
                start = index+1
        return sum
s = "MCMXCIV"
# s = "LVIII"
s = "DCXXI"
# res = Solution.sToInt(1,s)
# print(res)
# """
test_case ={"III":3, "IV":4, "IX":9, "LVIII":58, "MCMXCIV":94, "DCXXI":621}
for item in test_case:
    res = Solution.sToInt(1,item)
    print( item,' => ',res)
# """
