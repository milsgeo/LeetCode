class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n,m = len(nums1), len(nums2)
        dp=[[0]*(m+1) for _ in range(n+1)] #adding 1 for empty "0"
        output=0
        for i in range(n):
            for j in range(m):
                if nums1[i]==nums2[j]:
                    dp[i][j]=1+dp[i-1][j-1]
                    output=max(output, dp[i][j])
        return output
        