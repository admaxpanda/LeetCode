n=3
ans=0
f=[1,1]
for i in range(20):
    f.append(0)
def dfs(length):
    
    if(length==0):
        return 1
    num=0
    for i in range(0,length):
        if(f[i]==0):
            f[i]=dfs(i)
        if(f[length-i-1]==0):
            f[length-i-1]=dfs(length-i-1)
        num+=f[i]*f[length-i-1]
    return num
print(dfs(length=3))
# def dfs(l,m,r):
#     if(l==m and m==r):
#         return 1
#     ll=0
#     rr=0
#     if(l==m):
#         ll=1
#     for i in range(l,m):
#         ll+=dfs(l,i,m-1)
#     if(m==r):
#         rr=1
#     for i in range(m+1,r+1):
#         rr+=dfs(m+1,i,r)
#     return ll*rr

# for i in range(n):
#     ans+=dfs(0,i,n-1)
#     print(ans)
# print(ans) 
    