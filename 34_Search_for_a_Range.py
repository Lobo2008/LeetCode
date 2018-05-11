"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
主要的难点在于复杂度，因为是logn，所以可以用二分法

"""
class Solution(object):

    """
    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]

    Input: nums = [5,6,6,8,8,10], target = 7
    Output: [-1,-1]
    """
    #nums = [4,5,6,8,8,10]; target = 7
    def recurssive(self,nums,low,mid,high,target):
        print('~~~~~~~~IN')
        if low == high:
            return low
        
        if target < nums[mid]:
            print('~~~~1')
            high = mid - 1
        elif target > nums[mid]:
            print('~~~~2')
            low = mid + 1
        else:
            print('~~~~3')
            return mid
        mid = (low + high)//2
        # so = Solution
        self.recurssive(nums,low,mid,high,target)
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        先找一个target，然后从target往左右两边再进行二分查找
        """

        low ,high = 0,len(nums)
        start, end = -1, -1
        if not nums or target > nums[high-1] :return [start, end]
        print(nums)
        while low <= high:#这里要用=号，因为如果只有一个target时，low=high即target
            mid = (low + high)//2
            if nums[mid] == target:#找到一个target立刻停止
                break
            elif nums[mid] > target:
                high = mid - 1
            else: 
                low = mid + 1
        if nums[mid] != target:[start,end]#如果连target都没找到，那元素不存在
        #look4the lowbound'往左找下界，同样也是二分查找
        ll,lh = 0,mid 
        while ll <= lh:  
            nm = (ll + lh)//2
            if nums[nm] == target:#找到下界，继续再二分找
                lh = nm - 1
                start = nm
            else:
                ll= nm + 1
        #look4the upbound 往右找上界
        hl,hh = mid ,len(nums)-1
        while hl <= hh:
            nm = (hl + hh)//2
            if nums[nm] == target:#找到后，继续往中点的右边二分查找
                hl = nm + 1  
                end = nm    
            else:
                hh = nm -1
        return [start,end]



    def searchRange2(self, nums, target):
        start, end = -1, -1
        low, high = 0,len(nums)-1
        if not nums or target > nums[high] :return [start, end]
        while low <= high:
            mid = (low + high) // 2
            print(low,mid,high)
            if nums[mid] == target:
                high = mid -1
                start = mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        low, high = 0,len(nums)-1
        while low <= high:
            mid = (low + high) // 2
            print(low,mid,high)
            if nums[mid] == target:
                low = mid + 1
                end = mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return [start,end]



so = Solution()

nums = [4,5,6,8,8,8,8,8,8,10,11,12]; target = 8
# nums = [5,7,7,8,10]; target = 9
# nums = [];target = 1
low = 0
high = len(nums)
mid = (low+high)//2
# print(so.recurssive(nums,low,mid,high,target))
print(so.searchRange2(nums,target))

