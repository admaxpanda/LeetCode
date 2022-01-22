int tribonacci(int n){
    int ls=1,ls2=1,ls3=0;
    if(n==0)return 0;
    if(n==1)return 1;
    if(n==2)return 1;
    for(int i=3;i<=n;i++){
        ls3^=ls2^=ls3^=ls2;
        ls2^=ls^=ls2^=ls;
        ls+=ls2+ls3;
    }
    return ls;
}