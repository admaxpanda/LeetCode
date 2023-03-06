n=[8,8,1,5,6,2,5,3,3,9]
maxn=max(n)
for i in range(0,maxn):
    for k in n:
        if(k+i>=maxn):
            print('■',end=' ')
        else:
            print('□',end=' ')
    print('')