class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        senators = deque()
        
        while True:
            
            unvotedR=0
            unvotedD=0
            newstr=""

            if (senate==len(senate)*'R') or (senate==len(senate)*'D'):
                break
            
            for char in senate:
                if char=='D':
                    if unvotedR==0:
                        senators.appendleft(char)
                        unvotedD+=1
                    else:
                        unvotedR-=1
                elif char=='R':
                    if unvotedD==0:
                        senators.appendleft(char)
                        unvotedR+=1
                    else:
                        unvotedD-=1
                
            for char in ''.join(senators)[::-1]:
                if char=='R' and unvotedD>0:
                    unvotedD-=1
                    continue
                if char=='D' and unvotedR>0:
                    unvotedR-=1
                    continue
                newstr += char
            
            senate=newstr
            senators.clear()
                    
        return "Radiant" if senate[0]=='R'else "Dire"