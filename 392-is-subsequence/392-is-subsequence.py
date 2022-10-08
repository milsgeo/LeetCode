class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        lens=len(s)
        lent=len(t)
        left, right=0,0
        while left <lens and right <lent:
            if(s[left]==t[right]):
                left+=1
            right+=1
        return left==lens