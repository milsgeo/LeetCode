class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        count=0
        
        start=sorted(i[0] for i in intervals)
        end=sorted(i[1] for i in intervals)
        l=len(intervals)
        
        sp=0
        ep=0
        
        while sp<l:
            if(start[sp]>=end[ep]):
                count -=1
                ep+=1
            count +=1
            sp+=1
            
        return count
        