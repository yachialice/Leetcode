"""
The solution is similar to NO.15 3SUM
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        res = nums[0] + nums[1] + nums[-1]
        
        for i in range(0, len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l<r:
                sum_ = nums[i] + nums[l] + nums[r]
                if abs(target - sum_) < abs(target - res):
                    res = sum_
                if sum_ < target:
                    l+=1
                elif sum_ > target:
                    r-=1
                elif sum_ == target:
                    return sum_
        
        return res