class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if (len(intervals)<2):
            return intervals
        intervals.sort()
        output=[intervals[0]]
        
        for l,r in intervals[1:]:
            if l > output[-1][1]: #previous one's end
                output.append([l,r])
            elif r > output[-1][1]:
                output[-1][1]=r
        return output