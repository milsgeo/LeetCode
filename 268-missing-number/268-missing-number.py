class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numset=set(nums)
        print(numset)
        n=len(nums)+1
        for number in range(n):
            if number not in numset:
                return number