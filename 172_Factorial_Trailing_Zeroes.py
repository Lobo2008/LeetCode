"""
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.

大概是，阶乘结果的0的数量？

5 = 5x4x3x2x1 = 120
10 = 10x9x8x7x6x5x4x3x2x1=3628800

方法一：
如果我们要判断出0的个数，如果我们直接求N!那么数据会很大，数据可能溢出，,
那么为了得到0的个数我们知道可以从10的角度进行判断，如果我们知道N!中10的个数，
我们就可以判断出0的个数，

如果N!=K*10^n,K是不能被10整除的数，那么我们可以根据n就可以得到0的个数，
考虑10的个数，我们必须对N!进行质因数的分解，N!=(2^x)*(3^y)(5^z)...........,由于2*5=10，
所以n只与x和z相关，

于是n=min(x,z),我们可以判断出x的个数必然大于z的个数，因为被2整除的数的频率大于被5整除的数的频率高，

所以n=z;

下面我们要判断出N1中5的个数，

因为N!=N*N-1*N-2*N-3.......................................

所以我们要判断出5的个数，我们可以对每个N，N-1,N-2,进行判断，就可以得到5的个数了

方法二：递归


        if n >= 5:
            return int(n/5) + int(self.trailingZeroes(n/5))
        else:
            return 0

因为0的数量只跟2x5有关，而5的数量必定比2的少，所以求5的个数即可
"""

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        #z=N/5+N/25+N/5^3+....................
        count = 0
        while n != 0:
            count += int(n /5)
            n = int(n/5)
        return count
    
    """
    recurssive
    """           
    def trailingZeroes2(self,n):

        if n >= 5:
            return int(n/5) + int(self.trailingZeroes(n/5))
        else:
            return 0


n = 668
n = 3322
so = Solution()
rs = so.trailingZeroes(n)
# rs = so.factorialX(n)
print(rs)
# for i in range(5,31,1):
#     rs = so.factorialX(i)
#     times = so.trailingZeroes(i)
#     print(i,'=>',rs,':',times)