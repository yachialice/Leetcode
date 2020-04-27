#35. Search Insert Position
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        """
        classic binary search
        """
    
        n = len(nums)
        left = 0
        right = n-1
        
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return left

