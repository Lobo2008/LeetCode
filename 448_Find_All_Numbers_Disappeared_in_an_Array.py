"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]



"""


class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        [4,3,2,7,8,2,3,1]

        n[0] = 4
        n[3] = 7
            ->  n[0] = n[0]+n[3] = 11
                n[3] = n[0] - n[3] = 11-7=4
                n[0] = n[0]-n[3]= 11-4=7
                ->n[0]=7
                  n[3]=4


        a = 3 b = 7
        不用额外空间交换两个数字
        a = a+b = 10
       
        b = a - b = 3
        a = a - b = 7


        [4,3,2,7,8,2,3,1]
        indx=1,  n[0]=4 x   ->  [7,3,2,4,8,2,3,1]
        indx=1,  n[0]=7 x   ->  [3,3,2,4,8,2,7,1]
        indx=1,  n[0]=3 x   ->  [2,3,3,4,8,2,7,1]
        indx=1,  n[0]=2 x   ->  [3,2,3,4,8,2,7,1]
        indx=1,  n[0]=3 x   ->  [3,2,3,4,8,2,7,1]
            the same:           [-1,2,3,4,8,2,7,1]
        indx=2  n[1]=2 v next
        indx=3  n[2]=3,v next
        """
        if not nums:    return []
        index = 1
        while index <= len(nums):
            while nums[index - 1] != index and nums[index-1] != -1:
                c = nums[index - 1] 
                tmp = nums[c-1]
                if c == tmp:
                    nums[index-1]=-1
                    break
                else:
                    nums[c-1] = c
                    nums[index - 1] = tmp
            index += 1
        return [i for i,c in enumerate(nums,1) if i != c ]

        

so = Solution()

nums = [4,3,2,7,8,2,3,1]

print(so.findDisappearedNumbers(nums))