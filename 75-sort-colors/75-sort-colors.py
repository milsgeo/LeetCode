class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # for i in range(len(nums)):
        #     while(i<len(nums)):
        #         if(nums[i]<nums[i+1]):
        #             nums[i], nums[i+1]=nums[i+1],nums[i]
        
#         l=0
#         h=len(nums)-1
        
        
#         while(l<=h):
#             if(nums[l]<nums[h]):
#                 l+=1
#             elif(nums[l]>nums[h]):
#                 # nums[l],nums[h]=nums[l],nums[h]
#                 temp=nums[l]
#                 nums[l]=nums[h]
#                 nums[h]=temp
#                 # l+=1
#                 h-=1
#             else:
#                 l+=1
#                 h+=1
#         return nums     

#         l=0
#         h=l+1
#         length=len(nums)
        
#         # while(l<=h and l<length and h<length):
#         #     if(nums[l]<=nums[h]):
#         #         l+=1
#         #         h+=1
#         #     else:
#         #         temp=nums[l]
#         #         nums[l]=nums[h]
#         #         nums[h]=temp
#         #         l+=1
#         #         h+=1
#         minNum=nums[0]
#         for i in range(length):
#             if(nums[i]<minNum):
#                 minNum=nums[i]

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if(nums[i]>nums[j]):
                    nums[i], nums[j]= nums[j], nums[i]
        
        return nums
        