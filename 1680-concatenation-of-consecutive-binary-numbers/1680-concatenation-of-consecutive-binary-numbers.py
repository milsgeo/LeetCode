class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod=10**9+7
        tmp=""
        
        for i in range(1,n+1):
            tmp+=bin(i)[2:]
        return int(tmp,2)%mod