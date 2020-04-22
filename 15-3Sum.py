"""
15. 3Sum
Sort the input array and use two pointers l and r to make the sum of three integers approximate 0. 
Pay attention to avoid putting the same triplets in the output by skipping the same nums in iteration.
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []
        for i in range(len(nums)-2):
            #avoid repetition
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i+1
            r = len(nums) - 1
            while l < r:
                sum_ = nums[i] + nums[l] +nums[r]
                if sum_ == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    #avoid repetition
                    while l < r and nums[l] == nums[l+1]:
                        l+=1
                    #avoid repetition
                    while l < r and nums[r] == nums[r-1]:
                        r-=1
                    l+=1
                    r-+1
                elif sum_ < 0:
                    l+=1
                elif sum_ > 0:
                    r-=1
                    
        return res