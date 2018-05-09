"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Input: 121
Output: true

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up:

Coud you solve it without converting the integer to a string?

正:  0  1  2  3   4  5   6   
    [8, 4 ,2, 3, 7]
反: -5 -4 -3  -2 -1
   
len = 7 奇数：
 0 6
 1 5
 2 4
 3

i   len-i-1
0   6
1   5
2   4
3   3




正: i           0    1   2  3 
反: -len + i   -4    -3  -2 -1

"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        head = tail = 0
        bitnum = len(str(x))# 65432=> 5
        tmp = 0
        # print ('len=',bitnum)
        for i in range(int(bitnum/2)):
            tail = int((x/(10**i)) % 10)
            tmp = 10**(bitnum-i-1)
            head = int(x / tmp)
            x = x - head*tmp
            if head != tail:
                return False
            # print(head,' VS ',tail)
            
        return True

x = 65432
print('输入的数字是: ',x)
res = Solution.isPalindrome(1,x)
print(res)

test_case=[0,1,5,7,9,10,121,-121,1234321,20180808102,12349876]

# for item in test_case:
#     res = Solution.isPalindrome(1,item)
#     print(item,'        is ',res)
# # print('ori number: ',x)

    

