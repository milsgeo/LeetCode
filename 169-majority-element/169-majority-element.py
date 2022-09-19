class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq_dict={}
        for num in nums:
            if num not in freq_dict:
                freq_dict[num]=1
            else:
                freq_dict[num]+=1
        
        n=len(nums)
        for i in freq_dict:
            if freq_dict[i]>n/2:
                return i