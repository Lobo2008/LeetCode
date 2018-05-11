class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        dict = {}
        for i in range(len(num)):
            x = num[i]
            if target-x in dict:
                return (dict[target-x]+1, i+1)
            dict[x] = i



nums=[3,2,4]
res = Solution.twoSum(1,nums,9)
print (res)