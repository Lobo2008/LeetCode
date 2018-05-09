class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        maxlen = start = 0
        usedChar = {}
        for i, c in enumerate(s):
            if c in usedChar and start <= usedChar[c]:
                start = usedChar[c] + 1
            else:
                maxlen = max(maxlen, i - start + 1)
            usedChar[c] = i
        return maxlen

