"""

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

    The same word in the dictionary may be reused multiple times in the segmentation.
    You may assume the dictionary does not contain duplicate words.

Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]

Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]

"""

class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        """
        第一代的变体，只是，现在要把所有的情况存下来
        不对，这个应该要用dfs

        s = "catsanddog"
                        wordDict = ["cat", "cats", "and", "sand", "dog"]
        Output:
            [
                "cats and dog",
                "cat sand dog"
            ]
        cur=end=0
        s[cur:end] c         不在
                   ca        不在
                   cat       在,end=3  ，tmprs = "cat"
                        cur=end=3
                            s[cur:end]  s       不在
                                        sa      不在
                                        san     不在
                                        sand    在， end=7, tmprs="cat"+" "+"sand"
                                            cur=end=7
                                                s[cur:end]  d   不在
                                                            do  不在
                                                            dog 在， end=10，tmprs=“cat sand”+" "+dog
                                                            因为 end=len(s),所以rs.append(tmprs)
                   cats 在，end=4, tmprs="cats" 
        """        

        """"

        cur=0, pre="",rs=[]
            end=0   x
            end=1   x
            ...
            end=3   s[cur:end]=cat, pre=""+"cat"
                        dfs(3,"cat",[])
                            cur=3,pre="cat",rs=[]
                                end=3   x
                                end=4   x
                                ...
                                end=7 ,s[cur:end]=sand, pre="cat sand", rs=[]
                                    dfs(7,"cat sand",[])不返回什么，只是把rs处理了
                                        cur=7, pre="cat sand", rs=[]
                                            end=7   x
                                            ...
                                            end=10  s[cur:end]=dog, pre="cat sand dog" ,rs=[]
                                                    ->end=len(s), rs=["cat sand dog"]
                                                    return
            end = 4 [cur:end] = cats, pre                 




        """
        rs = []
        tmprs=[]
        return self.dfs(s, wordDict, [], rs)

    def dfs(self, s, wordDict, [],rs ):
        for word in wordDict:
            l = len(word)
            if s[:l] == word:
                rs = self.dfs(s[l:], wordDict, [],rs)



        # def dfs(s, curIndex, wordDict, preS,rs):
        #     print("pres= ",preS,curIndex)
        #     for endIndex in range(curIndex, len(s)+1):
        #         if curIndex == 0: preS = []
        #         if s[curIndex:endIndex] in wordDict:
        #             print(curIndex,'-',endIndex)
        #             print(" ",s[curIndex:endIndex],' -> ',end="")
        #             preS.append(s[curIndex:endIndex])
        #             if endIndex == len(s):  
        #                 print('     ---over:',preS)
        #                 rs.append(" ".join(preS))
        #                 # preS = []
        #                 return
        #             print(' check ',s[endIndex:])
        #             dfs(s, endIndex, wordDict, preS,rs)
        #     return False
        # rs = []
        # dfs(s,0, wordDict,[],rs)
        # return rs
so = Solution()
s = "catsanddog";   wordDict = ["cat", "cats", "and", "sand", "dog"]
s = "pineapplepenapple";    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]

# s = "catsandog";    wordDict = ["cats", "dog", "sand", "and", "cat"]
print(so.wordBreak(s, wordDict))