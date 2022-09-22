class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # pas=[[1]]
        # for i in range(1, rowIndex+1):
        #     tmp=[1 for _ in range(i+1)]
        #     for j in range(1, len(tmp)-1): #we only want the middle portion
        #         tmp[j]=pas[-1][j]+pas[-1][j-1]
        #     pas.append(tmp)
        # return pas[-1]
    
    #O(k) space
    
        output=[1]
        for i in range(1, rowIndex+1):
            output.append(1)
            for j in range(len(output)-2, 0, -1):
                output[j]+=output[j-1]
        return output           