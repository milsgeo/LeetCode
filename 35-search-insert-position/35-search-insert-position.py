class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        l,h=0,n-1
        while (l<=h):
            mid=l+(h-l)//2
            if(nums[mid]==target):
                return mid
            elif(target<nums[mid]):
                h=mid-1
            else:
                l=mid+1
        return l