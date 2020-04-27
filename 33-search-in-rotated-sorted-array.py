# 33. Search in Rotated Sorted Array
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """
        First find the index of the smallest element in the array, the initial index, with binary search. Then, imagine a sorted array to do binary search, and find the real-index with the initial index.
        """
        
        n = len(nums)
        left = 0
        right = n-1
        
        #find the index of the smalled number
        while left < right:
            mid = (left+right)//2
            
            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid
        
        
        initial = left
        left = 0
        right = n-1
        while left <= right:
            mid = (left+right)//2
            real_mid = (mid+initial)%n
            if target == nums[real_mid]:
                break
            if target < nums[real_mid]:
                right = mid-1
            elif target > nums[real_mid]:
                left = mid+1
        
        if left > right:
            return -1
        else:
            return real_mid
        
        