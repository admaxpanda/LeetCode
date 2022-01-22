#include <stdlib.h>
#include <stdio.h>
#include <string.h>
int* sortedSquares(int* nums, int numsSize, int* returnSize){
    int *ans=malloc(sizeof(int)*numsSize);
    int l=-1,r=0;
    for(int i=0;i<numsSize;i++)
        if(nums[i]<0){
            l=i;
            r=i+1;
        }
        else
            break;
    int tot=0;
    //printf("%d %d\n",l,r);
    while(tot<numsSize){
        //printf("%d %d\n",nums[l],nums[r]);
        if(l>=0&&r<numsSize)
            if((-nums[l])<nums[r]){
                ans[tot]=nums[l]*nums[l];
                l--;
                tot++;
            }
            else{
                ans[tot]=nums[r]*nums[r];
                tot++;
                r++;
            }
        else if(l>=0){
            ans[tot]=nums[l]*nums[l];
            l--;
            tot++;
        }
        else{
            ans[tot]=nums[r]*nums[r];
            tot++;
            r++;
        }
    }
    *returnSize=tot;
    return ans;
}
int main(){
    int nums[]={-5,-3,-2,-1};
    int rsize=5;
    int *tot=sortedSquares(nums,sizeof(nums)/sizeof(int),&rsize);
    for(int i=0;i<rsize;i++)
        printf("%d\n",tot[i]);
    free(tot);
}