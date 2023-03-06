class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sa=[]
        sb=[]
        for i in s:
            if(i=='#'):
                if(sa):
                    sa.pop()
            else:
                sa.append(i)
        for i in t:
            if(i=='#'):
                if(sb):
                    sb.pop()
            else:
                sb.append(i)
        print(sa,sb)
        return sa==sb

s=Solution()
print(s.backspaceCompare("y#fo##f","y#f#o##f"))