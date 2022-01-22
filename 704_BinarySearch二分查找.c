int search(int* nums, int numsSize, int target){
    int l=0,r=numsSize-1;
    int mid=0;
    while(r-l>1){
        mid=(r+l)/2;
        if(nums[mid]==target)
            return mid;
        if(nums[mid]>target)
            r=mid;
        else
            l=mid;
    }
    if(nums[mid]==target)return mid;
    if(nums[l]==target)return l;
    if(nums[r]==target)return r;
    return -1;
}
#include <stdio.h>
int main(){
    int nums[6]={-1,0,3,5,9,12};
    //printf("QAQ");
    printf("%d",search(nums,6,2));
}