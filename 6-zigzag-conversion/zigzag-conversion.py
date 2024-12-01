class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        rows=[""]*numRows
        step,index=0,0

        if numRows<=1:
            return s

        for char in s:
            rows[index]+=char
            if index==0:
                step=1
            elif index==numRows-1:
                step=-1
            index+=step

        return "".join(rows)

        
        
        
        '''
        columns=[]
        rows=[]
        n=len(s)
        i,k=0,0
        
        while i<n:
            if k ==0:
                temp=[]
                for j in range(numRows):
                    if i<n:
                        temp.append(s[i])
                        i+=1
                    else:
                        break
                columns.append(temp)
                k=numRows-2
                if k<0:
                    k=0
            else:
                temp=[]
                for l in range(numRows):
                    if l==k:
                        temp.append(s[i])
                    else:
                        temp.append(" ")
                columns.append(temp)
                k-=1
                i+=1

        for i in range(numRows):
            rows.append([columns[j][i] for j in range(len(columns)) if i<len(columns[j]) and columns[j][i]!=" "])

        return ''.join([''.join(row) for row in rows])
        '''

