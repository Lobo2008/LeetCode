"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.




"""

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        """
        beginWord = "hit",
        endWord = "cog",
        wordList = ["hot","dot","dog","lot","log","cog"]


        vi=[hit],dist = 1
            1)word=hit
              tmp=[h,i,t]
              i=0
                j=a -> tmp=ait
                j=b -> tmp=bit
                ...
                j=z -> tmp=zit
              i=1
                j=a
                ...
                j=o -> tmp=hot bingo!
                    vi=[hot]
                    wordlist=^hot
                    dist=2
              i=2
            2)vi=[hot]
        ...

        将hot变换一个字母的所有可能性找出来，比如
        变换第一位时可能为：aot bot cot dot...lot...zot 其中dot和lot在字典中
        变换第二位时可能为：hat hbt hct .... hzt 
        变换第三位时可能为：hoa hob ...hoz
        
        如果在字典中，就ok，放入下一轮遍历的结果中nextlevel，直到
            下一轮要遍历的单词中含有endword的时候，或者下一轮为空的时候（说明已经没有变换的可能性了）

        Warning:
            1)字典一定要去重
            2)

        """
        visited = set()
        visited.add(beginWord)
        wordList = set(wordList)
        dist = 1
        if beginWord in wordList:
            wordList.remove(beginWord)
        while endWord not in visited :#找到立即停止
            nextLevel = set()
            for word in visited:
                for i in range(len(word)):
                    tmp = list(word)
                    for j in range(ord('a'),ord('z')+1):
                        tmp[i] = chr(j)
                        if ''.join(tmp) in wordList:
                            nextLevel.add(''.join(tmp))
                            wordList.remove(''.join(tmp))
            """
            找一轮，距离+1，下一轮为空的时候，说明没有，则停止
            """
            dist += 1
            if len(nextLevel) == 0:#没找到下次变换，则错误
                return 0
            visited = nextLevel
        return dist

so = Solution()

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
# wordList = ["hot","dot","dog","lot","log"]
wordList = ["hot","cog","dot","dog","hit","lot","log"]


beginWord="teach"
endWord="place"
wordList=["peale","wilts","place","fetch","purer","pooch","peace","poach","berra","teach","rheum","peach"]
print(so.ladderLength(beginWord, endWord, wordList))
