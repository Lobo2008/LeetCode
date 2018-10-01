"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:

    It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
    Space complexity should be O(n).
    Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

Credits:
Special thanks to @ syedee for adding this problem and creating all test cases.

"""
class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        """
            decimai                     binary              num of 1
             0                             0                0
             1                             1                1
        ->   2                             10               1
             3                             11               2
        ->   4                             100              1
             5                             101              2
             6                             110              2
             7                             111              3
        ->   8                             1000             1
             9                             1001             2 
             10                            1010             2
             11                            1011             3
             12                            1100             2
             13                            1101             3
             14                            1110             3
             15                            1111             4
        ->   16                            10000            1   
                                    .
                                    .
                                    .
             31                            11111            5
        ->   32                            100000           1 
            ...
        可以观察到 从 [2^1,2^2) 是 [1,2]
                 从 [2^2,2^3] 是 [1,2,2,3]   新多出的两个数量是上面[1,2]中各元素+1
                 从 [2^3,2^4) 是 [1,2,2,3,2,3,3,4] 新多出的4个元素是上面的[1,2,2,3]各元素+1
        每到2的k次方，1的数量就要从1,2,2,3这种上升上去， 
            比如k-1次方的时候，是[a1,a2,a3...ak]
            到了k次方，元素数量翻倍，多出的一倍由原来的元素+1得到  [a1,a2,a3,...ak, a1+1,a2+1,a3+1...ak+1]

        给定数字n，需要x位来表示，有关系式: 2^x >= n

        """
        rs = [0,1,1,2]
        if num <= 2:   return rs[:num+1]
        i = 2
        while 2**i <= num:
            start = 2**(i-1)
            end = 2**i
            tmprs = rs[start:end]+ [ele+1 for ele in rs[start:end]]  
            rs.extend(tmprs)
            i += 1
        return rs[:num+1]


            
so = Solution()

num = 5
# num = 0
# num = 1
num = 5
# num = -10
print(so.countBits(num))
