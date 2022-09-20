class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)==0:
            return None
        ans=0
        n=len(height)
        l,h=0,n-1
        left_max, right_max=0,0
        
        while(l<h):
            if(height[l]<height[h]):
                if height[l]>=left_max:
                    left_max = height[l] 
                
                ans+= left_max-height[l]
                l+=1
            else:
                if height[h]>=right_max:
                    right_max = height[h] 
                
                ans+= right_max-height[h]
                h-=1
        return ans