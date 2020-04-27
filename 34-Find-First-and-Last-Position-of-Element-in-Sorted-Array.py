class Solution:
    """
    binary search
    """
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low + high)//2
            if target > nums[mid]:
                low += 1
            elif target < nums[mid]:
                high -=1
            elif target == nums[mid]:
                low = mid
                high = mid
                while (low-1)>=0 and target == nums[low-1]:
                    low -= 1
                while high+1<len(nums) and target == nums[high+1]:
                    high += 1
                break
                
        if low > high:
            return [-1, -1]
        else:
            return [low, high]