class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        l,h=0,n-1
        vol=0
        while l<h:
            width=h-l
            vol=max(vol,min(height[l],height[h])*width)
            if (height[l]<=height[h]):
                l+=1
            else:
                h-=1
        return vol