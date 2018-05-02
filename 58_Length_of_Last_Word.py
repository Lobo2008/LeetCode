"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Input: "Hello World"
Output: 5

"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if len(s.replace(' ','')) == 0:return 0
        num = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == ' ':
                s = s[0:i]
            else:break
        print(s)
        for i in range(len(s)-1,-1,-1):
            if s[i] != ' ':
                num +=1
            else:
                return num
        return num 

    """
    一个更简单的方法（主要是python不熟）
    s.strip(' ')去除字符串s首位的空格
    s.rfind(' ')字符串s最后出现的位置
    """
    def lengthOfLastWord_2(self,s):
        s = s.strip(' ')
        return len(s) - 1 - s.rfind(' ')


s = "hello world bitchsss "
s="     "
res = Solution.lengthOfLastWord(1,s)
print(res)