class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared_nums=[]
        for i in range(len(nums)):
            sq=nums[i]*nums[i]
            squared_nums.append(sq)
        return sorted(squared_nums)
        