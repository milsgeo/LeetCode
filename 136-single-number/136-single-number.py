class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dup_nums={}
        for num in nums:
            if num in dup_nums:
                dup_nums[num]+=1
            else:
                dup_nums[num]=1
        for i in dup_nums:
            if dup_nums[i]==1:
                return i