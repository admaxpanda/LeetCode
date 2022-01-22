#include <stdio.h>
int isBadVersion(int v){
    if(v>8)return 1;
    else return 0;
}
int firstBadVersion(int n) {
    int l=0,r=n-1;
    int mid=0;
    while(r-l>1){
        mid=l+((r-l)>>1);
        if(isBadVersion(mid))
            r=mid;
        else 
            l=mid;
    }
    if(isBadVersion(l))return l;
    if(isBadVersion(mid))return mid;
    if(isBadVersion(r))return r;
    return n;
}
int main(){
    printf("%d",firstBadVersion(5));
}