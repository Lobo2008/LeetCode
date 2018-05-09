"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

Note:

    s could be empty and contains only lowercase letters a-z.
    p could be empty and contains only lowercase letters a-z, and characters like . or *.

Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".

Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false


"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        import re
        rs = re.search(p, s)
        if rs and rs.group() == s:            
            return True
        return False


so = Solution()

s = "aab"; p = "c*a*b"
# s = "aa"; p = "a"


# print(so.isMatch(s, p))

test_case = {"aa":"a", "aa":"a*", "ab":".*", "aab":"c*a*b", "mississippi":"mis*is*p*."}
test_case = {'a':'aa','a*': 'aa', '.*': 'ab', 'c*a*b': 'aab', 'mis*is*p*.': 'mississippi'}
#F T T T F
for i in test_case:
    rs = so.isMatch(test_case[i],i)
    print(i,':',test_case[i],'   ->',rs)