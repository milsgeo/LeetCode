class Solution:
    def search(self, nums: List[int], target: int) -> int:
    
        n=len(nums)
        
        l,h=0,n-1
        
        while( h >=l):
            mid=l+(h-l)//2
            if(target==nums[mid]):
                return mid;
            elif(target>nums[mid]):
                l=mid+1
            else:
                h=mid-1
        else:
            return -1
            