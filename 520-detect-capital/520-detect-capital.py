class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        length=len(word)
        
        if(length==1):
            return True
        
        if(word[0].isupper() and word[1].isupper()):
            for i in range(2,length):
                if not word[i].isupper():
                    return False
        else:
            for i in range(1,length):
                if(word[i].isupper()):
                    return False
        return True
    
                