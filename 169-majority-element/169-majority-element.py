class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsSeen={}
        for i in nums:
            if i in numsSeen:
                numsSeen[i]+=1
            else:
                numsSeen[i]=1
            
        for i in numsSeen:
            if numsSeen[i]>(len(nums)//2):
                return i