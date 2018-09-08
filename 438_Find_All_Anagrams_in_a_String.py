"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".


"""

class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        """ 
        ref:    https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92009/Python-Sliding-Window-Solution-using-Counter
          
            Input:
            s: "cbaebabacd" p: "abc"
        搜索词abc长度是3，统计出每个letter的频率设为pD，然后在文本中取前3个letter，统计出词频，设为sD
        如果pD等于sD，说明搜索词的词频和文本中前3个的词频相等，因为顺序无所谓，所以满足条件，找到一组，记录初始的index
        注意，这时候的窗口是    [cba]ebabacd  围着cbd
        then，窗口右移，变成    c[bae]babacd,同样的，统计出窗口中的词频，与pD比较

        注意，窗口右滑的时候，要把第一个  窗口左边 已经划过的字母的，从sD中删掉，保持sD中的数量跟pD一致
        还要注意，因为pD中可能有相同的单词，比如pd={a:2,c:1}，表示有3个字母，
        所以如果滑的是aac，那只需要把a的频率-1，而不是直接删除，当减到0的时候，再从字典中删除

        """
        if len(s) == 0 or len(p) == 0 or len(s) < len(p):   return []
        from collections import Counter
        pDic = Counter(p)
        sDic = Counter(s[:len(p)-1])#Attention, 初始窗口比搜索词小一格
        rs = []
        for endIndex in range(len(p)-1,len(s)):
            starIndex = endIndex - (len(p)-1) # 
            newAddLetter = s[endIndex]
            sDic[newAddLetter] += 1
            if pDic == sDic:
                rs.append(starIndex)
            headLetter = s[starIndex]
            sDic[headLetter] -= 1
            #因为只是减第一个字母的次数，所以可能会减到0，0没有意义且会对pDic造成影响，所以要删掉
            if sDic[headLetter] == 0:
                del sDic[headLetter]
        return rs







        

so = Solution()

s = "cbaebabacd" ; p= "abc"
s = "abab"; p =  "ab"
s = "acsasa"; p ="xasasasa"
print(so.findAnagrams(s, p))