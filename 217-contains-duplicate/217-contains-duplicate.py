class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dup_set={}
        
        for i in nums:
            if i in dup_set:
                return True
                dup_set[i]+=1
            else:
                dup_set[i]=1
        return False