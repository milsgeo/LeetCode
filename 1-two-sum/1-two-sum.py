class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_seen={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in num_seen:
                return [i,num_seen[diff]]
            num_seen[nums[i]]=i