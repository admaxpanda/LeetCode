class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull=[0]*10
        cnts=[0]*10
        cntg=[0]*10
        for i in range(len(secret)):
            x=int(secret[i])
            y=int(guess[i])
            cnts[x]+=1
            cntg[y]+=1
            if(x==y):
                bull[x]+=1
        ansA=0
        ansB=0
        for i in range(10):
            ansA+=bull[i]
            ansB+=min(cntg[i]-bull[i],cnts[i]-bull[i])
        return str(ansA)+'A'+str(ansB)+'B'
s=Solution()
print(s.getHint('1123','0111'))