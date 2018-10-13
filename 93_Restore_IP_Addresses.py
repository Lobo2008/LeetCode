"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"




"""


class Solution:

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        #ref https://segmentfault.com/a/1190000008931557
        #tricky的方法
        # rs = []
        # for a in range(1,4):
        #     for b in range(1,4):
        #         for c in range(1,4):
        #             for d in range(1,4):
        #                 if sum([a,b,c,d]) == len(s):
        #                     n1 = s[:a]
        #                     n2 = s[a:a+b]
        #                     n3 = s[a+b:a+b+c]
        #                     n4 = s[a+b+c:]

        #                     if self.isValid(n1) and self.isValid(n2) and self.isValid(n3) and self.isValid(n4):
        #                         ip = n1 + "." + n2 + "." + n3 + "." + n4
        #                         if len(ip) == len(s) + 3:
        #                             rs.append(ip)
        # return rs

        """
        #234.245.256.123
        #2.  342 452 561 23 还剩2个点，最多可以有(2+1)位，而目前还有11位，不行， len(s)-index > (dot+1)*3

        dfs方法，事实上是上面的tricky的方法的抽象版本

        """
        def dfs(nows, index, path, rs,dotnum):
            

            # if dotnum == 0 and len(nows) > 12:return
            # if dotnum == 1 and len(nows) > 9:return
            # if dotnum == 2 and len(nows) > 6:return
            if dotnum <= 2 and len(nows) > (4-dotnum)*3:return


            if dotnum == 3 and self.isValid(nows):
                rs.append(path+nows) 
                return
            else:
                for i in range(1,4):
                    tmp = nows[:i]
                    if self.isValid(tmp):
                        dfs(nows[i:],i,path+tmp+".",rs,dotnum+1)
                    
        rs = []
        if len(s) < 4 or len(s) > 12:   return rs
        dfs(s,0, "",rs,0)
        return rs

    def isValid(self,s):
        if len(s) <=0:  return False
        if int(s) < 0 or int(s) > 255:
            return False
        if len(s) > 1 and s[0] == '0':
            return False
        return True 





    def restoreIpAddresses_backtracing(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        """
        ref:https://blog.csdn.net/u012501459/article/details/46804405

        """
        
        
        rs = []
        
        self.helper(s, 0, 0, [], rs)
        # return rs
        for item in rs:
            print(item)

    def helper(self, s, num, pos, path, rs):
        if pos == len(s) or num == 4:
            rs.append(path[:len(path)-1])
            return
        # if(s.size()-pos>3*(4-num))
        if len(s) - pos > 3*(4-num):
            return

        if pos < len(s):
            path += s[pos:pos+1] + "."
            self.helper(s, num+1, pos+1, path, rs)
            path = path[:len(path)-1]

        if pos < len(s) - 1 and s[pos] != '0':
            path += s[pos:pos+2]+"."
            self.helper(s, num+1, pos+2, path, rs)
            path = path[:len(path)-2]
        if pos < len(s) - 2 and s[pos] != '0' and s[pos:pos+3] <= '255':
            path += s[pos:pos+3]+"."
            self.helper(s, num+1, pos+3, path, rs)
            path = path[:len(path)-3]

so = Solution()

s = "25525511135"
s = "010010"
# s="19216821"
print(so.restoreIpAddresses(s))