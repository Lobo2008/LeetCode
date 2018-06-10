"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

"""

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        1到n都可以作为二叉树的根节点，假如根节点是k的话，0到k-1就是此树的左son，k+1到n-1就是此树的右son
        比如如下的以3为root的树，左son是1和2，可以构造成两种情况，因此，推理到n的时候，就是左边的种类*右边的种类
        左边是2，右边是1，因为右son没有节点，也就是空树-> 以3为root的有2*1=2种
            3     3      
           /     /     
          2     1      
         /       \                 
        1         2             
        推广：    
        以k为根节点的二叉树的种类数就是左右可能种类的乘积，用递推式表示成：
        h(n) = h(0)*h(n-1)   +   h(1)*h(n-2)  + ... +  h(n-2)*h(1)  +  h(n-1)h(0)
              左边0个右边n-1个     左边1个右边n-2个 ...    左边n-2个右边1个   左边n-1个右边0个

        其中h(0)=h(1)=1，因为0个数（空树）或者1个数能组成的形状只有1个，然后递推出后面的即可
        注意到，这其实是一个卡特兰数，所以直接用公式即可
        h(0) = 1
        h(1) = 1
        h(2) = h(0)h(1)+h(1)h(0) = 1+1=2
        h(3) = h(0)h(2)+h(1)h(1)+h(2)h(0) = 1*2+1*1+2*1=5
        h(4) = h(0)h(3)+h(1)h(2)+h(2)h(1)+h(3)h(0) = 1*5+1*2+2*1+5*1=14
        
        代码流程：
        n=4时:
            左i  右n-i-1
            0    3
                    h(0)*h(3)，其中h(0)=1,h(3)要递归调用：
                    n=3时
                        左    右
                        0     2  h(0)*h(2)=1*2=2  -> sumi=2
                        1     1  h(1)*h(1)=1*1=1  -> sumi=2+1=3
                        2     0  h(2)*h(0)=2*1=2  -> sumi=3+2=5
                    所以0 3得5，此时sumi=5
            1    2 
                    h(1)*h(2)=1*2=2  -> sumi=5+2=7
            2    1 
                    h(2)*h(1)=2*1=2  -> sumi=7+2=9
            3    0
                    h(3)*h(0)=5*1=2  -> sumi=9+5=14   这里h(3)在上面已经计算过了

        =>>>>>>>>   代码超时
        """
        rs = [1,1,2] #最基本的情况
        if n <= 2:
            return rs[n]
        sumi = 0
        for i in range(n):
            sumi += self.numTrees(i)*self.numTrees(n-i-1)
        return sumi
    """
    上面的代码超时了，因为有重复计算，0 3的时候，算了一遍h(0~2)，3 0的时候，又把h(0~2)算了一遍
    所以，好的方法应该是：计算第k项的时候，用到的第0~k-1项应该都已经存起来了，用到的时候直接取就好，不用重复计算
        h(0) = 1
        h(1) = 1
        h(2) = h(0)h(1)+h(1)h(0) = 1+1=2
        h(3) = h(0)h(2)+h(1)h(1)+h(2)h(0) = 1*2+1*1+2*1=5
        h(4) = h(0)h(3)+h(1)h(2)+h(2)h(1)+h(3)h(0) = 1*5+1*2+2*1+5*1=14

    n=5时，dp=[1,1,1,1,1]，因为要返回dp[n]，所以先用1占位
    注意：以下用到了公式：  h(i) = h(0)h(i-1)+h(1)h(i-2)+...+h(n-1)h(0)
        i=2 s=0    
            j=0
                s=0+dp[0]*dp[1]=0+1*1=1
            j=1
                s=2+dp[1]*dp[0]=1+1*1=2
            -> dp[2]=2
        i=3 s=0
            j=0
                s=2+dp[0]*dp[2]=0+1*2=2
            j=1
                s=4+dp[1]*dp[1]=2+1*1=3
            j=2
                s=5+dp[2]*dp[0]=3+2*1=5
            -> dp[3]=5
        可以看到，计算dp[3]的时候，用到的dp[0-2]都已近是存着的了，不需要重复计算了
        ...
    """
    def numTrees_dp(self, n):
        h=[1 for __ in range(n+1)] #先用1占位
        """
        因为0和1的情况都是一种，
        h的初始值已经满足了，所以从2开始
        """
        for i in range(2,n+1):
            s = 0
            for j in range(i):
                s += h[j]*h[i-j-1]# h(i)*h(n-i-1)
            h[i] = s
        return h[n]


so = Solution()
n = 4
print(so.numTrees(n))
print(so.numTrees_dp(n))