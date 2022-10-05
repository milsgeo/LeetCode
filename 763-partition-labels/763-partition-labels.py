class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last={c:i for i,c in enumerate(s)}
        # print(last)
        output=[]
        max_index=-1
        size=1  #size of array being built up so far
        for i,c in enumerate(s):
            max_index=max(max_index, last[c])
            if i == max_index:
                output.append(size)
                size=1
            else:
                size+=1
        return output
        