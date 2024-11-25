class Solution:
    def predictPartyVictory(self, senate: str) -> str:
       
        n= len(senate)

        rInd = [i for i in range(n) if senate[i]=='R']
        dInd = [i for i in range(n) if senate[i]=='D']

        while rInd and dInd:
            r=rInd.pop(0)
            d=dInd.pop(0)
            if r<d:
                rInd.append(n+r)
            else:
                dInd.append(n+d)
           
        return "Radiant" if len(rInd)>0 else "Dire"