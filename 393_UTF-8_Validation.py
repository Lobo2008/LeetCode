"""
A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:

    For 1-byte character, the first bit is a 0, followed by its unicode code.
    For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, 
    followed by n-1 bytes with most significant 2 bits being 10.

This is how the UTF-8 encoding would work:

   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

Given an array of integers representing the data, return whether it is a valid utf-8 encoding.

Note:
The input is an array of integers. Only the least significant 8 bits of each integer 
is used to store the data. This means each integer represents only 1 byte of data.

Example 1:

data = [197, 130, 1], which represents the octet sequence: 11000101 10000010 00000001.

Return true.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.

Example 2:

data = [235, 140, 4], which represented the octet sequence: 11101011 10001100 00000100.

Return false.

The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
The next byte is a continuation byte which starts with 10 and that's correct.
But the second continuation byte does not start with 10, so it is invalid.


"""


class Solution:
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """

        """
        我操，结合着测试用例，终于读懂题目是啥意思了，头条滚粗

        给定[197,130,1]，二进制分别是
            11000101 10000010 00000001
        看第一个二进制 11000101，因为最高2位是11，第3位是0，所以说明这个字会有两个个byte来编码，那就意味着后面还会跟着一个byte
            即 10000010 也是属于同一个字的编码
            前两个 197,130 => 11000101 10000010 编码成了一个字
            所以对于第2个二进制，是以10开头的，满足两字节的110xxxxx 10xxxxxx格式，因此到这里，是True

            那么，再看第三个，第三个二进制又构成了一个新的汉字的第一字节
            而由于00000001的最高位为0，说明只有一个字节，就是ASCII码，满足一字节的格式0xxxxxxx，是True

        [235, 140, 4] 11101011 10001100 00000100
            第一个二进制编码 11101011，前3位是1，第4位是0，说明这个字是3个字节的，后面应该连续跟着两个字节的10XXXXXX二进制
            但是，不满足，所以False


            now lets coding

            py里面二进制是表示为 0b+编码，比如5的二进制表示为 0b101, 7的二进制俄日 0b111
            十进制可以直接跟二进制比较，比如
                5 < 0b111会返回True
            所以，如果一个数 < 0b1000 0000的话，说明是一字节的，类推。。。
            but，不用这种方法

            197 = 11000101，右移5位的二进制为 0b110，则说明后面要跟1个字节
            235 = 11101011，右移4位的二进制位 0b1110，则说明后面要跟2个字节
            。。。
            用这种方法进行处理

            ref:https://www.cnblogs.com/grandyang/p/5847597.html



        """

        nextByteNum = 0
        for thisNum in data:
            if nextByteNum == 0:
                if thisNum >>5 == 0b110:
                    nextByteNum = 1
                elif thisNum >> 4  == 0b1110:
                    nextByteNum = 2
                elif thisNum >> 3 == 0b11110:
                    nextByteNum = 3
                #移了5位（1B）、4位（2B）、3（3B）位都不满足，那测试1B的，1B要移7位，移了7位还剩1，说明原来是0b1xxxxx,不对
                elif thisNum >> 7 == 0b1: return False
            else:#nextByteNum !=0时，开始检查第2B及以后的情况，需要满足 移动6位还剩10
                if thisNum >> 6 != 0b10: return False
                nextByteNum -= 1
        return nextByteNum == 0




so = Solution()

data = [197, 130, 1]
data = [235, 140, 4]
print(so.validUtf8(data))