#include <stdio.h>
int gcd(int a,int b){
    if(b)
        return gcd(b,a%b);
    else
        return a;
}
void rotate(int* nums, int numsSize, int k){
    k%=numsSize;
    int round=gcd(numsSize,k);
    for(int j=0;j<round;j++){
        int pos=j;
        int tmp=nums[pos],tmpold;
        for(int i=0;i<numsSize/round;i++){
            tmpold=tmp;
            pos+=k;
            if(pos>=numsSize)pos-=numsSize;
            tmp=nums[pos];
            nums[pos]=tmpold;
            //printf("*%d %d\n",tmpold,tmp);
        }
        nums[j]=tmpold;
        // for(int i=0;i<numsSize;i++)
        // printf("%d\n",nums[i]);
        // printf("\n\n");
    }
}

int main(){
    int nums[]={1,2,3,4,5,6,};
    int size=6;
    rotate(nums,size,3);
    for(int i=0;i<size;i++)
        printf("%d\n",nums[i]);
}