class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largestSum=nums[0]
        sumnum=nums[0]
                
        for i in range(1,len(nums)):
            num=nums[i]
            sumnum=max(num,sumnum+num)
            largestSum =max(sumnum,largestSum)        
        
        return largestSum