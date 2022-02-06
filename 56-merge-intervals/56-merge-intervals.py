class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # # newArr=[]
        # l=len(intervals)
        # # newele=[]
        # for i in range(l-1):
        #     # for j in range(l-1):
        #     if(intervals[i][1]>=intervals[i+1][0]):
        #         newele=[intervals[i][0], intervals[i+1][1]]
        #         # return [[intervals[i][0], intervals[i+1][1]]]
        #         intervals[i]=intervals[newele]
        #         intervals.pop(i+1)
        # # newArr.append(newele)
        # # if(l>2):
        # #     newArr.extend(intervals[i:]) 
        # # else:
        # #     return newArr
        # # return newArr
        # return intervals 
        
        intervals.sort(key=lambda i:i[0])
        output=[intervals[0]]
        
        for start,end in intervals[1:]:
            lastend=output[-1][1]
            # print(lastend)
            if start <=lastend:
                #end value of the most recently added interval
                output[-1][1]=max(lastend,end)
                # print(output[-1][1])
            else:
                output.append([start,end])
        return output