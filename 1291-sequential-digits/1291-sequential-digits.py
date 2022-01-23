class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        
        digits = "123456789"
        out = []
        lenlow = len(str(low))
        lenhigh = len(str(high))
        
        for i in range(lenlow, lenhigh + 1):
            for j in range(0, 10 - i):
                num = int(digits[j: j + i])
                if num >= low and num <= high: 
                    out.append(num)
        return out;