class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        groups=[1]
        for i in xrange(1,len(s)):
            if(s[i-1]!=s[i]):
                groups.append(1)
            else:
                groups[-1]+=1 #increasing the size of the most recent group
            
        count=0
        
        for i in xrange(1,len(groups)):
            count+=min(groups[i-1],groups[i])
        return count