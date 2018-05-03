"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

除了数字0以外，首位不会为0
首先list转str再转int，然后加1，再转回list即可
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[0] == 0 and len(digits) == 1:return [1]
        num = ""
        i = 0
        while len(num) !=len(digits):
            num += str(digits[i])
            i +=1
        num = str(int(num) +1)
        res = []
        i = 0
        while len(res) != len(num):
            res.append(int(num[i]))
            i+= 1
        return res


digits = [4,3,2,1]
# digits=[0]
so = Solution()
res = so.plusOne(digits)
print(res)