class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        """
        sorting boxTypes according to the number of units as we want to get as much of those as possible.
        """
        boxTypes.sort(key=lambda x:-x[1])  #- indicates descending order 
        capacity=0
        
        for box,units in boxTypes:
            if truckSize >= box:
                truckSize -= box
                capacity += box*units
            else:
                capacity += truckSize*units
                break
        return capacity