struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdlib.h>
int *ans,now;
int cmp(const void *a,const void* b){
    return *(int*)a- *(int*)b;
}
void dfs(struct TreeNode* n){
    if(n->left)
        dfs(n->left);
    ans[now++]=n->val;
    if(n->right)
        dfs(n->right);
}
int* getAllElements(struct TreeNode* root1, struct TreeNode* root2, int* returnSize){
    ans=malloc(sizeof(int)*10005);
    now=0;
    if(root1)
        dfs(root1);
    if(root2)
        dfs(root2);
    qsort(ans,now,sizeof(int),cmp);
    *returnSize=now;
    return ans;
}