int searchInsert(int* nums, int numsSize, int target){
    int l=0,r=numsSize-1;
    int mid=0;
    while(r-l>1){
        mid=l+((r-l)>>1);
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
    if(nums[l]>target)return l;
    if(mid==l||mid==r)
        if(nums[r]>target)
            return r;
        else 
            return r+1;
    else{
        if(nums[mid]>target)
            return mid;
        if(nums[r]>target)
            return r;
        else 
            return r+1;
    }
}