class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count=Counter(nums)
        nums=sorted(list(set(nums)))
        
        prev1,prev2=0,0
        
        for i in range(len(nums)):
            curr=nums[i]*count[nums[i]]
            
            if i>0 and nums[i]==nums[i-1]+1:
                temp=prev2
                prev2 = max(curr+prev1,prev2)
                prev1=temp
                
            else:
                temp=prev2
                prev2=max(curr+prev2,prev1)
                prev1=temp
        
        return prev2