"""
Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

注意：只需要存当前最大的长度即可

载入 p时，没问题，此时最大长度为1，起始位置为0
载入 w1时，没问题，此时最大长度为2，起始位置还是0
载入 w2时，有情况！w重复了，则目前最大长度就是刚才的pw1的长度2，起始位置就是w2的下标

因为只需要获取长度，二不用找出最大串，所以可以用键值对互换的存储方式，最大长度就是当前字符的下标-起始位置+1

"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = maxLen = 0
        usedChar = {}
        print (s)
        for i in range(len(s)):
            print('it is:',i,'=>',s[i],'    ',usedChar)
            if s[i] in usedChar and start <= usedChar[s[i]]:
                    print('字符已存在')
                    start = usedChar[s[i]] + 1
                    #有重复的字符，则起始位置变成重复字符的下一个
                    #如pw时起始位置时0，第三个字符w载入，已存在！则新的起始位置变成第三个（也就是2）
                    # 然后把pw的长                                            
            else:
                print('字符不存在')
                maxLen = max(maxLen, i - start + 1)
            usedChar[s[i]] = i #键值对互换的存储方式
            print('usedChar: ',usedChar,',max = ',maxLen,', start = ',start,'\n')
        return maxLen




s = 'pwwkew'
res = Solution.lengthOfLongestSubstring(1,s)
print (res)