"""

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

    The same word in the dictionary may be reused multiple times in the segmentation.
    You may assume the dictionary does not contain duplicate words.

Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false


"""

class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        """
        ref:   leetcode.com/problems/word-break/discuss/43797/A-solution-using-BFS/43031
        BFS
        例子：s = "catsandogog"; wordDict=["cats", "og",  "and", "cat"]
        初始时，两个指针（cur和end）指向位置0，也就是c，然后end从0往后移，判断s[cur:end]是否在字典中
        s[cur:end] = c      不在 
                     ca     不在
                     cat    在，则记录此下标  que=[3],      visited={0,3}
                     cats   在，则记录此下标，que=[4,3],    visted={0,3,4} 
                     catsa  不在
                     ...
                至此，queue=[4,3] 说明在下标分别为3和4的位置，做了分词，下一次，要从这两个的其中一个开始（所以是BFS）
        cur = 3,也就是上一个词为cat的时候，对剩下的sandogog进行判断
        s[cur:end] = s 不在
                     sa 不在
                     ...都不在  说明，cat进行分词的不满足，那试试cats分词的情况
        cats时，cur=4,剩下的部分是andogog
        s[cur:end] = a      不在
                     an     不在
                     and    在，则记录此下标，que=[7]
                     ando   不在
                     ...不在，然后 queue=[7]，说明cats分词以后，在下标为7的地方再一次可以分词，那下一次从这里开始检查
        。。。
        """

        from collections import deque

        queue = deque()
        visted = set()
        queue.append(0)
        visted.add(0)
        while queue:
            curIndex = queue.pop()
            for endIndex in range(curIndex,len(s)+1):
                if endIndex in visted:  continue
                if s[curIndex:endIndex] in wordDict:
                    if endIndex == len(s):   return True
                    queue.appendleft(endIndex)
                    visted.add(endIndex)
        return False
























        import collections
        queue = collections.deque()                                                                           
        visited = set()                                                                                       
        queue.appendleft(0)                                                                                   
        visited.add(0)                                                                                        
        while len(queue) > 0:                                                                                 
            curr_index = queue.pop()                                                                          
            for endIndex in range(curr_index, len(s)+1):                                                             
                if endIndex in visited:                                                                              
                    continue                                                                                  
                if s[curr_index:endIndex] in wordDict: #因为字典中可能存在长度为1的词，所以要从cur开始找                                                              
                    if endIndex == len(s):   
                        return True                                                                           
                    queue.appendleft(endIndex)                                                                       
                    visited.add(endIndex)     
        return False 




        #TLE
        if not s or not wordDict:   return False
        tmp = [len(i) for i in wordDict]
        minlen, maxlen = min(tmp), max(tmp)
        return self.helper(minlen, maxlen, s, wordDict)

    def helper(self,minlen,maxlen,s, wordDict):
        if len(s) < minlen: return False
        if s in wordDict:
            return True
        for l in range(minlen, maxlen+1):
            word = s[:l]
            if word in wordDict:
                if self.helper(minlen, maxlen, s[l:],wordDict):
                    return True      
        return False
            
        


so = Solution()
s = "catsandogog"; wordDict = ["cats", "dog",  "and", "cat"]
s = "leetcode"; wordDict = ["leet", "code"]
s = "applepenapple"; wordDict = ["apple", "pen"]
s = "catsandog"; wordDict = ["cats", "dog", "sand", "and", "cat"]
s = "catsandogog"; wordDict=["cats", "og",  "and", "cat"]
print(so.wordBreak(s, wordDict))