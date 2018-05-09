"""
Note:

    Only the space character ' ' is considered as whitespace character.
    Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

Example 1:

Input: "42"
Output: 42

Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.

Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.

Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.

思考：用正则就可以了，主要是找到各种情况：
1)纯数字开头   2   3   123                ^\d+
2)正负号开头+数字   -23  +12  -3 +5       ^[\-\+]\d+
3)空格+数字   '  123'  '  31'             ^\s+\d+
4)空格+正负号+数字  '   -1'  ‘ +122 ’     ^\s+[\-\+]\d+

1)2)合并 ^[\-\+]{0,1}\d+
    不能合并，因为1）是数字开头，2是正负号开头
3)4)合并 ^\s+[\-\+]{0,1}\d+

所以 pattern = r"(^\d+)|(^[\-\+]{0,1}\d+)|(^\s+[\-\+]{0,1}\d+)"

"""
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        import re
        pattern = r"(^\d+)|(^[\-\+]{0,1}\d+)|(^\s+[\-\+]{0,1}\d+)"
        rs = re.search(pattern,str)
        # print('~~~',rs.group())
        num = 0
        if rs:
            num =  int(rs.group())
        #[−2^31,  2^31 − 1]. If the numerical value is out of the range of representable values, 
        # INT_MAX (2^31 − 1) or INT_MIN (−2^31) is returned.
        if num < (-2)**31:
            num =  -2**31 
        elif  num > ((2**31) - 1):
            num = 2**31 -1
        return num

so = Solution()

line = "4193 with words"
line = "+-2"

# rs = so.myAtoi(line)
# print(rs)

test_case = {"42":42,"   -42":-42,"4193 with words":4193,"words and 987":0,"-91283472332":-2147483648,"+-2":0}

for i in test_case:
    rs = so.myAtoi(i)
    print('---------')
    print(i,':',test_case[i])
    print('     ->',rs)






