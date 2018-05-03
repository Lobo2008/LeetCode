"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

思路参考：leetcode.com/problems/climbing-stairs/discuss/124405/A-Python-Solution-using/123036
简述一下思路：
对于一个n步长的阶梯，有如下的思路去走：
1.走0个两步（即全部走一步）
2.走一个两步
3.走两个两步
...
...
i.走i个两步
这就变成了一个排列组合的问题。
当然，对于一个n步长的阶梯，最多走n/2个两步，注意这里要取整数。
举两个例子：
一.n=5时，看看有几种走法。
1.走0个两步 方法：1种
2.走一个两步 即1211的排列组合，结果为C1 4。(1是上标，4是下标) 方法：4种
3.走两个两步 即122的排列组合，结果位C2 3。(2是上标，3是下标) 方法：3种
所以总共就有1+4+3=8种

二.以步数为n，走i个两步时为例
这时走i个两步，那么就走n-2i个一步，总共需要排序的位置就是i+n-2i=n-i个，所以结果为Ci n-i,(i是上标，n-i是下标)
具体的实现如代码所示


"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        num2 = n//2 +1
        count = 0
        
        for i in range(num2):
            times = n-i
            count += self.C(i,times)
        return count
    
    """
    阶乘 n!= n*(n-1)*(n-2)*....*2*1
    return n!
    """
    def factorial(self,n):
        if n == 1 or n==0:
            return 1
        else:
            return n*self.factorial(n-1)
    """
    排列组合：C(1,4) = 4, C(2,6) = 6!/((6-2)!*2!)
    return C(i,n)
    """
    def C(self,i,n):
        return int(self.factorial(n)/(self.factorial(n-i)*self.factorial(i)))

n = 10       
so = Solution()

res = so.climbStairs(n)
print(res)

# print(so.factorial(0))

# print(so.C(0,6))