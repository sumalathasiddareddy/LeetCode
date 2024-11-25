class Solution:
    def predictPartyVictory(self, senate: str) -> str:
       
        n= len(senate)

        rInd = deque()
        dInd = deque()

        for i in range(n):
            if senate[i]=='D':
                dInd.append(i)
            else:
                rInd.append(i)

        while rInd and dInd:
            r=rInd.popleft()
            d=dInd.popleft()
            if r<d:
                rInd.append(n+r)
            else:
                dInd.append(n+d)
           
        return "Radiant" if len(rInd)>0 else "Dire"