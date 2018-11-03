"""
Given an array nums of n integers and an integer target, 
find three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. You may assume that each input would have exactly one solution.

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


"""
class Solution(object):



    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """
        #ref https://leetcode.com/problems/3sum-closest/discuss/7871/Python-O(N2)-solution/8988
        #[-20, -4, -1, -1, 0, 1, 2, 7, 20] ,target= 15

        先排序，然后固定一个数，然后每次从这个数后面的数开始找，用两个指针

        比如，固定 -4（下标index=1），然后从剩下的元素newnum=[-1, -1, 0, 1, 2, 7, 20] 中开始找
        两个指针，一个指针指向newnums的最左边，一个指向最右边（还原到nums里的下标就是left=index+1，right=len(nums)-1）
        然后求三个数的和 sum = index + left + right ,注意，index是固定的，所以内循环每次更新 l 和r即可
        如果  sum与target的差距（sum-target）小于  上一次的差距  (rs-tagget)，则更新结果

        sum每次和target比较，如果小于target，则左指针右移，反之右指针左移，相等的时候就是结果

        """
        if len(nums) < 3:return 
        nums.sort()
        rs = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                tmpsum = nums[i] + nums[l] + nums[r]
                if tmpsum == target:
                    return tmpsum
                if abs(tmpsum - target) < abs(rs - target):
                    rs = tmpsum
                if tmpsum < target:
                    l += 1
                if tmpsum > target:
                    r -= 1
        return rs




    def threeSumClosest_old(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """
        先找出threesum的组合，然后sum每个组合，遍历一遍就可以了？
        a+b+c-target = x
        min(x)
        
        [-20,-4, -1, -1, 0, 1, 2,7,20] target = 13
                => [-4,-1,20]  -4-1+20=15 最接近13

        先找 target-a最小的，然后(target-a)-b最小的，最后(target-a-b)-c最小的

        设置初始的最小最近值是前三个数相加，即min(x0)=clo =(-20)+(-4)+(-1) - 13 = -38

        先固定一个元素a，比如-20，然后从[-4,-1, -1, 0, 1, 2,7,20]中找离新目标 newTarget=13-(-20)=33最近的元素
            两个数初始最小值 clo2 = (-4)+(-1)=-5-target = -38
            最边上两个数字和，(-4)+20 = 16 ->  16-newtarget(33) = -17  
                abs(-17)< abs(-38),距离比clo2更近,则当前最近就是 -17,
                同时这两个和小于newtarget，所以从右边往左逼近 <--
                vice versa
            最后可以找到固定-20的时候[-4,-1, -1, 0, 1, 2,7,20]距离newtarget最近的值
        如果这个值小于三元素的clo，则对clo进行更新，遍历万以后可以找到全局最小的那一个

            用夹逼的方法，如果从两边迫近，
             如果nums[low]+nums[high]= newtarget，则已经找到
             如果nums[low]+nums[high] > newtarget，说明数字太大，右边往左逼近
             如果nums[low]+nums[high] < newtarget,说明数字太小，左边往右逼近
             每次nums[low]+nums[high] - newtarget的值都要进行判断            
        """
        nums.sort()
        if len(nums) <=3: return sum(nums)
        print('-----ori:',nums,',target=',target)
        closet = nums[0] + nums[1] + nums[3] - target
        i = 0
        while i <= len(nums)-3:
            newTarget = target -nums[i]
            if  i >= 1 and nums[i] == nums[i-1] and i < (len(nums)-3):
                while nums[i] == nums[i-1] and i <(len(nums)-3) :
                    i += 1
                continue
            low, high = i+1, len(nums)-1
            closet2 = nums[low] + nums[low+1] - newTarget
            while low <high:
                diff =  nums[low] + nums[high] - newTarget
                if diff == 0:#差值为0，说明找到了直接返回
                    return target
                elif diff > 0:#太大了，所以往左逼近
                    high -= 1
                    while  low < high and nums[high] == nums[high+1] and high > 2:
                        high -= 1
                else:#太小了，所以往右逼近
                    low += 1
                    while low < high and nums[low] ==  nums[low-1] and low < len(nums)-2:
                        low += 1
                closet2 = diff if abs(diff) < abs(closet2) else closet2
            closet = closet2 if abs(closet2) < abs(closet) else closet
            i += 1
        return closet+target 



    """
    有更多注释、打印的代码
    """
    def threeSumClosest1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """
        先找出threesum的组合，然后sum每个组合，遍历一遍就可以了？
        a+b+c-target = x
        min(x)
        
        [-20,-4, -1, -1, 0, 1, 2,7,20] target = 13
                => [-4,-1,20]  -4-1+20=15 最接近13

        先找 target-a最小的，然后(target-a)-b最小的，最后(target-a-b)-c最小的

        设置初始的最小最近值是前三个数相加，即min(x0)=clo =(-20)+(-4)+(-1) - 13 = -38

        先固定一个元素a，比如-20，然后从[-4,-1, -1, 0, 1, 2,7,20]中找离新目标 newTarget=13-(-20)=33最近的元素
            两个数初始最小值 clo2 = (-4)+(-1)=-5-target = -38
            最边上两个数字和，(-4)+20 = 16 ->  16-newtarget(33) = -17  
                abs(-17)< abs(-38),距离比clo2更近,则当前最近就是 -17,
                同时这两个和小于newtarget，所以从右边往左逼近 <--
                vice versa
            最后可以找到固定-20的时候[-4,-1, -1, 0, 1, 2,7,20]距离newtarget最近的值
        如果这个值小于三元素的clo，则对clo进行更新，遍历万以后可以找到全局最小的那一个

            用夹逼的方法，如果从两边迫近，
             如果nums[low]+nums[high]= newtarget，则已经找到
             如果nums[low]+nums[high] > newtarget，说明数字太大，右边往左逼近
             如果nums[low]+nums[high] < newtarget,说明数字太小，左边往右逼近
             每次nums[low]+nums[high] - newtarget的值都要进行判断            
        """
        nums.sort()
        if len(nums) <=3:return sum(nums)
        print('-----ori:',nums,',target=',target)
        closet = nums[0] + nums[1] + nums[3] - target
        i = 0
        # for i in range(len(nums)-2):
        while i <= len(nums)-3:
            a = nums[i]
            newTarget = target - a
            """
            如果固定的元素一样，前一个处理了以后，直接跳过，比如[-4,-1,-1,0,1,1,1]，
            固定了-4，然后是-1 ，再接着一个-1，而第二个-1可以不用处理了，直接跳过到0
            因为要留给low和high至少各一个元素，所以最多能跳到倒数第3个

            跳过重复元素的优化，可以将耗时从171ms降到121ms
            """
            if  i >= 1 and nums[i] == nums[i-1] and i < (len(nums)-3):
                print('~~~~~~~~~~~~~~~~~~',nums[i],' - ',nums[i-1])
                print('**** before i=',i)
                while nums[i] == nums[i-1] and i <(len(nums)-3) :
                    i += 1
                    print('**** i=',i)
                continue
            print('      i=',i)
            print('先固定 ',a,'，然后从 ',nums[i+1:],'中找离 ',newTarget,'最近的元素')
            low = i+1
            high = len(nums)-1
            closet2 = nums[low] + nums[low+1] - newTarget
            while low <high:
                #twosum的 初始最小差值
                print(' ',nums[low],' + ',nums[high],' = ',nums[low] + nums[high],' VS ',newTarget,' min=',closet2)
                diff =  nums[low] + nums[high] - newTarget
                print('         diff=',diff)
                if nums[low] + nums[high] == newTarget:#差值为0，说明找到了直接返回
                    print('****BINGO****')
                    return target
                elif nums[low] + nums[high] > newTarget:#太大了，所以往左逼近
                    print('  太大了，所以往 <-- 逼近')
                    high -= 1
                    print('high before=',high)
                    """
                    [1,1,1,1,1,1]这种，因为固定元素占了一个，low占了一个，所以high最多能降到第3个元素，所以下标大于2的时候才能减一
                    """
                    while  low < high and nums[high] == nums[high+1] and high  > 2:

                        high -= 1
                        print('high=',high)
                else:#太小了，所以往右逼近
                    low += 1
                    print('    太小了，所以往 --> 逼近')
                    """
                    [1,1,1,1,1,1]这种，因为固定元素占了一个，high占了一个，所以low最多能升到倒数第2个元素
                    """
                    while low < high and nums[low] ==  nums[low-1] and low < len(nums)-2:
                        low += 1
                if abs(diff) < abs(closet2):#更新差值
                    print('    更新差值为,',diff)
                    closet2 = diff#固定元素nums[i]时的min(x)
            print('-----所以最小差值为 ',closet2)
            if abs(closet2) < abs(closet):#全局min(x)
                closet = closet2
            i += 1
        return closet+target 




        
so = Solution()
nums = [-1, 2, 1, -4]; target = 1
nums = [-20,-4, -1, -1, 0, 1, 2,7,20] ;target = 15
# nums = [1,1,1,1,1,1,1,1]; target=0
# print(so.threeSumClosest1(nums, target))
print(so.threeSumClosest(nums, target))





