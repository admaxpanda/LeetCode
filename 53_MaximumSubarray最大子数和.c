#include <stdlib.h>
int maxSubArray(int* nums, int numsSize){
    int dp,max;
    dp=max=nums[0];
    for(int i=1;i<numsSize;i++){
        if(dp+nums[i]>nums[i]){
            dp+=nums[i];
            max=dp;
        }
        else{
            if(nums[i]>max)
                max=nums[i];
            dp=nums[i];
        }
    }
    return max;
}