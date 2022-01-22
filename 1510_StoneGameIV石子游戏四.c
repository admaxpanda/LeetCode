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