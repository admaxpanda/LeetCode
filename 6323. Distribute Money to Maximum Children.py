class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if(money==4 and children==1):
            return -1
        if(money<children):
            return -1
        if(children*8==money):
            return children
        if(children*8==money+4):
            return children-2
        for i in range(children-1,-1,-1):
            if(i*8+children-i<=money):
                return i
        return -1
s=Solution()
print(s.distMoney(2,2))