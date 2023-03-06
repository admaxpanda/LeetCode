#include <cstdio>
int sum1[1000],sum2[1000];
int lowbit(int x){
    return x&(-x);
}
void change(int j,ing k){
    int i=j;
    while(j<=n){
        sum1[j]+=k;
        sum2[j]+=k*(i-1);
        j+=lowbit(j);
    }
}