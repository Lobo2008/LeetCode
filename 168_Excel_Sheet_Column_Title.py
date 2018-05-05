"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...

Example 1:

Input: 1
Output: "A"

Example 2:

Input: 28
Output: "AB"

Example 3:

Input: 701
Output: "ZY"

52 AZ
53 BA
78  BZ
1000100 BDWKJ
841 "AFI"
分析： A要和A-Z进行组合，
      B要和A-Z进行组合

十進位整數      1   2   ...  26   27  ...  52
對應字串        A   B   ...  Z    AA  ...  AZ
除以 26 之商    0   0   ...  1    1   ...   2
除以 26 之餘    1   2   ...  0    1   ...   0

我們會發現:

    如果不是整除的話(餘數不為零)，那規則跟進位轉換沒兩樣，可以直接用餘數查詢對應的符號，並且用 商 作被除數來做下一次的除法

    [坑]如果整除(餘數為零)，我們則必須取最後一個符號，且下一次的除法要用 (商-1) 來當被除數做下一次的除法

"""

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <1:return ""
        letter = []
        letter.append("")
        for x in range(65,65+26,1):
            letter.append(chr(x))
        res = ""
        while n != 0:
            r = n % 26 
            n = int(n/26)
            if r == 0:
                res += letter[26]
                n -= 1
            else:
                res += letter[r]
        return res[::-1]
        
n = -1
so = Solution()
res = so.convertToTitle(n)
print(res)


test_case={0:"",1:"A",28:"AB",701:"ZY",52:"AZ",53:"BA",78:"BZ",1000100:"BDWKJ",841:"AFI"}
for item in test_case:
    rs = so.convertToTitle(item)
    if rs == test_case[item]:
        flag = "V"
    else: flag = "X"
    print(item,'=>',rs,'  ',flag) 