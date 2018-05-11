"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Input: 4
Output: 2

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.

输入一个数，求出他的平方根

思路：用的是二分法
x的根root，最多是 x/2，所以只需要在 [0,n/2]区间找就可以了
不停的划分下去，如果root的平方大于x，则说明root应该在左边部分，反之应该在右边的部分

坑主要是在0~3的几个数字，以及   start是从0还是1还是2开始，mid是start+end还是start+end+1之类的
"""
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <2 :return x
        start = 1
        end = x//2 
        mid = (start + end + 1 )//2
        while start != mid and end != mid:
            if mid**2 <= x:
                start = mid
            else:
                end = mid
            mid = (start + end  )//2 
        return mid

    def mySqrt2(self, x):
        if x < 2:return x
        low ,high = 0,x
        while low <= high:
            mid = (low + high) // 2
            print(low,mid,high)
            r = mid * mid
            if r == x:
                return mid
            elif r > x:
                print('<-')
                high = mid - 1
                
            else:
                print('->')
                low = mid + 1
                
        return low - 1

    def mySqrt3(self, x):
        if x <= 1:
            return x
        s, e = 0, x
        while s <= e:
            mid = (s+e)/2
            r = mid * mid
            if r > x:
                e = mid - 1
            elif r == x:
                return mid
            else:
                s = mid + 1
        return s - 1

x = 26
so = Solution()
print(so.mySqrt2(x))
