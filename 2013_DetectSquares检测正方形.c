#include <stdlib.h>
typedef struct {
    int a[1005][1005];
} DetectSquares;
DetectSquares* detectSquaresCreate() {
    DetectSquares *d=malloc(sizeof(DetectSquares));
    for(int i=0;i<1005;i++)
        for(int k=0;k<1005;k++)
            d->a[i][k]=0;
    return d;
}
void detectSquaresAdd(DetectSquares* obj, int* point, int pointSize) {
    obj->a[point[0]][point[1]]+=1;
}

int detectSquaresCount(DetectSquares* obj, int* point, int pointSize) {
    int ans=0;
    int x=point[0],y=point[1];
    for(int i=1;i<=1000;i++){
        if(x+i<=1000&&y+i<=1000)
            ans+=obj->a[x][y+i]*obj->a[x+i][y]*obj->a[x+i][y+i];
        if(x+i<=1000&&y-i>=0)
            ans+=obj->a[x][y-i]*obj->a[x+i][y]*obj->a[x+i][y-i];
        if(x-i>=0&&y+i<=1000)
            ans+=obj->a[x][y+i]*obj->a[x-i][y]*obj->a[x-i][y+i];
        if(x-i>=0&&y-i>=1000)
            ans+=obj->a[x][y-i]*obj->a[x-i][y]*obj->a[x-i][y-i];
    }
    return ans;
}

void detectSquaresFree(DetectSquares* obj) {
    free(obj);
}
    // int p[1005][2],cntx=0,cnty=0;
    // for(int i=0;i<=1000;i++){
    //     if(i!=point[0])
    //         for(int k=0;k<obj->a[i][point[1]];k++)
    //             p[cntx++][0]=i;
    //     if(i!=point[1])
    //         for(int k=0;k<obj->a[point[0]][i];k++)
    //             p[cnty++][1]=i;
    // }
    // for(int i=0;i<cntx;i++){
    //     for(int k=0;k<cnty;k++){
    //         ans+=(obj->a[p[i][0]][p[k][1]]);
    //     }
    // }
    // for(int i=0;i<=1000;i++){
    //     if(i==point[0])
    //         continue;
    //     for(int k=0;k<=1000;k++){
    //         if(k==point[1])
    //             continue;
    //         ans+=obj->a[i][k]*obj->a[point[0]][k]*obj->a[i][point[1]]
    //     }
    // }
/**
 * Your DetectSquares struct will be instantiated and called as such:
 * DetectSquares* obj = detectSquaresCreate();
 * detectSquaresAdd(obj, point, pointSize);
 
 * int param_2 = detectSquaresCount(obj, point, pointSize);
 
 * detectSquaresFree(obj);
*/