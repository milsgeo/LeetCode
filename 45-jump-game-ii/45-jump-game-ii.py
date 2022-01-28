class Solution:
    def jump(self, nums: List[int]) -> int:
        dest=len(nums)-1
        count=0
        farthest=0
        l,r=0,0
        
        while r<dest:
            for i in range(l,r+1):
                farthest=max(farthest,i+nums[i])
            l=r+1
            r=farthest
            count+=1
        return count