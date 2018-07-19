"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

"""

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: strz
        :rtype: int
        """
        """
        输入一个数字字符串，转换成编码   
        
        设dp[i]表示字符串前i个字符组成的解码的数量，则状态方程为：
        dp[i]=   1)   dp[i-1] + dp[i-2]，
                        当s[i-2]和s[i-1]有两种编码方式时，比如10~26之间，不包括10和20的其他数字，如
                        23 可以是：  BC  或者  W，有两种
                 2)   dp[i-2]
                        当s[i-2]和s[i-1]是10和20的时候，只能有一种编码方式10->J,  20->T
                 3)   dp[i-1]
                        当s[i-2]和s[i-1]是大与26的数字或者是01、08等情况的时候，没有解
                        因此，前i个元素组成的数量与前i-1个元素组成的数量一样。

        2320160,dp=[1,1],n=5
        i=2
            s[i-2]s[i-1]=s[0,1]= 23 满足第一个if，所以dp[2]=1+1=2
                说明前两个元素组成的数量是2:（2 3 ,23),此时dp=[1,1,2]
        i=3
            s[i-2]s[i-1]=s[1,2]=32，满足第三个if，所以dp[3]=dp[2]=2
                说明前三个元素组成的数量是2：(2 3 2, 23 2)，此时dp=[1,1,2,2]
        i=4
            s[i-2]s[i-1]=s[2,3]=20,满足第二个if，所以dp[4]=dp[2]=2
                说明前四个元素组成的数量是2：(2 3 20,23 20)，此时dp=[1,1,2,2,2]
        i=5
             s[i-2]s[i-1]=s[3,4]=01,满足第三个if，所以dp[5]=dp[4]=2
                说明前五个元素组成的数量是2：(2 3 20 1,23 20 1),此时dp=[1,1,2,2,2,2]
        i=6
             s[i-2]s[i-1]=s[4,5]=16 满足第一个if，所以dp[6]=2+2=4
                说明前六个元素组成的数量是4:(2 3 20 1 6, 2 3 20 16, 23 20 1 6, 23 20 16)
                    2  3  20  1  6
                    2  3  20  16
                    23  20  1  6
                    23  20  16
        i=7 
             s[i-2]s[i-1]=s[5,6]=60,满足第四个if，直接返回0，没有可用的编码方式
            
    
        """

        if len(s) == 0 or s[0] == '0':
            return 0
        dp = [1,1]
        for i in range(2,len(s)+1):
            if int(s[i-2:i]) >= 10 and int(s[i-2:i]) <= 26 and s[i-1] != '0':
                dp.append(dp[i-2]+dp[i-1])
            elif  int(s[i-2:i]) in [10,20]:
                dp.append(dp[i-2])
            elif s[i-1] != '0':
                dp.append(dp[i-1])
            else:
                return 0
        return dp[len(s)]

   
        
so = Solution()
s = '2320160'
print(so.numDecodings(s))