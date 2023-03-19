#include <stdio.h>
#include <stdlib.h>
#define EDGETOT 0
typedef struct queue{
    int pos;
    int cost;
    struct queue *nxt;
}queue;
void getfront(queue *q,int *pos,int *cost){
    *pos=q->pos;
    *cost=q->cost;
}
queue* push(queue *q,int pos,int cost){
    if(q){
        queue* tmp=q;
        while(tmp->nxt)tmp=tmp->nxt;
        queue *newone=malloc(sizeof(queue));
        newone->pos=pos;
        newone->cost=cost;
        newone->nxt=NULL;
        tmp->nxt=newone;
    }
    else{
        q=malloc(sizeof(queue));
        q->pos=pos;
        q->cost=cost;
        q->nxt=NULL;
    }
    return q;
}
queue* pop(queue *q){
    if(q->nxt){
        queue *tmp=q;
        q=q->nxt;
        free(tmp);
        return q;
    }
    else if(q)
        free(q);
    return NULL;
}
int getlenth(queue *q){
    int cnt=0;
    while(q->nxt){
        q=q->nxt;
        cnt++;
    }
    return cnt;
}
int e[1005][1005];
int secondMinimum(int n, int** edges, int edgesSize, int* edgesColSize, int time, int change){
    
    e[0][0]=n;
    int a,b;
    //a,b点
    //e[0][0]记录总点数
    //e[i][0]计入第i个点的边数
    //e[i][k]计入第i个点的第k条边连向的点的编号
    for(int i=0;i<edgesSize;i++){
        //printf("a:%d b:%d\n",edges[i][0],edges[i][1]);
        a=edges[i][0];
        b=edges[i][1];
        e[a][EDGETOT]++;
        e[b][EDGETOT]++;
        e[a][e[a][EDGETOT]]=b;
        e[b][e[b][EDGETOT]]=a;
    }
    // for(int i=1;i<=n;i++){
    //     printf("%d ",i);
    //     for(int k=1;k<=e[i][EDGETOT];k++)
    //         printf("%d ",e[i][k]);
    //     printf("\n");
    // }
    int minest=1e9;
    queue *q=NULL;
    q=push(q,1,0);
    //printf("q%d\n",q);
    while(q){
        int nowpos,nowcost;
        getfront(q,&nowpos,&nowcost);
        //printf("pos%d cost%d\nlenth:%d\n",nowpos,nowcost,getlenth(q));
        q=pop(q);
        if(nowpos==n){
            if(minest==1e9)
                minest=nowcost;
            else if(nowcost>minest)
                return nowcost;
        }
        if((nowcost/change)%2)
            nowcost=((nowcost/change)+1)*change;
        for(int i=1;i<=e[nowpos][EDGETOT];i++){
            //printf("to:%d\n",e[nowpos][i]);
            q=push(q,e[nowpos][i],nowcost+time);
        }
        
    }
    return 0;
}
int main(){
    int *QAQ=NULL;
    int t[][2]={
        {1,2},
        {1,3},
        {2,4},
        {3,5},
        {5,4},
        {4,6}
    };
    int **a;
    //printf("%d",sizeof(int*));
    //a=t;
    int n=6;
    int lena=6;
    int time=3;
    int change=100;
    a=malloc(sizeof(int*)*lena);
    for(int i=0;i<lena;i++)
        a[i]=malloc(sizeof(int*) * 2);
    for(int i=0;i<lena;i++)
        for(int k=0;k<2;k++)
            a[i][k]=t[i][k];

    printf("%d",secondMinimum(n,a,lena,QAQ,time,change));
}