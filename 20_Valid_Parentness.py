"""
()  -->  True
()[]{}  -->  True
(]  -->  False
([)]  -->  False
{[]}  -->  True
((  -->  False
]  -->  False
运用堆栈的概念，list好像就可以

"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stackList = [None] #必须为None，因为如果是 "]"，则一开始就进如判断：而stackList=[]的话，stackList.pop()会报错，溢出 
                            #或者可以做个判断，因为第一个输入必须会是左括号，否则就应该报错
        matchDict = {"}":"{", ")":"(", "]":"["}
        for c in s:
            if c in matchDict:# 右括号 ， key是否在matchDict中
                # print("  right")
                if matchDict[c] != stackList.pop():#右括号key对应的值（左括号）是否相等
                    return False
            else:#左括号，压入栈
                stackList.append(c)
        return len(stackList) == 1

    """
    一个更容易理解的写法
    """
    def isValid_2(self,s):
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif not stack:
                return False
            elif c == ')' and stack.pop() != '(':
                return False
            elif c == '}' and stack.pop() != '{':
                return False
            elif c == ']' and stack.pop() != '[':
                return False
        return not stack


s = "{[]}"
# s = "()[]{}"
# res = Solution.isValid(1,s)
# print(res)

# """
test_case={"()":True, "()[]{}":True,  "(]":False, "([)]":False, "{[]}":True, "((":False,"]": False}
for item in test_case:
    res = Solution.isValid(1,item)
    if res == test_case[item]:
        judge = "v"
    else:
        judge = "x"
    print(item,' --> ',res,"  ")

# """