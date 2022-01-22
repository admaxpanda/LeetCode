int fib(int n){
    int ls=1,ls2=0;
    if(n==0)return 0;
    if(n==1)return 1;
    for(int i=2;i<=n;i++){
        ls^=ls2^=ls^=ls2;
        ls+=ls2;
    }
    return ls;
}