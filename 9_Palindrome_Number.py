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
        num = []
        while x != 0:
            num.append(int(x % 10))
            x = int(x / 10)
            """
            这里也许可以优化？
            1.第一次循环，找到最后一位数字
            2.然后再找头一位数字（
            3.对比，如果相等，直接True
            
            """
        for index in range(int(len(num)/2)):
            r_index = len(num) - index -1
            if num[index] == num[r_index]:
                continue
            else:
                return False
        return True


#Here is a more brief solution

    def isPalindrome_new(self, x):
        if x < 0:
            return False
        head = tail = 0
        bitnum = len(str(x))# 65432=> 5
        tmp = 0
        # print ('len=',bitnum)

        #   87654
        for i in range(int(bitnum/2)):
            tail = int((x/(10**i)) % 10) #遍历获取最后一位数字:  4  5  ...
            tmp = 10**(bitnum-i-1)  #头数字需要除以的分母:10000   1000  100...
            head = int(x / tmp) #获取最左边数字 8 7 ...
            x = x - head*tmp  #x更新为  7654
            if head != tail:   
                return False            
        return True


# x = 121
# res = Solution.isPalindrome(1,x)
# print(res)

test_case=[0,1,5,7,9,10,121,-121,1234321,20180808102,12349876]

for item in test_case:
    res = Solution.isPalindrome(1,item)
    print(item,'        is ',res)



    

