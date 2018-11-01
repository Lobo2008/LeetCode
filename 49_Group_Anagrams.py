"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        """
        每个单词，转换成数字以后，异或，比如 
        eat分别对应 101 97 116
        tea分别对应 116 101 97
        则将这6个数字异或以后，结果是0，说明应该分为一组
        每个元素与其他所有元素进行比较，复杂度O(n^2)
        """
        d = {}
        for word in strs:
            key = tuple(sorted(word))
            #d={"key1":["name1","name2"]}
            # d.get('key1') 的结果是一个list，即["name1","name2"]，所以可以直接加[word]
            d[key] = d.get(key, []) + [word]
        return list(d.values())

        
so = Solution()

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

# strs = ["eat", "nat", "bat"]

# strs = ["eat","tea"," "," "]
print(so.groupAnagrams(strs))