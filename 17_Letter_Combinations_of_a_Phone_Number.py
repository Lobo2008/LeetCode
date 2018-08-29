"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].


"""
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        """
        有点bfs的意思？
        比如234
        第一次，那一个数字作为循环列表 rs:[a,b,c]
        然后，用这个rs列表的每一个元素，跟下一个数字对应的每一个元素两个组合，放入下次遍历的列表
        next=['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
        待rs中的元素都处理完以后，将next作为下一次循环的列表，rs=next，然后再遍历每个元素，将其与下一个数字对应的元素组合

        """

        if len(digits) == 0:    return []
        mapDict = {"1":"*","2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        rs = []
        #初始化结果列表
        for i in mapDict[digits[0]]:
            rs.append(i)

        from collections import deque
        newRs = []
        rs = deque(rs)
        index = 1
        alpha = [chr(i) for i in range(97,123)]+['*']

        while rs and index < len(digits):
            i = rs.popleft()
            for j in mapDict[digits[index]]:
                if j not in alpha: return [" "]
                newRs.append(i+j)
            if len(rs) == 0:
                index += 1
                rs = deque(newRs)
                newRs = []
        return list(rs)

        




digits = "23"

res = Solution.letterCombinations(1,digits)

print(res)