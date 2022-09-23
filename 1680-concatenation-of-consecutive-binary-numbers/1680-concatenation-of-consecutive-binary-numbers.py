class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod=10**9+7
        tmp=0
        
        # for i in range(1,n+1):
        #     tmp+=bin(i)[2:]
        # return int(tmp,2)%mod
        
        for i in range(1, n+1):
            tmp=2**(len(bin(i))-2)*tmp +i
            tmp%=mod
        return tmp