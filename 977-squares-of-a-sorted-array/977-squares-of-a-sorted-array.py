class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # squared_nums=[]
        # for i in range(len(nums)):
        #     sq=nums[i]*nums[i]
        #     squared_nums.append(sq)
        # return sorted(squared_nums)
        
        n=len(nums)
        result=[0]*n
        l,h=0,n-1
        for i in range(n-1,-1,-1):
            if abs(nums[l])<abs(nums[h]):
                sq=nums[h]
                h-=1
            else:
                sq=nums[l]
                l+=1
            result[i]=sq*sq
        return result
            
        