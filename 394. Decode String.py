class Solution:
    def decodeString(self, s: str) -> str:
        def find(s,i):
            num=0
            ans=''
            while(i<len(s)):
                # print(s[i],' ',num,' ',ans)
                if(s[i].isalpha()):
                    ans+=s[i]
                elif(s[i].isdigit()):
                    if(num==0):
                        num=int(s[i])
                    else:
                        num=num*10+int(s[i])
                elif(s[i]=='['):
                    cur,i=find(s,i+1)
                    ans+=cur*num
                    num=0
                elif(s[i]==']'):
                    return ans,i
                i+=1
            return ans
        return find(s,0)
s=Solution()
print(s.decodeString('3[a]2[bc]'))

                