class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        n=len(gas)
        i=0

        while i<n:
            j=i
            currGas=0
            stationCount=0
            while stationCount < n:
                currGas+=gas[j%n]-cost[j%n]
                if currGas<0:
                    break
                stationCount+=1
                j+=1  
            if stationCount==n and currGas>=0:
                return i
            i=j+1
        return -1
        





        