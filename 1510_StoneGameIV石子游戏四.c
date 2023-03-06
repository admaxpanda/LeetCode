/*
    一个DP的策略，实际上没有“博弈”中的最优策略
    在都是最优的情况下，只有一个胜利者，如果A赢，B就输
    因此只需要先找到能赢的，不能赢就是输，不能输就是赢
*/
#include <stdlib.h>
int winnerSquareGame(int n){
    char *dp=malloc(n+1);
    for(int i=0;i<=n;i++)
        dp[i]=0;
    for(int i=1;i<=n;i++)
        for(int k=1;k*k<=i;k++)
            if(dp[i-k*k]==0){
                dp[i]=1;
                break;
            }
    return dp[n];
}