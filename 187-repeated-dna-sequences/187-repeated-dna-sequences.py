class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        l,n=10, len(s)
        seen, output=set(), set()
        
        for start in range(n-l+1):
            temp=s[start:start+l]
            if temp in seen:
                output.add(temp[:])
            seen.add(temp)
        return output